# LxRunOffline

#windows #wsl

[LxRunOffline](https://github.com/DDoSolitary/LxRunOffline) is a full-featured utility for managing Windows Subsystem for Linux (WSL).

LXRunOffline provides a uniform way to download various distributions and import them as WSL instances into any directories.

### Install LxRunOffline

- Scoop

    ```
    scoop bucket add extras
    scoop install lxrunoffline
    ```

- Chocolatey

    ```
    choco install lxrunoffline
    ```

- Or download binaries directly from [GitHub](https://github.com/DDoSolitary/LxRunOffline/releases).

### Download an Image

The download URL pattern is

```
https://lxrunoffline.apphb.com/download/{distro}/{version}
```

Choose the distribution and version using the [LXRunOffline Wiki](https://github.com/DDoSolitary/LxRunOffline/wiki).

For example:

- Ubuntu Jellyfish: `https://lxrunoffline.apphb.com/download/Ubuntu/jellyfish`
- Fedora 35: `https://lxrunoffline.apphb.com/download/Fedora/35`

### Import the Image

Assuming that

- `$Name` is the name you give to the new created WSL instance.
- `$Target` is the path to the directory where you want to store the new WSL instance.
- `$RootFsTar` is the path to the download image file, usually with extension `.tar.gz` or `.tar.xz`.
- Remember to append the required additional argument listed in the Wiki.

Here is the command to create a new WSL instance from the downloaded instance:

```
lxrunoffline.exe i -n "$Name" -f "$RootFsTar" -d "$Target" -v 2 [Append additional argument here]
```

Examples:

- Ubuntu Jellyfish

    ```
    lxrunoffline.exe i -n ubuntu-jellyfish -f ./ubuntu-jellyfish-oci-amd64-root.tar.gz -d D:\WSL\ubuntu-jellyfish -v 2
    ```

- Fedora 35, remember to append `-r .`.

    ```
    lxrunoffline.exe i -n fedora-35 -f ./fedora-35-x86_64.tar.xz -d D:\WSL\ubuntu-jellyfish -v 2 -r .
    ```
