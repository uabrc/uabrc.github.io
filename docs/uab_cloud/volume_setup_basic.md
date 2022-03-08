# Basic Volume Setup

These instructions are intended for users who want to setup a persistent volume for use across instances. To follow these instructions you'll need to have already setup an [Instance](instance_setup_basic.md).

## Creating a Volume

1. Click the "Volumes" fold-out in the left-hand navigation pane - the fold-out should open.

    ![!OpenStack Overview page. The Volumes fold-out is opened. The Volumes link in the fold-out is highlighted. ><](./images/volumes_000.png)

    

2. Click "Volumes" within the fold-out to open the "Volumes" table page.

    ![!Volumes page. The Volumes table is empty. ><](./images/volumes_001.png)

3. Click "+ Create Volume" to open a dialog box.

4. Fill out the dialog box.

    1. Enter a "Volume Name".
    2. Enter a "Description".
    3. Select "No source, empty volume" in the "Volume Source" drop-down box to create an empty volume.
    4. Select "\_\_DEFAULT\_\_" in the "Type" drop down box.
    5. Select a size in GB appropriate for your needs.
    6. Select "nova" in the "Availability Zone" drop down box.
    7. Select "No group" in the "Group" drop down box.

    ![!Create Volume dialog. The dialog is filled out. The volume name is set to my_volume. ><](./images/volumes_002.png)

    

5. Click "Create Volume"

    1. Returns to the "Volumes" table page.
    2. There will be a new entry in the "Volumes" table.

        ![!Volumes page. The table has one entry labeled my_volume. ><](./images/volumes_003.png)

## Attaching a Volume to a Running Instance

To attach a volume you must have already created at least one using the OpenStack interface. More information can be found in \[link\]

1. Open the instances table by clicking "Compute" in the left-hand navigation pane and clicking "Instances".

2. In the "Actions" column entry, click the drop down triangle button and select "Attach Volume".

    ![!OpenStack Instances Page. The table has one entry labeled my_instance. The drop-down box under the Actions column is open revealing many options. The Attach Volume option is highlighted. ><](./images/instances_018.png)

    

3. A dialog box will open.

4. Select a volume in the "Volume ID" drop down box.

    ![!Attach Volume dialog box. The Volume ID is set to my_volume. ><](./images/instances_019.png)

    

5. Click "Attach Volume".

Now the volume should be attached to the instance. From here you may format the volume and mount it.

## Formatting a Volume

To format a volume, you must have created a volume and attached it to an instance capable of formatting it correctly. These instructions assume a Linux operating system.

1. Click "Compute" in the left-hand navigation pane, then open the "Instances" menu. Click the name of any instance you wish to use to format the volume. Then click "Overview".

2. Scroll down to "Volumes Attached" and make note of the `<mount>` part of `<volume-name> on <mount>` for your attached volume as it will be used in later steps.

    ![!my_instance overview page. The page has been scrolled to the bottom. The mouse is pointing to a label under the Volumes Attached heading. The mouse is pointing to the Attached To label reading my_volume on /dev/vdb. ><](./images/persistent_volumes_000.png)

    

3. SSH into the instance from your local machine or from Cheaha.

4. Verify the volume is attached by using `sudo fdisk -l | egrep "<mount>""`

    ![!MINGW64 terminal on Windows. The last three lines show the sudo fdisk -l command entered. The result includes the disk label /dev/vdb. ><](./images/persistent_volumes_001.png)

5. Format the volume using `sudo fdisk "<mount>"`

    1. You will be in the `fdisk` utility.
    2. Enter `n` to create a new partition.
    3. Enter `p` to make it the primary partition.
    4. Enter numeral `1` to make it the first partition.
    5. Press enter to accept the default first sector.
    6. Press enter to accept the default last sector.
    7. Enter `t` to change partition type.
    8. Enter numerals `83` to change to Linux partition type.
    9. Enter `p` to display the partition setup. Note that the partition will be labeled `<mount>1`. This literally whatever `<mount>` was from earlier followed by the numeral `1`. Further steps will refer to this as `<pmount>`
    10. Enter `w` to execute the setup prepared in the previous substeps.

    ![!MINGW64 terminal. The sudo fdisk /dev/vdb command has been entered. Also shown are the various prompts guiding through the process of formatting the disk. The final command was the literal character w, which executed the previously entered commands. ><](./images/persistent_volumes_002.png)

6. Verify the volume is not mounted using `sudo mount | egrep "<mount>"`. If there is no output, then move to the next step. If there is some output then use `sudo umount -l "<mount>"` to unmount the volume and verify again.

    ![!MINGW64 terminal. The volume has been verified to be not mounted using the sudo mount | egrep /dev/vdb command. ><](./images/persistent_volumes_003.png)

7. Create the filesystem using `sudo mkfs.ext4 "<pmount>"`. Ensure that the output looks like the following:

    ```bash
    ubuntu@my-instance:~$ sudo mkfs.ext4 /dev/vdb1
    mke2fs 1.45.5 (07-Jan-2020)
    Discarding device blocks: done
    Creating filesystem with 26214144 4k blocks and 6553600 inodes
    Filesystem UUID: 335704a9-2435-440a-aeea-8ae29438ac64
    Superblock backups stored on blocks:
          32768, 98304, 163840, 229376, 294912, 819200, 884736, 1605632, 654208,
          4096000, 7962624, 11239424, 20480000, 23887872
    
    Allocating group tables: done
    Writing inode tables: done
    Creating journal (131072 blocks): done
    Writing superblocks and filesystem accounting information: done
    ```

    ![!MINGW64 terminal. The sudo mkfs.ext4 /dev/vdb1 command has been used to create a partition labeled /dev/vdb1 on mount /dev/vdb. ><](./images/persistent_volumes_004.png)

The volume is now formatted and ready for mounting within an attached instance OS. You will need to make note of `<pmount>` for when you are ready to mount the volume to an instance.

## Mounting a Volume in an Instance

Mounting a volume needs to be done once per instance it will be attached to. It is assumed you've already created and formatted a volume and attached it to some instance. You'll need the `<pmount>` label from when you formatted the volume.

1. SSH into the instance from your local machine or from Cheaha.

2. Obtain the uuid of the volume using `sudo blkid | egrep "<pmount>"`. This will be referred to as `<uuid>` in future steps.

    ![!MINGW64 terminal on Windows. The sudo blkid | egrep "vdb1" command has been used to find the partition UUID. ><](./images/persistent_volumes_005.png)

3. Create a directory to mount the volume as. A good choice is `sudo mkdir /mnt/<volume-name>` where `<volume-name>` is something meaningful for you or your project. This directory will be referred to as `<directory>` in future steps.

4. Mount the volume to the directory using `sudo mount -U <uuid> <directory>`.

5. Verify the volume is mounted using `df -h | egrep <pmount>`

    <!-- markdownlint-disable-next-line MD033 -->
    ![!MINGW64 terminal. The command mkdir /mnt/my-volume has been used to create a mount point. The command sudo mount -U <UUID> /mnt/my-volume has been used to mount the volume to the mount point. The command df -h | egrep "vdb1" has been used to verify mounting. ><](./images/persistent_volumes_006.png)

6. Edit the `fstab` file to make mounting persistent across instance reboots.

    1. Edit the file using `sudo nano /etc/fstab`.
    2. Add the following line to the file:

    ``` bash
    /dev/disk/by-uuid/<uuid> <directory> auto defaults,nofail 0 3
    ```

    ![!MINGW64 terminal. The nano editor is open and the file /etc/fstab is being edited with sudo privileges to allow saving. The suggested line has been added to the file. ><](./images/persistent_volumes_007.png)

7. Verify _fstab_ was modified correctly by soft rebooting the instance and verifying the mount again using `df -h | egrep "<pmount>"`.

    ![!MINGW64 terminal. The instance has been rebooted prior to this. The command df -h | egrep "vdb1" has been used to verify the partition was mounted on restart. ><](./images/persistent_volumes_008.png)

8. Set access control using the following commands:

    ``` bash
    sudo apt install acl # or yum install, etc., if not already installed
    sudo setfacl -R -m u:<username>:rwx <directory>
    ```

    ![!MINGW64 terminal. The acl package has been installed using the command sudo apt install acl. The access controls have been set on the mount point /mnt/my-volume using the sudo setfacl command. ><](./images/persistent_volumes_009.png)

9. Verify the access controls were modified correctly by creating a test file and then listing files in `<directory>` to ensure the file was created. The following commands will achieve this:

    ``` bash
    cd <directory>
    touch testfile
    ls
    ```

    ![!MINGW64 terminal. Access control settings have been verified by creating an empty file in the mount point /mnt/my-volume and listing files. ><](./images/persistent_volumes_010.png)

The volume is now mounted to your instance and ready for use and re-use across sessions and reboots.
