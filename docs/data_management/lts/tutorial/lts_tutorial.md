---
toc_depth: 3
---
# Basic Workflow with LST and s3cmd

This tutorial covers setting up and using S3 with LTS, including installing s3cmd, configuring your environment, creating and managing S3 buckets, and setting access permissions Cheaha.

## Setting Up Your Environment

### Install s3cmd within Anaconda Environment on Cheaha

To interact with LTS using S3, you need the `s3cmd` tool installed. It is recommended to install it using `pip` within an Anaconda environment on Cheaha. Please avoid using `conda install s3cmd`, as that version may not function correctly. Instead, follow the below steps to install `s3cmd` using `pip`:

First, access our interactive Open OnDemand (OOD) portal at https://rc.uab.edu and create an [interactive HPC Desktop session](../../../cheaha/open_ondemand/hpc_desktop.md). Once the HPC Desktop session lunched, open the terminal and run the below commands.

```bash
module load Anaconda3
conda create -n s3 
conda activate s3
pip install s3cmd
```

### Install s3cmd on Your Local Systems

To install s3cmd on your local machine, please follow the instructions provided in [our s3cmd documentation for local installation](../../../data_management/lts/interfaces.md/#installation-of-s3cmd-and-s5cmd-on-personal-system).

### Configuring s3cmd for LTS Buckets

Properly configuring s3cmd is important for working with LTS buckets. The steps vary depending on whether you have a single LTS account or multiple accounts to manage. Follow the appropriate guide below for your setup.

#### Single LTS Account (Individual Users and Researchers)

For individual users with a single LTS account, follow these steps:

Open a terminal through the HPC Desktop, activate the `s3` environment created in the [Install s3cmd using within Anaconda Environment](./lts_tutorial.md/#install-s3cmd-using-pip-within-anaconda) section, and run the below command:

```bash
s3cmd --configure
```

This will prompt you for your access key and secret access key associated with your LTS account. Enter these details carefully. You will be asked for additional information, see examples [here](../interfaces.md/#configuring-s3cmd). Once completed, `s3cmd` will create a default configuration file named `.s3cfg` in your home directory (`$HOME`).

#### Multiple LTS Account (PIs/Cores and Data managers)

If you are a Lab PI or Core and manage both a personal and a lab/core LTS account, you need separate profiles for each. Follow these steps: 

- **To create a profile for your personal LTS Account**: Run `s3cmd --configure -c $HOME/personal_profile`. Replace `personal_profile` with your preferred profile name. Enter your personal LTS access credentials when prompted. This will create a configuration file named  `personal_profile` in your home directory (`$HOME`).
- **To create a profile for your Lab/Core LTS Account**: Run the command, `s3cmd --configure -c $HOME/lab_core_profile`. Replace `lab_core_profile` with your preferred profile name. Enter your lab/core LTS access credentials when prompted. This will also create a configuration file named  `lab_core_profile` in your home directory (`$HOME`).

In both cases, you will be asked for additional information beyond your access key and secret access key. For examples and detailed guidance, see [here](../interfaces.md/#configuring-s3cmd).

### How to I switch between `s3cmd` configuration profiles?

Once you have configured the `s3cmd` following the above steps, use the `-c` option with the specific profile name to specify which account you want to use with `s3cmd` commands. For example, to list buckets in your personal account:

```bash
s3cmd -c $HOME/personal_profile ls
```

Please replace the `personal_profile` with the profile name you used during configuration. When you run this command nothing will be returned if you don't have created a bucket. To create and manage buckets in you LTS account read the section about [Creating and Managing Buckets](./lts_tutorial.md/#creating-and-managing-buckets).

## Creating and Managing Buckets

Long Term Storage (LTS) services like Amazon S3 uses a specific data organization model based on **buckets** and **objects**. Imagine folders called buckets that hold individual pieces of data called objects. Each bucket has a unique name. We have information about basic terminology on s3 storage system [here](../index.md/#terminology) and a naming guide for LTS buckets [here](../index.md/#avoiding-duplicate-names-for-buckets).

### Create a Bucket

Once you have complete `s3cmd` configuration, you can create new buckets in your LTS storage. To create a bucket use a `mb`(make bucket) command:

```bash
 s3cmd mb s3://your_bucket_name
 ```

Please replace `your_bucket_name` with your desired name. This command creates a new bucket that you named `your_bucket_name` in your LTS storage using the currently configured s3cmd profile.

### Managing Buckets

To manage buckets using `s3cmd`, you should specify the appropriate configuration file if you are using multiple profiles.

- If you manage a single LTS account and are using the default configuration file `.s3cfg`, follow these steps:

    - To **lists all buckets** accessible with your current `s3cmd` profile, use command: `s3cmd ls`
    - To **upload a file**  named `file.txt` to a bucket, use a command: `s3cmd put file.txt s3://your_bucket_name/`
    - To **download a file** a file named `file.txt` from a bucket, use a command:`s3cmd get s3://bucket-name/file.txt`
    - To **delete/remove** a bucket, use command: `s3cmd rb s3://your_bucket_name`

- If you mange multiple LTS accounts (e.g personal and Lab LTS accounts), and have multiple profiles and you are using credentials NOT saved in the `$HOME/.s3cfg` file, you need to specify which profile to use to apply the bucket management action, use the `-c` option with the path to the desired profile configuration file::
    - To **lists all buckets** accessible with your current `s3cmd` profile, use command: `s3cmd ls`
    - To **upload a file** to a bucket `s3cmd -c $HOME/profile_name put file.txt s3://your_bucket-name/`
    - To **download a file** from a bucket, use a command `s3cmd -c $HOME/profile_name get s3://bucket-name/file.txt`
    - To **delete/remove** the bucket, use command: `s3cmd  -c $HOME/profile_name rb s3://your_bucket_name`

Please replace `profile_name` with the name of the configuration file you want to use, and `your_bucket-name` with the name of the bucket you want to manage.

<!-- markdownlint-disable MD046 -->
!!! Note

    An S3 bucket cannot be deleted unless it is completely empty. If the bucket contains any objects, `s3cmd` will return an error, like `S3 error: 409 (BucketNotEmpty)` when you attempt to delete it. To remove all objects within the bucket, use: `s3cmd del -r s3://your_bucket_name`. You can then remove the bucket itself with: `s3cmd rb s3://your_bucket_name`
<!-- markdownlint-disable MD046 -->

<!-- markdownlint-disable MD046 -->
!!! danger

    Be cautious when deleting buckets, as this action is permanent and will remove all data within the bucket. Once data is deleted from LTS, it cannot be recovered.
<!-- markdownlint-enable MD046 -->

### How to Grant Access to Other Accounts for your Buckets?

Managing access to your buckets is essential for collaboration and security. By setting up specific policies, you can control who can view or modify your bucket’s contents.

- **Read-only Access**

    Do you want to give another account the ability to view your bucket’s contents without making changes? Use [read only permission policy](../policies.md/#read-only-for-all-files).

- **Read/Write Access**

    If you need to allow another account to both view and modify the contents of your bucket, apply the [read/write permissions policy.](../policies.md/#read-write-permissions).

For detailed instructions on how to apply and remove bucket policies, please refer to the [apply bucket policy guide](../policies.md#applying-a-policy).
