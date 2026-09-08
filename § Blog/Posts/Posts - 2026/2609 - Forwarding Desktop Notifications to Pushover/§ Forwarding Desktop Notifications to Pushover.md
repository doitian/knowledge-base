---
date: '2026-09-08T21:00:00+0800'
draft: false
aliases: ["Forwarding Desktop Notifications to Pushover"]
tags:
  - automation
  - bun
  - desktop
  - linux
  - script
  - windows
description: "One binary forwards mako and Windows toasts to Pushover. Linux needs one hook line; Windows needs a signed sparse-identity MSIX."
---

# Forwarding Desktop Notifications to Pushover

**Status**:: #x
**Zettel**:: #zettel/permanent
**Created**:: [[2026-09-08]]
**URL**:: [blog.iany.me](https://blog.iany.me/2026/09/forwarding-desktop-notifications-to-pushover/)

I already forwarded **mako** notifications to Pushover on Linux. The hook is tiny: mako runs a command with the notification id, the script reads `makoctl list -j`, skips loops and Pushover itself, and POSTs to the Pushover API.

Windows has no equivalent of `on-notify=exec`. I wanted one binary, `dn-pushover`, that does the same job on both desktops: titles become `[DN][hostname] …` so a notification that bounces back is easy to drop.

Linux stayed simple. Windows did not.

<!--more-->

## How it works

![[Notification forwarding setup paths.svg]]

**Linux.** `dn-pushover setup` writes a managed block into `~/.config/mako/config`:

```text
on-notify=exec dn-pushover "$id"
```

Then it reloads mako. If `makoctl` is missing, setup fails instead of pretending to work. An old `mako-pushover` block is migrated so deleting the old binary cannot leave a dead hook behind.

**Windows.** There is no desktop-wide exec hook. The supported API is `UserNotificationListener`: after the user grants access, an app can read other apps' toast notifications. `setup` therefore:

1. Checks Pushover credentials.
2. Builds a small C# WinForms helper (first time only; later setups reuse the exe).
3. Packs a **sparse identity MSIX** (manifest + logos; the exe lives next to it via `-ExternalLocation`).
4. Signs it and registers it.
5. Launches the helper. You click **Allow Access** and accept the Windows prompt.
6. The helper baselines whatever is already in the notification center, then polls for new toasts and runs `dn-pushover --forward` with JSON on stdin.

`teardown` stops the helper. `teardown --cleanup` also unregisters the package and deletes `%LOCALAPPDATA%\dn-pushover`. There is no autostart: after logout, run `setup` again.

The JS side is shared: prefix, truncation, skip `[DN]` / `[mako]` / recognizable Pushover traffic, then `send()`.

## Gotchas

### Linux is a hook. Windows is an identity.

`UserNotificationListener` is not "read the notification database." It is a capability on a **packaged** app. An unpackaged Win32 process can call `RequestAccessAsync` and even get `Allowed` while `GetNotificationsAsync` returns an empty list and Settings never shows the app.

A loose `Add-AppxPackage -Register` development package (`SignatureKind=None`) has the same problem. Windows will not list it under **Privacy & security → Notifications** (the *read* list, not **System → Notifications**, which is the *send* list).

What worked was a **signed sparse MSIX** whose publisher matches the exe's `app.manifest` `msix` element, with `uap3:Capability Name="userNotificationListener"` and `AppListEntry` **not** set to `none`.

### Signing is not optional, and per-user trust is not enough

Self-signed is fine for a personal machine. The private key stays in `CurrentUser\My`. Importing the *public* cert into `CurrentUser\TrustedPeople` does **not** make you a public CA; it only means this user trusts this publisher.

MSIX deployment still failed with `0x800B0109` (untrusted root) until the public cert was also in **`LocalMachine\TrustedPeople`**. That needs a one-time UAC. Later setups skip the import if the thumbprint is already there.

`powershell.exe -NoProfile` has no `Cert:` drive. `Import-Module PKI` under `$ErrorActionPreference = 'Stop'` blew up on duplicate type data. Certificate create/import had to use `X509Store` / `CertificateRequest` instead of `New-SelfSignedCertificate`.

### The SDK is not the runtime

A .NET 10 **runtime** cannot `dotnet publish`. First Windows setup needs a **.NET 10 SDK** (Scoop: `versions/dotnet-sdk-lts`) plus Windows SDK tools `makeappx` and `signtool`. Setup runs PowerShell with `-NoProfile`, so Scoop's shims are not on `PATH`; it has to look in `~/scoop/apps/dotnet-sdk-lts/current/` itself.

Setup also **skips rebuilding** if the helper exe already exists, and used to **skip re-registering** if the package was already installed. That is how a stale unsigned package and an old helper survived "I already ran setup." `teardown --cleanup` is the rebuild switch. Signed packages under `WindowsApps` must actually be removed; if cleanup no-ops, `Get-AppxPackage` will still show them.

### The compiled Bun binary is a different program

`import.meta.main` is false inside a Bun-compiled `.exe`. Guarding `main()` with only that flag made `dn-pushover setup` exit 0 with **no output**. Detect the virtual `B:/~BUN/` / `$bunfs` entrypoint as well.

`Bun.stdin.text()` in that same compiled Windows exe did not read the helper's piped JSON. `--forward` exited 0, sent nothing. `readStdin()` from Node's `process.stdin` did. A WinForms **AcceptButton** also treated the Enter key from the terminal as **Allow Access**, so setup "returned immediately" after the first successful grant.

Substring `/pushover/i` on the app id matched `DnPushover.NotificationListener` and dropped every toast. Skip the Pushover *product*, not any name that contains those letters.

## Debug process

The failure mode was always the same from the outside: a Windows toast appeared, Pushover stayed quiet. The pipeline has three stages; each can succeed while the next never runs.

![[Notification forwarding failure stages.svg]]

**Is the listener alive?** Process + `%LOCALAPPDATA%\dn-pushover\listener.log`. Empty log with a running process meant polls were not seeing new toasts (or the form was hidden and the timer never ticked). `Listener ready; N existing toast(s)` means those N will never be forwarded — send a **new** toast after ready.

**Does JS send?** Pipe JSON into `dn-pushover --forward` and watch the Pushover API. A 200 body `{"status":1,"request":"…"}` means credentials and the API are fine. If that works and the listener still does not, the helper is not invoking the CLI you think it is (`config.json` points at `dist\dn-pushover.exe`), or the CLI is skipping the payload.

**What did `--forward` actually do?** Temporary logging of argv, stdin length, skip vs send, and the API status. That is how `Bun.stdin.text()` was caught: argv logged, stdin never read, process exit 0, no HTTP. After the stdin fix, the same toast showed `apiStatus: 200`. Edge then showed the Pushover copy with a `[DN]` title; that one is supposed to be skipped so you do not loop.

Direct `fetch` to `https://api.pushover.net/1/messages.json` (user key + desktop-notification token, no secrets in logs) is the ground truth. If that returns `status: 1` and the device still shows nothing, you are looking at the wrong Pushover app or device, not at this script.

## Practical checklist

- Linux: `makoctl` on mako's PATH; `dn-pushover setup`; section-specific `on-notify` rules win over the global hook.
- Windows: .NET 10 SDK + Windows SDK; one UAC to trust `CN=dn-pushover` in `LocalMachine\TrustedPeople`; `dn-pushover setup`; click Allow Access; Privacy list is *access*, not senders.
- After changing helper C# or the Bun CLI: `teardown --cleanup` then `setup`, and use the rebuilt `dist` binary.
- Test with a toast created **after** the listener is ready. Expect `[DN][hostname]` on Pushover.
