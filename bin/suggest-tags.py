import argparse
import sys
from pathlib import Path

# Setup paths
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
TAGS_FILE = PROJECT_ROOT / 'tags.txt'

def load_known_tags():
    if not TAGS_FILE.exists():
        return []
    with open(TAGS_FILE, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]

def main():
    parser = argparse.ArgumentParser(description='Generate a prompt to ask Gemini for tag suggestions.')
    parser.add_argument('file', help='Path to the markdown file')
    
    args = parser.parse_args()
    file_path = Path(args.file)

    if not file_path.exists():
        print(f"File not found: {file_path}")
        sys.exit(1)

    known_tags = load_known_tags()
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

    # Construct the prompt
    prompt = "I need tagging suggestions for a blog post.\n\n"
    
    prompt += "Existing known tags:\n"
    prompt += ", ".join(sorted(known_tags))
    prompt += "\n\n"
    
    prompt += "Blog Post Content:\n"
    prompt += "```markdown\n"
    prompt += content
    prompt += "\n```\n\n"
    
    prompt += "Instructions:\n"
    prompt += "1. Analyze the post content.\n"
    prompt += "2. Recommend tags from the 'Existing known tags' list that fit best.\n"
    prompt += "3. Only suggest new tags if absolutely necessary and they follow the 'kebab-case' style.\n"
    prompt += "4. Output the recommended tags as a comma-separated list."

    print(prompt)

if __name__ == '__main__':
    main()

