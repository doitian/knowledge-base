---
date: '2021-02-06T20:06:11+0800'
feature: big-sur.jpg
banner: "![[big-sur.jpg]]"
banner_y: 0.4463
---

# Install macOS Big Sur in 2021

#macos

My MacBook's battery capacity is significantly reduced and it has many weird issues so I decide to do a clean installation of macOS Big Sur. This article is a reference for my own reference in case I need to do it again.

<!--more-->

## Preparation

I plan to erase the disk and install a clean copy of macOS, so the first step is creating the bootable installer.

* Back up the data. Follow [these instructions](https://support.apple.com/en-us/HT201065) if I want to sell, give away, or trade in my Mac.
* Get Big Sur from the App Store. This will install the app `Install macOS Big Sur.app` into `/Applications`.
* Insert the USB stick which has at least 8GB capacity. Assuming the stick name is `MyVolume`, create the installer using the USB stick with following command [^1]

    ```
    sudo /Applications/Install\ macOS\ Big\ Sur.app/Contents/Resources/createinstallmedia --downloadassets --volume /Volumes/MyVolume
    ```

    The option `--downloadassets` is optional but is recommended, because without proxy, it is slow to download resources during the installating stage in some regions.

* Reboot the laptop into recovery mode by holding <kbd>Command+R</kbd>. Choose Utilities > Startup Security Utility from the menu bar and allow booting from external media.[^2] This step is **very important** and must be done before erasing the disk because it requires verifying the admin user password in the installed system. I fogot it and had to recover the factory macOS version to just create a user so that I can allow booting from external media.
* Ensure there's a working Internet connection. The installation requires network to do verification.

## Install

Keep the USB stick inserted. Reboot the laptop by holding Option (⌥) this time. This will bring the startup disk selection interface. Select the USB stick, which is shown as "Install Big Sur".

This will boot into the Big Sur recovery mode.

* Use disk utility to erase the disk. Use security options to securely erase the data from the disk if I plan to sell the Mac or send it to the genius bar.
* Quit disk utility and choose to install Big Sur from the menu.

[^1]: [How to create a bootable installer for macOS – Apple Support](https://support.apple.com/en-gb/HT201372)
[^2]: [About Startup Security Utility - Apple Support](https://support.apple.com/en-us/HT208198)
