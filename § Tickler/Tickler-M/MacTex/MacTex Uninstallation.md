## MacTex Uninstallation

### Uninstalling TeX

[Uninstalling - MacTeX - TeX Users Group](http://www.tug.org/mactex/uninstalling.html)

There are two reasons users want to uninstall. Some casual users see TeX on the web, download it to experiment, decide that the program is not their cup of tea, and want to get rid of it. Other users have MacTeX-2018 or another earlier distribution, upgrade to the latest version, and want to reclaim space by erasing the old distribution.

The Apple Installer does not support uninstalling files. However, it is fairly easy to remove most software installed by MacTeX.

The actual TeX distribution TeX Live is by far the largest piece of MacTeX. Luckily, TeX Live is installed in a single directory on the Mac; it is not scattered over several different places. TeX Live 2018 is entirely contained in /usr/local/texlive/2018; the old TeX Live 2017 was in /usr/local/texlive/2017.

The only difficulty is that TeX Live is owned by root and lives in a location that is not commonly visible in the Finder. But it is easy to work around this problem. In the Finder's Go menu, select "Go to Folder"; in the resulting dialog window, type "/usr/local/texlive". You will see folders containing various copies of TeX Live. Drag the folder corresponding to the version of TeX Live you want to uninstall to the trash. You will need to provide an administrative password when asked.

The folder texmf-local is available for local additions to TeX. These local additions are used by all versions of TeX Live, so if you added files for TeX Live 2018, they are still around for TeX Live 2019. When MacTeX is installed, it doesn't touch texmf-local if it already exists, but it creates an empty directory tree if none is present.

Consequently, if you are updating TeX Live to a new version, you want to leave texmf-local alone. But if you are trying to remove all traces of TeX, then remove texmf-local by dragging it to the trash.

### Uninstalling the GUI Applications

This step is easy. The GUI applications are in /Applications/TeX. To uninstall, drag them to the trash.

### Uninstalling the TeX Distribution Data Structure

This data structure takes very little space, so it makes little sense to erase it. But if you must, locate /Library in the Finder and drag the subfolder TeX to the trash. You will be asked to give an Administrator password. Warning: if you have other TeX distributions, they may have also installed files in /Library/TeX, so erasing this folder is then not a good idea.

Incidentally, when you remove a TeX Distribution, say TeX Live 2018, it is not necessary to remove its related links from the TeX Distribution Data structure. The software is smart enough to know that these links no longer point to live data.

### Uninstalling Ghostscript

This step is more difficult. One way to proceed is to open the MacTeX-2019 install package and select "Show Files" from the resulting "File" menu of Apple's installer. This will give a complete list of files installed, and their install locations. Find files related to Ghostscript and remove them. Most Ghostscript files are in /usr/local/bin or /usr/local/share.
