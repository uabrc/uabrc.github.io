# Access GPFS Snapshots on Cheaha

How do you recover data you deleted in error on the cluster? With our new GPFS filesystem, you can recover these files with GPFS Snapshots. GPFS snapshots on Cheaha allow you to recover deleted or modified files without needing to contact support. These snapshots function similarly to tools like Time Machine on macOS or Timeshift on Linux, but are accessed directly through the filesystem.

## Overview

Snapshots are read-only, point-in-time copies of your project directory that are created automatically.

- Snapshots are created daily.
- Retains approximately 14 days of history.
- Snapshots for files from your `/home/$USER` are stored in the `/home/$USER/.snapshots` directory or in `/gpfs/.snapshots/<snapshots_id>/user/home/<username>`.
- Snapshots for files stored in `/data/user/$USER` are located in a hidden directory within the `/gpfs/.snapshots` directory.
- Project directory snapshots are located at `/data/project/<Project-Directory-Name>/.snapshots` within your project directory.
- Files are restored by copying them out of the snapshot. Use the `cp` command.
- Snapshots are a self-service recovery mechanism.

<!-- markdownlint-disable MD046 -->
!!! note

    Snapshots provide short-term recovery only. For long-term backups, consider using [Long Term Storage (LTS)](../lts/index.md).
<!-- markdownlint-enable MD046 -->

## Accessing Snapshots via the Terminal

### Open a Terminal

Access a terminal using one of the following methods:

- Launch an HPC Desktop session through [Open OnDemand](../../../cheaha/open_ondemand/hpc_desktop.md#accessing-the-terminal).
- [Connect via SSH to Cheaha](../../../cheaha/getting_started.md#accessing-cheaha).

### Navigating to Your Project, Home or User Snapshot Directory

Snapshots are available for your home and user directory files (i.e.`/home/$USER` and `/data/user/$USER`), and project directory files (`/data/project`). These files are located in different locations. For all locations, snapshots are stored in a hidden directory named `.snapshots`. For your project and user files, you can list hidden files and directories by running the `ls -a` command within your respective project or user directories. However, if you try the same `ls -a` command within your home directory (`/home/$USER`), the `.snapshots` directory will not be visible. You can directly list it by using the absolute path to the `.snapshots` directory. This approach works with all locations.

For a project directory

```bash
ls -a /data/project/my_lab/.snapshots
```

For your home directory

```bash
ls -a /home/$USER/.snapshots
```

For your user directory, run.

```bash
ls -a /gpfs/.snapshots/<snapshots_id>/user/$USER
```

This should list the contents of your `.snapshots` directory, including timestamped snapshot directories. To go into the snapshots located in your project directory, home directory or user directory, run the corresponding `cd` command. Remember to replace "my_lab" with the name of your project directory, and "snapshots_id" with the actual timestamped directory.

```bash
cd /data/project/my_lab/.snapshots/snapshots_id
```

To access your home directory run the command

```bash
cd /home/$USER/.snapshots/snapshots_id
```

To access your user directory run the command

```bash
cd /gpfs/.snapshots/snapshots_id/user/$USER
```

<!-- markdownlint-disable MD046 -->
!!! note

    Files in your `/home/$USER` directory, are saved in the snapshot directory located in `/home/$USER/.snapshots` for you to retrieve. They are also available here `/gpfs/.snapshots/snapshots_id/user/home/$USER`. For snapshot files stored for your /data/user/ files, you will need to access them by going through the snapshots_id before accessing your files (i.e. `/gpfs/.snapshots/snapshots_id/user/$USER/`), for the other locations this is not the case.
<!-- markdownlint-enable MD046 -->

### List Available Snapshots

Use the `ls` command within the `.snapshots` directory to view available snapshots. Each directory is timestamped to show exactly when the files were saved.

```bash
ls
```

![!Image of a Terminal showing commands to navigate a directory and files listed in the `.snapshots` directory](../images/files-listed-snapshots-directory.png)

Snapshots follow a timestamp based naming convention. `snapshots_id = @GMT-YYYY.MM.DD-HH.MM.SS`. For example `@GMT-2026.04.23-07.35.14`

You will use the `snapshots_id` value when navigating to a snapshot directory or restoring files.

<!-- markdownlint-disable MD046 -->
!!! tip

    Choose a snapshot created before the file was deleted or modified.
<!-- markdownlint-enable MD046 -->

### Enter a Snapshot Directory

Navigate into a snapshot directory, using the `snapshots_id` listed in the `.snapshots` directory.

```bash
cd /path/to/files/in/snapshots/directory/snapshots_id
```

For instance, if you need to access files in your project directory (for example "my_lab") from April 23, 2026, those files can be accessed by running the command. Make sure the `snapshots_id` you enter falls within the 14 day period, and is listed as one of the files in the snapshot directory.

```bash
cd /data/project/my_lab/.snapshots/@GMT-2026.04.23-07.35.14
```

To access files located in your home directory snapshot, you will run the below command (you can replace "$USER" with your BlazerID which doubles as your username).

```bash
cd /home/$USER/.snapshots/@GMT-2026.04.23-07.35.14
```

To access files located in your user directory snapshot, you will run the command.

```bash
cd /gpfs/.snapshots/@GMT-2026.04.23-07.35.14/user/$USER/
```

### Locate Your File

Browse the snapshot as if it were your normal project or user directory. So commands for file navigation like `ls` and `cd` will come in handy. You can review our [Using the Terminal](../../../cheaha/open_ondemand/hpc_desktop.md#using-the-terminal) section for additional information.

```bash
cd path/to/files/in/snapshot/directory

ls
```

Remember to replace the above path with the actual project directory, home or user directory path.

### Restore the File

To restore a file, copy it from the snapshot directory into your preferred location outside the snapshots directory with the `cp` command:

```bash
cp <source> <destination>

cp -r /data/project/.snapshots/<snapshots_id>/directoryORfilename /data/project/restoredDirectoryOrFilename
```

In the case of your home directory.

```bash
cp -r /home/$USER/.snapshots/<snapshots_id>/directoryORfilename /home/$USER/restoredDirectoryOrFilename
```

Or in the case of your user directory.

```bash
cp -r /gpfs/.snapshots/<snapshots_id>/user/$USER/directoryORfilename /data/user/$USER/restoredDirectoryOrFilename
```

<!-- markdownlint-disable MD046 -->
!!! important

    Snapshots are **read-only**. Files must be copied out to be restored, before they can be used. Your files in the snapshot directory may not reflect the actual file size until it is copied out.
<!-- markdownlint-enable MD046 -->

## Accessing Snapshots via Open OnDemand (OOD)

At this time, snapshots can only be accessed via the Terminal, trying to access the snapshots via Open OnDeman (OOD) will return an error.

![!Error message show when trying to access snapshots via OOD](../images/snapshots-error-message-ood.png)

## Common Mistakes

Avoid the following:

- Attempting to modify files inside `.snapshots` directory.
- Selecting a snapshot created **after** the file was deleted.
- Using an incorrect directory path.
- Attempting to restore Ceph-stubbed files directly.

## When to Contact Support

Contact Research Computing if:

- You receive an **"Operation not permitted"** error.
- The file is not present in any snapshot.
- You are unsure whether your data is GPFS or Ceph-resident.
- You need help restoring large or complex datasets.

For critical data that needs to be archived, consider using [Long Term Storage (LTS)](../lts/index.md), snapshots are not intended for use as an archive.

{% include "_template/base_help_section.md.j2" %}
