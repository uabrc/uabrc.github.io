---
toc_depth: 3
---
# Basic Workflow With Individual LTS and `s3cmd`

In this tutorial, we will guide you through using `s3cmd` on the Cheaha system to effectively manage and interact with your individual LTS allocation. We will cover the installation and configuration of `s3cmd`, and demonstrate essential operations, including creating buckets, listing, copying, downloading, and deleting [buckets and objects](../index.md#terminology) in your LTS allocation. In addition, we will show you how to set and manage read and write access for other allocations to your LTS buckets and objects.

## Prerequisites

To get up to speed, you should have a basic understanding of how to use the shell/terminal. If you’re not familiar with these concepts, we recommend checking out our [learning resources on basic shell usage](../../../workflow_solutions/shell.md#shell-reference).

You will also need an individual LTS allocation created by our team. If you believe you need an allocation but do not have one, please [contact us](../../../index.md#how-to-contact-us).

## Setting Up Your Environment

### Install `s3cmd` Within Conda Environment on Cheaha

To interact with LTS (Long-Term Storage) using [S3 (Simple Storage Service)](https://aws.amazon.com/s3/), you need the `s3cmd` tool installed.[`s3cmd`](https://s3tools.org/s3cmd) is a command-line tool for managing files in cloud storage systems like S3. It's recommended to install it using `pip`, the standard package installer for Python, which allows you to install packages from the [Python Package Index (PyPI)](https://pypi.org/), within a [Conda environment](../../../workflow_solutions/using_anaconda.md#create-an-environment) on Cheaha.

Please avoid using `conda install s3cmd`, as that version will not work as expected. Instead, follow the steps below to install `s3cmd` using `pip` within your Conda environment.

First, access our interactive Open OnDemand (OOD) portal at <https://rc.uab.edu> and create a job on Cheaha using one of our interactive applications. For guidance, refer to our tutorial on [installing and setting Conda environment](../../../cheaha/tutorial/pytorch_tensorflow.md#installing-anaconda-environments-using-the-terminal).

Once your interactive apps session is launched, open the terminal as described in [step 5 of the Anaconda tutorial page](../../../cheaha/tutorial/pytorch_tensorflow.md#installing-anaconda-environments-using-the-terminal) and run the below commands.

```bash
module load Anaconda3
conda create -n s3 -c conda-forge pip
conda activate s3
pip install s3cmd
```

Once these steps are completed, verify the installation by running `pip list | grep "s3cmd"` in the terminal. If `s3cmd` is listed, as shown in the screenshot below, the package has been successfully installed.

![image](../images/pip-s3cmd.png)

### Install `s3cmd` on Your Local Systems

To install s3cmd on your local machine, please follow the instructions provided in [our s3cmd documentation for local installation](../../../data_management/lts/interfaces.md#installation-of-s3cmd-and-s5cmd-on-individual-systems-without-anaconda).

### Configuring `s3cmd` for LTS Buckets

Properly configuring `s3cmd` is important for working with LTS buckets and objects. The configuration process varies depending on whether you have a single LTS allocation or multiple allocations to manage. In this section, we will provide a step-by-step guide tailored specifically for the **Cheaha** system and a researcher with an **individual LTS allocation**.

Open a terminal using one of the interactive apps on Cheaha. Activate your conda environment created in the [Install s3cmd using within Conda Environment](./individual_lts_tutorial.md#install-s3cmd-within-conda-environment-on-cheaha) section, and then run the below command:

```bash
s3cmd --configure
```

This will prompt you to enter the access key and secret key associated with your individual LTS allocation. You will be asked for additional information, which will be displayed on the screen, as shown below. You can copy the necessary details from [an example of S3 configuration](../interfaces.md#configuring-s3cmd).

![image-s3cmd](../images/config-s3cmd.png)

Once the configuration is complete, `s3cmd` will generate a `.s3cfg` file in your home directory (`$HOME`), as shown below. To find your home directory in Cheaha and view the `.s3cfg` file, follow the instructions on our [Navigating Open OnDemand](../../../cheaha/open_ondemand/ood_layout.md#navigating-open-ondemand) page. Be sure to check the **Show Dotfiles** option in the top right corner to make hidden files visible.

![config-file](../images/s3cfg.png)

### Creating Buckets

Long Term Storage (LTS) services like Amazon S3 use a flat data organization model based on **buckets** and **objects**. Think of buckets as folders that contain individual pieces of data called objects. For more information about S3 terminology please see the [terminology section](../index.md#terminology).

Once you have complete `s3cmd` configuration, you can create new buckets in your individual LTS storage. To create a bucket use a `mb` (make bucket) command:

```bash
s3cmd mb s3://your-bucket-name
```

Please replace `your-bucket-name` with your desired name. This command creates a new bucket that you named `your-bucket-name` in your LTS storage using the currently configured `s3cmd` profile. For example, the image below shows an LTS bucket named `first-test-bucket` that was created successfully after running the command `s3cmd mb s3://first-test-bucket`.

![image-bucket](../images/create-bucket.png)

When creating a bucket, it is important to be aware of name uniqueness and naming conventions. For detailed information on bucket naming, please refer to our documentation on [valid bucket names in LTS](../lts_faq.md) and [avoiding duplicate names for buckets](../index.md#avoiding-duplicate-names-for-buckets).

If you try to create a bucket with `s3cmd mb` with the name that already exists within your namespace, the system will report success without making any changes. For example, if you run `s3cmd mb s3://existing-bucket-name` and that bucket name is already taken in your namespace, the command will complete successfully without creating a new bucket and showing an error. However, if you try to create a bucket with a name that is already used in someone else’s namespace, you will receive a `409 (BucketAlreadyExists)` error. To create a unique bucket within your namespace, first use `s3cmd ls` to list existing buckets and choose a name that is not already in use. To avoid the `409 (BucketAlreadyExists)` error and ensure your bucket name is unique, follow the [avoiding duplicate names for buckets](../index.md#avoiding-duplicate-names-for-buckets) guide. This will help you create your bucket successfully and maintain its uniqueness.

### Managing Buckets

To manage a bucket, various commands can be used. Below are some common `s3cmd` commands to interact with your LTS bucket and its objects:

- To **list all buckets** you own with your current `s3cmd` profile, use command: `s3cmd ls`.
- To **list all objects in a bucket** accessible with your current `s3cmd` profile, use command: `s3cmd ls s3://your-bucket-name`.
- To **upload a file** named `file.txt` to a bucket, use a command: `s3cmd put file.txt s3://your-bucket-name/`. For example, to upload the file `file.txt` from the `/data/user/$USER` directory on Cheaha to the bucket `your-bucket-name`, you can use the command: `s3cmd put /data/user/$USER/file.txt s3://your-bucket-name`.
- To **download an object** named `file.txt` from a bucket, use a command:`s3cmd get s3://your-bucket-name/file.txt`. For example, to download the object `file.txt` from the bucket `your-bucket-name` to the `/data/user/$USER` directory on Cheaha, you can use a command `s3cmd get s3://your-bucket-name/file.txt /data/user/$USER`.
- To **delete/remove** an object, use command: `s3cmd del s3://your-bucket-name/your-object-name`.
- To **delete/remove** a bucket, use command: `s3cmd rb s3://your-bucket-name`.

    <!-- markdownlint-disable MD046 -->
    !!! Note

        An S3 bucket cannot be deleted unless it is completely empty. If the bucket contains any objects, `s3cmd rb` will report an error, like `S3 error: 409 (BucketNotEmpty)` when you attempt to delete it. To remove all objects within the bucket, use: `s3cmd del -r s3://your-bucket-name --force`. You can then remove the bucket itself with: `s3cmd rb s3://your-bucket-name`.
    <!-- markdownlint-disable MD046 -->

    <!-- markdownlint-disable MD046 -->
    !!! danger

        Deleting objects and buckets cannot be undone. Once the delete command is entered, any data is lost permanently and cannot be restored.
    <!-- markdownlint-enable MD046 -->

You can find a variety of `s3cmd` commands at our [`s3cmd` commands page](../../lts/interfaces.md#s3cmd-commands) and on the [S3tools website](https://s3tools.org/usage). For quick reference, you can also use the `s3cmd --help` command to view available options directly in your terminal.

If you are continuing in the same session with your **conda environment already activated**, you can directly use the `s3cmd` commands. If you are starting a new session or returning at a later date, make sure to load the Anaconda module and activate your conda environment before using `s3cmd`.

### How to Grant Access to Other Allocations for Your Buckets?

Managing access to your buckets is essential for both collaboration and security. By setting up specific [bucket policies](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-policies.html), you can control who can view or modify your bucket’s contents. Follow these steps to grant access:

- Create a policy file: define a policy and save it as a `JSON` file. For guidance and details on creating and formatting policy files, refer to our [create a policy structure guide](../iam_and_policies.md#policy-structure). For example, you might create a policy file named `my_policy.json` with read permissions.
- Apply the policy: Use the command like `s3cmd setpolicy policy_file.json s3://your-bucket-name` to apply your defined read policy to your bucket. Replace `policy_file.json` with the name of your policy file and `your-bucket-name` with the name of your bucket.
- Verify the policy update: After applying the policy, you should see a `Policy updated` message if the operation was successful. You can also verify the applied policy by running: `s3cmd info s3://your-bucket-name`.

Below is a screenshot showing how to apply a policy file named `my_policy.json` to a bucket named `first-test-bucket`, and the command to view information about this bucket, including the policy file that we defined and applied.

![policy-image](../images/policy.png)

Please note that the permissions granted are determined by the settings defined in your policy file. The policy demonstrated in this example is a **read-only** policy. Below, you can find examples of the different policies, including the read and write policies, you can set and apply for your buckets and objects in your individual LTS allocation.

- **Read-only Access**

    To allow another allocation to view and copy files from your bucket without making any changes, use the [read only permission policy](../iam_and_policies.md#read-only-for-all-files).

- **Read/Write Access**

    To grant another allocation the ability to both view and modify the contents of your bucket, use the [read/write permissions policy](../iam_and_policies.md#read-write-permissions).

For detailed information on LTS bucket policies and instructions on how to apply and remove bucket policies, please refer to our [policy structure](../iam_and_policies.md#policy-structure) and [apply bucket policy](../iam_and_policies.md#applying-a-policy) guides.
