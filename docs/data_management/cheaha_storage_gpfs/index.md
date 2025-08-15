# Cheaha Storage (GPFS)

The Cheaha storage, also known as GPFS (General Parallel File System), is a distributed file system designed for managing dynamic data and serves as a storage solution on Cheaha. We provide the following Cheaha storage solutions.

- [User Data and Home Directories](./individual_directories.md): These directories are automatically provided to every Cheaha user upon account creation. They are intended for storing important program files, scripts, small input datasets, critical results, and files you use often.
- [Project Directories](./project_directories.md): A shared storage space for files related to a research team. Accessible from any login or compute node by group members. Use it to store scripts, datasets, results, and other files that need to be shared among collaborators. Project directories can be accessed via the path `/data/project/<alloaction-name>`.
- [Global Scratch](./global_scratch.md): A global scratch is a scratch space that is common to all compute nodes, and are available through `/scratch/<BlazerID>` path or `$USER_SCRATCH` environment variable on Cheaha.
- [Local Scratch](./local_scratch.md): A local scratch is a temporary storage specific to the compute node your job runs on, and it can be accessed through `/scratch/local/$SLURM_JOB_ID` or via the `$LOCAL_SCRATCH` environment variable on Cheaha.
- [Temporary Files (`/tmp/` Directory)](./temporary_files.md): This directory is provided for short-term file storage, and is local to each node, and it can be accessed via `/tmp` or `$TMPDIR` environment variable on Cheaha.
