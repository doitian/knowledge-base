# /// script
# requires-python = ">=3.13"
# dependencies = ["inflector>=3.1.1", "PyYAML>=6", "tzdata"]
# ///

import contextlib
import datetime as dt
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import types
import unittest
from unittest.mock import patch
from zoneinfo import ZoneInfo

from inflector import English
import yaml

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ['create-entry', 'create-post', 'create-journal']
INSTANTS = ['2025-12-31T23:30:00+00:00', '2026-01-01T00:30:00+00:00',
            '2024-02-29T23:30:00+00:00', '2026-03-08T07:30:00+00:00', '2026-11-01T06:30:00+00:00']
ZONES = ['UTC', 'Asia/Shanghai', 'America/New_York', 'Pacific/Kiritimati']
TITLES = ['Simple Title', "Alice's Note", '中文 👋', 'A & B', 'null', '2024-02-29']
SAMPLES = []


def properties(text):
    return yaml.safe_load(text.split('---\n', 2)[1])


def run_script(script, directory, title, instant, zone, *, interactive=False, source=None):
    instant = dt.datetime.fromisoformat(instant)
    timezone = ZoneInfo(zone)
    class Clock(dt.datetime):
        @classmethod
        def now(cls, tz=None):
            return cls.fromtimestamp(instant.timestamp(), tz)

        def astimezone(self, tz=None):
            return super().astimezone(tz or timezone)
    clock = types.SimpleNamespace(datetime=Clock, timezone=dt.timezone)
    path = ROOT / 'bin' / script
    source = source if source is not None else path.read_text(encoding='utf-8')
    previous = Path.cwd()
    output = io.StringIO()
    try:
        os.chdir(directory)
        with patch.dict(sys.modules, {'datetime': clock}), patch.object(sys, 'argv', [str(path)] + ([] if interactive else [title])), \
                patch('builtins.input', return_value=title) as prompt, contextlib.redirect_stdout(output):
            exec(compile(source, str(path), 'exec'), {'__name__': '__main__', '__file__': str(path)})
            if interactive:
                prompt.assert_called_once_with('title: ')
            else:
                prompt.assert_not_called()
    finally:
        os.chdir(previous)
    return directory / output.getvalue().strip()


class NoteCreationTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix='blog-note-creation-')
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)

    @classmethod
    def tearDownClass(cls):
        destination = os.environ.get('BRAIN_BLOG_CREATION_SAMPLES')
        if destination:
            target = Path(destination).resolve()
            if target.is_relative_to(ROOT):
                raise AssertionError('Evidence must stay outside the blog worktree')
            target.write_text(json.dumps(SAMPLES, ensure_ascii=False, indent=2) + '\n', encoding='utf-8', newline='\n')

    def test_metadata_dates_paths_and_existing_file_noop(self):
        number = 0
        for script in SCRIPTS:
            for instant in INSTANTS:
                for zone in ZONES:
                    for title in TITLES:
                        with self.subTest(script=script, instant=instant, zone=zone, title=title):
                            directory = self.root / str(number)
                            directory.mkdir()
                            number += 1
                            file = run_script(script, directory, title, instant, zone)
                            now = dt.datetime.fromisoformat(instant).astimezone(ZoneInfo(zone))
                            expected = {'tags': ['i', 'zettel/literature' if script == 'create-journal' else 'zettel/permanent'],
                                        'created': f'[[{now:%Y-%m-%d}]]'}
                            if script == 'create-entry':
                                expected_path = Path(title) / f'§ {title}.md'
                            else:
                                section = 'Journals' if script == 'create-journal' else 'Posts'
                                expected_path = Path('§ Blog') / section / f'{section} - {now.year}' / f'{now:%y%m} - {title}' / f'§ {title}.md'
                                expected.update(date=now.strftime('%FT%T%z'), draft=True, aliases=[title])
                                slug = English().urlize(title.lower()).replace('_', '-')
                                prefix = 'journal/' if script == 'create-journal' else ''
                                expected['url'] = f'[blog.iany.me](https://blog.iany.me/{prefix}{now:%Y/%m}/{slug}/)'
                            self.assertEqual(file.relative_to(directory), expected_path)
                            content = file.read_bytes()
                            self.assertNotIn(b'\r', content)
                            text = content.decode('utf-8')
                            self.assertEqual(properties(text), expected)
                            self.assertIn('# ' + title + '\n', text)
                            self.assertNotIn('**Status**::', text)
                            self.assertNotIn('**URL**::', text)
                            ns = 1700000000987654300
                            os.utime(file, ns=(ns, ns))
                            self.assertEqual(run_script(script, directory, title, instant, zone), file)
                            self.assertEqual((file.read_bytes(), file.stat().st_mtime_ns), (content, ns))
                            SAMPLES.append({'script': script, 'instant': instant, 'zone': zone, 'title': title,
                                            'path': expected_path.as_posix(), 'text': text, 'properties': expected})

    def test_existing_content_classification_order_and_times_untouched(self):
        for script in SCRIPTS:
            directory = self.root / script
            directory.mkdir()
            file = run_script(script, directory, 'Existing', INSTANTS[0], ZONES[0])
            for content in [b'# Legacy note\r\n\n**Status**:: #x\nBody ^kept\n',
                            b'---\nkind: [paralet, app]\r\nstatus: now\nzettel: keyword\ntags: [python]\n---\nKeep [[Link]]\n']:
                with self.subTest(script=script, content=content):
                    file.write_bytes(content)
                    ns = 1700000000987654300
                    os.utime(file, ns=(ns, ns))
                    run_script(script, directory, 'Existing', INSTANTS[0], ZONES[0])
                    self.assertEqual((file.read_bytes(), file.stat().st_mtime_ns), (content, ns))

    def test_interactive_title_matches_argument_title(self):
        for script in SCRIPTS:
            a, b = self.root / (script + '-a'), self.root / (script + '-b')
            a.mkdir()
            b.mkdir()
            first = run_script(script, a, 'Prompt 中文', INSTANTS[1], ZONES[2], interactive=True)
            second = run_script(script, b, 'Prompt 中文', INSTANTS[1], ZONES[2])
            self.assertEqual(first.relative_to(a), second.relative_to(b))
            self.assertEqual(first.read_bytes(), second.read_bytes())

    def test_isolated_cli(self):
        for script in SCRIPTS:
            directory = self.root / script
            directory.mkdir()
            before = dt.datetime.now(dt.timezone.utc).astimezone()
            result = subprocess.run([sys.executable, '-B', '-X', 'utf8', str(ROOT / 'bin' / script), 'CLI', '中文'],
                                    cwd=directory, capture_output=True, text=True, encoding='utf-8')
            after = dt.datetime.now(dt.timezone.utc).astimezone()
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            file = directory / result.stdout.strip()
            self.assertTrue(file.is_relative_to(directory))
            values = properties(file.read_text(encoding='utf-8'))
            self.assertIn(values['created'], [f'[[{date:%Y-%m-%d}]]' for date in [before, after]])
            self.assertEqual(values['tags'], ['i', 'zettel/permanent'] if script != 'create-journal' else ['i', 'zettel/literature'])


if __name__ == '__main__':
    unittest.main()
