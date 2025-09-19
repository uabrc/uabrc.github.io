# Cheaha Storage (GPFS)

The Cheaha storage, also known as GPFS (General Parallel File System), is a distributed file system designed for managing dynamic data and serves as a storage solution on Cheaha. We provide the following Cheaha storage solutions.

- [User Data and Home Directory](./individual_directories.md):These directories are automatically created for every Cheaha user upon account setup. They are intended for storing essential program files, scripts, small input datasets, critical results, and frequently used files.
- [Project Directory](./project_directories.md): A shared storage space for files related to a research team. Accessible from any login or compute node by group members. Use it to store scripts, datasets, results, and other files that need to be shared among collaborators.
- [Network Scratch](./network_scratch.md): Also known as "Global Scratch" or "User Scratch". The network scratch space is available on all nodes at `/scratch/`. Every researcher has a separate directory `/scratch/$USER`. The Linux environment variable `$USER_SCRATCH` points to this path. Please clean up unneeded data as soon as possible. We will delete aging data to free up space.
- [Local Scratch](./local_scratch.md): A local scratch is a temporary storage specific to the compute node your job runs on, and it can be accessed through `/scratch/local/$SLURM_JOB_ID` or via the `$LOCAL_SCRATCH` environment variable on Cheaha.
- [Temporary Files (`/tmp/` Directory)](./temporary_files.md): This directory is provided for short-term file storage, and is local to each node, and it can be accessed via `/tmp` or `$TMPDIR` environment variable on Cheaha.
