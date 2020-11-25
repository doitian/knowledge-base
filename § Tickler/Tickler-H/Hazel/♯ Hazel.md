# Hazel

#macOS #automation #softwareUsage

## Configuration

If you need to restore your Hazel settings and rules from a backup, use this procedure:

-   Quit System Preferences.
-   Launch Activity Monitor. While in Activity Monitor, do the following:
    -   Find HazelHelper. Quit HazelHelper.
    -   Find cfprefsd. Quit any occurrences that you can (some may be for other accounts and you can’t kill them).
-   Restore the following:
    -   In your Library/Application Support folder, the Hazel folder
    -   In your Library/Preferences folder, the files starting with com.noodlesoft.
-   Reboot.
