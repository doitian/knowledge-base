# Set Up a New Mac

#macOS

## Prepare the Setup

* Backup `Surge.app` and the profile.
* Backup the `.gnupg` folder.

## Restore Network

* Restore `Surge.app` and the profile from the backup. Start Surge to enable the proxy.

## Set Up Yubikey

* Install Homebrew
* Set up environment variables for Homebrew

    ```
    export HOMEBREW_BOTTLE_DOMAIN=https://mirrors.ustc.edu.cn/homebrew-bottles
    export HOMEBREW_NO_BOTTLE_SOURCE_FALLBACK=1
    ```

* Install GnuPG

    ```
    brew install gnupg pinentry-mac
    ```

* Restore the `.gnupg` folder. Enable SSH support and use `pinentry-mac` in `.gnupg/gpg-agent.conf`

    ```
    default-cache-ttl 600
    max-cache-ttl 7200
    enable-ssh-support
    pinentry-program /usr/local/bin/pinentry-mac
    ```

* Reboot the Mac if `gpg --card-status` cannot detect the card.
* Use GPG as the SSH agent and continue restoring dotfiles and other repositories from Github

    ```
    export SSH_AUTH_SOCK=$HOME/.gnupg/S.gpg-agent.ssh
    ```

* Tune the macOS preferences
    * Mouse/trackpad speed
    * Disable auto correction
    * Speed up key repetition