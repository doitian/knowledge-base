---
date: '2015-02-08'
description: Create ctags index for Ansible to ease navigation in editor.
title: Ctags for Ansible
---

# Ctags For Ansible

#ansible #vim

Ansible uses YAML to define tasks, playbooks and handlers. If the files follow some conventions, it is easy to index them using [Exuberant Ctags][1].

<!--more-->

For example, following ctags options will index all the lines starting with `- name:` in `.yml` and `.yaml` files. Save it as `.ctags` in the playbook or role top directory.

	--langdef=ansible
	--langmap=ansible:.yml.yaml
	--regex-ansible=/^[ \t]*-[ \t]*name:[ \t]*(.+)/\1/k,tasks/
	--languages=ansible,ruby,python

It is assumed that playbook and task files use extension `.yml` or `.yaml`. And `name` field just follows `-`.

	- name: name must be the first field just following the dash
	  hosts: all
	  roles: [ site ]

Now generate the tags

	ctags -R .

And try it in vim

	:tselect /keyword

To make it works with [ctrlp][2] `CtrlPBufTag`, add following config in vimrc

	let g:ctrlp_buftag_types = {
	  \ 'yaml'     : '--languages=ansible --ansible-types=k',
	  \ }

[1]:	http://ctags.sourceforge.net
[2]:	https://github.com/kien/ctrlp.vim
