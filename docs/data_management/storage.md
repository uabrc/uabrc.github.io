# Storage

## Privacy

**Do not store sensitive information on this filesystem. It is not encrypted.** Note that your data will be stored on the cluster filesystem, and while not accessible to ordinary users, it could be accessible to the cluster administrator(s).

## No Automatic Backups

There is no automatic back up of any user data on the cluster in home, data, or scratch. At this time, all user data back up processes are defined and managed by each user and/or lab. Given that data backup demands vary widely between different users, groups, and research domains, this approach enables those who are most familiar with the data to make appropriate decisions based on their specific needs.

For example, if a group is working with a large shared data set that is a local copy of a data set maintained authoritatively at a national data bank, maintaining a local backup is unlikely to be a productive use of limited storage resources, since this data could potentially be restored from the authoritative source. If, however, you are maintaining a unique source of data of which yours is the only copy, then maintaining a backup is critical if you value that data set. It's worth noting that while this "uniqueness" criteria may not apply to the data you analyze, it may readily apply to the codes that define your analysis pipelines.

An often recommended backup policy is the 3-2-1 rule: maintain three copies of data, on two different media, with one copy off-site. [You can read more about the 3-2-1 rule here](https://www.backblaze.com/blog/the-3-2-1-backup-strategy/). In the case of your application codes, using revision control tools during
development provides an easy way to maintain a second copy, makes for a good software development process, and can help achieve reproducible research goals.

Please review the data storage options provided by UAB IT for maintaining copies of your data. In choosing among these options, you should also be aware of UAB's data classification rules and requirements for security requirements for sensitive and restricted data storage. Given the importance of backup, Research Computing continues to explore options to facilitate data backup workflows from the cluster. Please contact us if you have questions or would like to discuss specific data backup scenarios.

## Directories on Cheaha

Users are provided a high performance GPFS file system to store data, toolboxes, and other supporting files. The specific directories a user can access are described below. In these descriptions, the "$USER" variable should be replaced with the user's account name string.

### Home Directory

Each user has a personal directory found at `/home/$USER` (or `$HOME`). This is traditionally meant to store scripts and supporting files and toolboxes such as those relating to Anaconda virtual environments or R packages. The owner ($USER) of the directory can read, write/delete, and list files. No other users or groups have permissions to this directory.

A user is limited to 5 TB of data across both their home directory and their user data directory (see below).

### User Data Directory

Each user has another directory found at `/data/user/$USER` (or `$USER_DATA`) that can store datasets and results for a user's projects. The owner ($USER) of the directory can read, write/delete, and list files. No other users or groups have permissions to this directory.

A user is limited to 5 TB of data across both their home directory (see above)and their user data directory.

!!! note

<!-- markdownlint-disable-next-line -->
    The home and user data directories are mirrored across storage locations to allow for emergency backup in case some of the drives fail. This is not meant to be a long-term backup solution as any data deleted by a user is deleted on the main drive and the mirrored drive.

    The mirrored system technically allows for over 5 TB of data to be stored but data cannot be recovered in case of an emergency storage failure. For data safety, do not store over 5 TB of data across user data and home directories.

### Project Space

Shared data can be stored in a `/data/project/<project_name>` directory. The default storage size for a new project is 50TB. If you need less than 5TB or your need for shared space is short term, please request a [Sloss space](#sloss)instead. Project storage can be helpful for teams of researchers who need access to the same data.

All project spaces must be owned by a principal investigator (PI) who is an employee of UAB with a legitimate research interest. The PI takes responsibility for data in the space, as well as access control of all files and directories under the parent directory. As with all data on Cheaha, backups and archival services are not provided, and are the responsibility of the respective data owners.

The PI and all members with access to the project directory can read, write/delete, and list files within the top-level directory, and all other subdirectories by default. Other people on the system have no ability to access the project space. Access control for directories and files within the project space can be implemented via access control lists. Please see the bash commands [setfacl](https://linux.die.net/man/1/setfacl) and [getfacl](https://linux.die.net/man/1/getfacl)) for more information. Access control within the project directory are the responsibility of the project owner. However, we respect that access control lists can be tricky, so please feel free to [contact us](/docs/index.md#contact-us) for assistance.

To create a project directory, or change access to or ownership of a project directory, the PI should follow the instructions at [How Do I Request Or Change A Project Space?](../resources/support.md#how-do-i-request-or-change-a-project-space).

#### Sloss

A special location under `/data/project/sloss` to store projects that are at most 5 TB. In keeping with the name [Sloss](https://www.slossfurnaces.com/), these spaces are intended as a foundry for experimental or temporary project spaces that have potential to grow. Otherwise, they are treated like any other project space.

### Scratch

Two types of scratch space are provided for analyses currently being ran, network-mounted and local. These are spaces shared across users (though one user still cannot access another user's files without permission) and as such, data should be moved out of scratch when the analysis is finished.

!!! note

<!-- markdownlint-disable-next-line -->
    Scratch space (network and local) **is not backed up**.

#### Network Scratch

All users have access to a large, temporary, work-in-progress directory for storing data, called a scratch directory in `/data/scratch/$USER` or `$USER_SCRATCH`. Use this directory to store very large datasets for a short period of time and to run your jobs. The maximum amount of data a single user can store in network scratch is 100 TB at once.

Network scratch is available on the login node and each compute node. This storage is a GPFS high performance file system providing roughly 1 PB of network scratch storage. If using scratch, this should be your jobs' primary working directory, unless the job would benefit from local scratch (see below).

!!! warning

<!-- markdownlint-disable-next-line -->
    Research Computing expects each user to keep their scratch areas clean. **The cluster scratch areas are not to be used for archiving data.** In order to keep scratch clear and usable for everyone, files older than 28 days will be automatically deleted.

#### Local Scratch

Each compute node has a local scratch directory that is accessible via the variable `$LOCAL_SCRATCH`. If your job performs a lot of file I/O, the job should use `$LOCAL_SCRATCH` rather than `$USER_SCRATCH` to prevent bogging down the network scratch file system. It's important to recognize most jobs run on the cluster do not fall under this category. The amount of scratch space available is approximately 800GB.

The `$LOCAL_SCRATCH` is a special temporary directory and it's important to note that this directory is deleted when the job completes, so the job script has to move the results to `$USER_SCRATCH` or other location prior to the job exiting.

Note that `$LOCAL_SCRATCH` is only useful for jobs in which all processes run on the same compute node, so MPI jobs are not candidates for this solution. Use the `#SBATCH --nodes=1` slurm directive to specify that all requested cores are on the same node.

The following is an array job example that uses `$LOCAL_SCRATCH` by transferring the inputs into `$LOCAL_SCRATCH` at the beginning of the script and the result out of `$LOCAL_SCRATCH` at the end of the script.

``` bash

#!/bin/bash
#SBATCH --array=1-10
#SBATCH --share
#SBATCH --partition=express
#
# Name your job to make it easier for you to track
#
#SBATCH --job-name=R_array_job
#
# Set your error and output files
#
#SBATCH --error=R_array_job.err
#SBATCH --output=R_array_job.out
#SBATCH --ntasks=1
#SBATCH --nodes=1
#
# Tell the scheduler only need 10 minutes and the appropriate partition
#
#SBATCH --time=00:10:00
#SBATCH --mem-per-cpu=256
#
# Set your email address and request notification when you job is complete or if it fails
#
#SBATCH --mail-type=FAIL
#SBATCH --mail-user=YOUR_EMAIL_ADDRESS

module load R/3.2.0-goolf-1.7.20

echo "TMPDIR: $LOCAL_SCRATCH"

cd $LOCAL_SCRATCH
# Create a working directory under the special scheduler local scratch directory
# using the array job's taskID
mdkir $SLURM_ARRAY_TASK_ID
cd $SLURM_ARRAY_TASK_ID

# Next copy the input data to the local scratch
echo "Copying input data from network scratch to $LOCAL_SCRATCH/$SLURM_ARRAY_TASK_ID - $(date)
# The input data in this case has a numerical file extension that
# matches $SLURM_ARRAY_TASK_ID
cp -a $USER_SCRATCH/GeneData/INP*.$SLURM_ARRAY_TASK_ID ./
echo "copied input data from network scratch to $LOCAL_SCRATCH/$SLURM_ARRAY_TASK_ID - $(date)

someapp -S 1 -D 10 -i INP*.$SLURM_ARRAY_TASK_ID -o geneapp.out.$SLURM_ARRAY_TASK_ID

# Lastly copy the results back to network scratch
echo "Copying results from local $LOCAL_SCRATCH/$SLURM_ARRAY_TASK_ID to network - $(date)
cp -a geneapp.out.$SLURM_ARRAY_TASK_ID $USER_SCRATCH/GeneData/
echo "Copied results from local $LOCAL_SCRATCH/$SLURM_ARRAY_TASK_ID to
network - $(date)

```

## Directory Permissions

Default file permissions are described for each directory above.
Additional background on Linux file system permissions can be found
here:

- <https://its.unc.edu/research-computing/techdocs/how-to-use-unix-and-linux-file-permissions/>
- <https://www.rc.fas.harvard.edu/resources/documentation/linux/unix-permissions/>
- <https://hpc.nih.gov/storage/permissions.html>
