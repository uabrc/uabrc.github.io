# RClone

RClone is a powerful command line tool for transferring and synchronizing files over the internet between various machines, servers and cloud storage services. It is highly recommended for small to moderate amounts of data. For very large amounts of data consider using [Globus](globus.md) for increased robustness against failure.

RClone requires a modest amount of setup time on local machines, but once setup can be used fairly easily. Most file manipulation commands on Linux can be found in the RClone commands, but may have slightly different names, e.g. `cp` is `rclone copy`.

## Installing

### Cheaha

On Cheaha, RClone is already installed as a [Module](../../cheaha/lmod.md).

### cloud.rc and Linux

See [Installing Software](../../uab_cloud/installing_software.md) for general good practice on installing software, then use the following command.

```bash
curl https://rclone.org/install.sh | sudo bash
```

Open a new terminal and enter `rclone` to verify installation.

### Windows

It is highly recommended to install `rclone` in Windows Subsystem for Linux (WSL).

To instead install natively on Windows, you will need to use the following instructions.

1. Download the appropriate version from the [downloads](https://rclone.org/downloads/) page.
2. Extract `rclone.exe` into a memorable folder on your system. Do not put it into `Program Files`.
3. In the Start Menu type `env` and look for the application "Edit the system Environment Variables" to open the System Properties dialog.
4. Click the "Environment Variables..." button.
5. Under "User variables for $USER" find the variable "Path".
6. Click "Path" to select it.
7. Click the "Edit..." button to open a new dialog.
8. Click the "New" button.
9. Type in the folder path to `rclone.exe` as `C:/path/to/rclone.exe`, modified appropriately.
10. Click the "OK" button to confirm and close the dialog box.
11. Click the "OK" button to confirm and close the Environment Variables dialog box.
12. Click the "OK" button to confirm and close the System Properties dialog box.
13. Verify the installation by typing "cmd" in the Start Menu and opening the Command Prompt application.
14. Type `rclone` and you should see the `rclone` help text.

### MacOS

Follow the [online instructions](https://rclone.org/install/#macos-installation-with-brew) for installing with `brew`.

## Setting up Remotes

RClone is capable of interfacing with many remote cloud services, as well as using `sftp` for connecting two personal computers or servers. We will only cover those relevant to UAB use, so please see their [documentation](https://rclone.org/docs/) for more information.

### Setting up `sftp` and `scp` Remotes

RClone connects two personal computers or servers using `sftp` which is built on `ssh`, so a lot of these instructions mirror what would be done with an `ssh` configuration.

1. [Generate a Key Pair](../../uab_cloud/cloud_remote_access.md#generating-key-pairs) for use with the remote machine.
2. At the terminal enter `rclone config`.
3. Follow the prompts to choose `sftp`.
4. Enter the following values as they come up, using defaults for other values.
    - `name>` Name of the remote for future reference and configuration
    - `host>` Remote IP address or `cheaha.rc.uab.edu` for Cheaha
    - `user>` The user you will log into on the remote machine
    - `key_file>` The absolute path to the private key file on the local machine, something like `~/.ssh/private_key_ed25519`
    - `key_file_pass>` The passphrase used to secure the private key file (optional, but highly recommended)
5. Verify by using `rclone lsd <name>`.

The official docuemntation for `rclone sftp` is [here](https://rclone.org/sftp/).

### Setting up a UAB Box Remote

RClone also connects to many cloud services. At UAB a vetted service called [Box](https://www.uab.edu/it/home/tech-solutions/file-storage/box) is used.

1. At the terminal enter `rclone config`. This will be terminal (1).
2. Follow the prompts to choose `Box`.
3. Enter a memorable name for future reference and configuration when prompted `name>`.
4. Press enter to leave all of the remaining prompts blank until "Use auto config?", then type "no" and press enter. This will be terminal (4)
5. On a machine with a browser, such as your personal computer, open a terminal and enter `rclone authorize "box"`.
6. When the browser window opens, authenticate to Box using UAB credentials as usual. You should be asked to grant permission to the RClone software. Allow these permissions if you want the software to work with Box.
7. Terminal (4) will print a secret token.
8. Copy and paste the token from the terminal (4) to the terminal (1).
9. Follow the remaining prompts.
10. Verify by using `rclone lsd <name>:` in terminal (1).

The official documentation for `rclone box` is [here](https://rclone.org/box/) and the official documentation for this style of Remote Setup is [here](https://rclone.org/remote_setup/).

## Usage

RClone is a powerful tool with many commands available. We will only cover a small subset of the available commands, as most are beyond typical usage, so please see their [documentation](https://rclone.org/docs/) for more information.

All commands have access to the [global flags](https://rclone.org/flags/). An important global flag is `--dry-run` to show what will happen without actually executing the command, which can be helpful to prevent costly mistakes.

The various remotes each have their own individual page with their own specific flags, and are linked in the relevant [Setting up Remotes](#setting-up-remotes) section above.

<!-- markdownlint-disable MD046 -->
!!! important

    Remote paths are always prefixed by the name of the remote like `cheaha:/path/to/files`. The color character `:` is required for all remote paths. Local paths have no prefix like `/path/to/local/files`. RClone can thus be used between any two machines that are configured where `rclone` is being used, including from the local machine to itself. In the following instructions, replace `<remote:>` by the appropriate remote name from configuration. To access local files, leave `<remote:>` off entirely.
<!-- markdownlint-enable MD046 -->

<!-- markdownlint-disable MD046 -->
!!! important

    Remember to use quotes `"` around paths with spaces like `"path\to\a folder with spaces"`
<!-- markdownlint-enable MD046 -->

### Creating a Directory

To create a directory use `rclone mkdir <remote:><path>`.

Example: `rclone mkdir box:manuscript`.

### Listing Files and Directories

To list files on a machine use `rclone ls <remote:><path>`.

Example `rclone ls box:`.

To list directories on a machine use `rclone lsd <remote:><path>`.

Example: `rclone lsd box:` should show `manuscript`.

### Copying Files

To copy files without changing their name, or to recursively copy directory content, use `rclone copy <source:><path> <destination:><path>`. Note that the directory contents are copied, so when copying a directory, be sure that directory exists on the remote and that you are copying into it.

Example: `rclone copy "C:\users\Name\My Documents" box:manuscript`

To copy a single file and change its name, use `rclone copyto <source:><path/oldname> <destination:><path/newname>`.

Example `rclone copyto "C:\users\Name\My Documents\manuscript.docx" box:manuscript\newest.docx`

### Syncing Between Two Devices

To make a destination directory's contents identical to a source directory, use `rclone sync <source:><path> <destination:><path>`

Example: `rclone sync cheaha:"C:\users\Name\My Documents" box:manuscript`.
