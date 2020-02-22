---
date: '2011-05-18'
description: How Mendeley manages documents and citations.
title: 'Mendeley: Cross Platform Research Management Tool'
---

# Mendeley Cross Platform Research Management Tool

#utility #productivity #app

[Mendeley][] is a research management tool for desktop & web. It has clients for Linux, Mac, Windows and iPhone and a Web interface. Mendeley can manage any document, but is better to work with PDF. The file meta data are synchronized though Mendeley server. The attached files (PDF or any other formats) can also be synchronized, but the free account has a quota of 500MB. However, the attached files directory and underlying sqlite database can be synchronized manually.

<!--more-->

Mendeley is also a collaboration platform that all the added documents can be shared with others. Co-workers can create group to maintain a shared documents list. Mendeley also maintains a public database, from which you can search and add result to your Mendeley library directly. Mendeley also supports importing data from other services such as [CiteULike][].

Mendeley client supports tags and PDF file indexing. It makes easy to search documents. If you use BibTex to manage references in your writings, the client can export all documents into a BibTex file and synchronize your further changes in Mendeley to that file.

## Get Started

You need to register an account in [Mendeley][]. Then [download](http://www.mendeley.com/download-mendeley-desktop/) a client for your platform. Following is the snapshot of Mendeley under Linux.

/mendeley.png "Mendeley Desktop"

## Add Documents

The documents can be added by adding attached files directly. Mendeley will try to extract meta information from files. It is also able to create an entry and edit meta information manually, and attach file later.

But the most convenient solution is search the documents in [Mendeley database][], add the search result and synchronize to the client, then attach files in client. However, I have not found a way to use a search result as the meta information of an existing document.

The meta information and attached files can be managed in details panel, which is opened by clicking the handler in the right side.

## Synchronize

Documents meta information are all synchronized. The attached files are synchronized according to the per folder settings. All folders are listed under My Library. Just select the folder you want to synchronize and edit its settings to enable.

If attached files are not synchronize attached files, their local paths are also not synchronized. It is very inconvenient. You cannot synchronize your attached files manually across machines with the same position and let Mendeley just synchronize the meta information.

However, you can manually synchronize the attached files directory and underlying sqlite database.

### Organize files

Open options dialog through menu *Tools -> Options* and switch to "File Organizer" tab.

- Enable "Organize my files" and select a directory such as "/Mendeley". It must be the same in different machines. Otherwise the manual solution cannot synchronize between Windows and Mac, Linux. Since in Windows, the path name contains the driver name, so the database also cannot be shared between Windows and other systems having root path.
- Enable "Sort files into sub-folders" to avoid file name conflicts. I prefer the Folder path `Year`/`Author`.

/file_organizer.png "File Organizer"

### Manual Synchronization

The attached files directory and the meta info sqlite database can be synchronized using [Dropbox][], [Rsync][] or [Lsyncd][]. For Dropbox, just make symbol links in the Dropbox directory.

The database file is created when you have logged-in in the client. It is stored in different location in different platform. I have figured out its location in Linux and Mac (replace email@example.com with your own registered email).

- Linux: `$HOME/.local/share/data/Mendeley Ltd./Mendeley Desktop/email@example.com@www.mendeley.com.sqlite`
- Mac: `$HOME/Library/Application Support/Mendeley Desktop/email@example.com@www.mendeley.com.sqlite`

Because the sqlite database file is binary, you cannot simply merge two database files. I recommend to add and edit documents only in one machine, and use other machines as read only copies. Otherwise you may loose data during synchronization.

[Mendeley]: http://www.mendeley.com/
[CiteULike]: http://www.citeulike.org/ "CiteULike: Everyone's library"
[Mendeley database]: http://www.mendeley.com/research-papers/
[Dropbox]: http://db.tt/I4zEuqN "cloud service for file synchronization"
[Rsync]: http://en.wikipedia.org/wiki/Rsync "file synchronization command"
[Lsyncd]: http://code.google.com/p/lsyncd/ "Live Syncing (Mirror) Daemon"
