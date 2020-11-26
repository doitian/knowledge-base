---
comment: true
date: '2020-02-02T12:15:10+08:00'
description: How to configure Apple Mail to download only the mails in Gmail inbox.
katex: false
share: true
title: How to Download Only Gmail Inbox
---

# Download Only Gmail Inbox

#powerTool

I prefer reading my mails in the Gmail web client directly. I rarely send new mails or replies. But when I do, I want to use PGP to encrypt or sign the mail. I have tried two extensions to use PGP in Gmail, FlowCrypt and Mailvelope. But both of them are far from a competent solution for me. GPG Mail in the GPG Suite for macOS is still my preferred way. However, GPG Mail is an Apple Mail plugin, which requires downloading mails first. Based on my scenarios, I only need to download the mails I left in the inbox. But the basic setup of Gmail in Apple Mail will download many mails in the background.

I tried POP3. It has two issues:

* The status is not synchronized with the server. I can configure Gmail to archive the mails which have been downloaded via POP3, but that means once I have downloaded mails, I must process them locally. This is a burden, since I only want to reply several mails in the client.
* POP3 does not observe the filter which auto archives new mails. The filtered emails still occur in the client.

IMAP is still the better choice. The real issue is indeed that Apple Mail uses remote IMAP mail boxes for Drafts, Sent, Junk, Trash and Archive by default. If it uses local mail boxes instead, the client will no longer try to synchronize this mail boxes.

Following is the detailed instructions to setup a Gmail IMAP client which only downloads mails in the inbox.

First go to the Gmail [label settings](https://mail.google.com/mail/u/0/#settings/labels). Disable all the "Show in IMAP" options except the one for inbox.

Since Apple Mail does not allow configuring mailboxes for a Google account, I have to generate an [app password](https://myaccount.google.com/apppasswords) to add the Gmail as an IMAP account. Open Mail app, add account and choose IMAP from "Other mail account…".

After adding the new account, use local mail boxes in the Mailbox Behaviors settings pane. Leave the Archive mail box remote, since we cannot change it.

![[apple-mail-mailboxes-behaviors.png|Apple Mail Mailboxes Behaviors Settings Pane]]

Now Apple Mail will only download mails in the inbox. There is one last thing, if I archive a mail in the client, it will be labeled `[Imap]/Archive` in Gmail, you may want to hide it from the label list and message like me in the [labels settings](https://mail.google.com/mail/u/0/#settings/labels).
