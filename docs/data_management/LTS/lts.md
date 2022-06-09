# Long-Term Storage

<!-- markdownlint-disable MD046 -->
!!! important

    This page is a work in progress. Please be patient as information is added or removed. Thank you.
<!-- markdownlint-enable MD046 -->

UAB Long-term storage (LTS) is an S3 object-storage platform hosted at UAB. This storage is designed to hold data that is not currently being used in analysis but should be kept for data sharing, recapitulation purposes, or reused for further analysis in the future. This documentation covers multiple methods for accessing LTS in Windows, Mac, and Linux environments.

<!-- markdownlint-disable MD046 -->
!!! important

    Currently, UAB LTS is only accessible using the campus network. If you are off campus and want to access LTS, please use the [UAB VPN](https://www.uab.edu/it/home/tech-solutions/network/vpn). If you are accessing LTS through Cheaha, you do not need to use the VPN even at home.

<!-- markdownlint-enable MD046 -->
## Terminology

When talking about S3 storage, some terms are different compared to a normal filesystem. This section is here to briefly explain some differences in case you go to other documentation and see these terms instead.

In S3, there are no such things as folders and files, just objects. Everything is an object, and there is no standard filesystem where things are physically stored in a heirarchical manner. However, there are certain things that can make it look that way such as prefixes. Prefixes are used in place of a file path to an object, and so can be used to represent a path to an object.

This documentation will use the standard file and path terms since that's more easily understood by most users. Just be aware that documentation such as [AWS CLI](https://awscli.amazonaws.com/v2/documentation/api/latest/index.html) will use terms prefix, object, and others that are not standard in a typical filesystem.

## Requesting an Account

UAB researchers do not have automatic access to LTS, and currently, single sign on is not enabled. To request access to LTS, please send an email to <support@listserv.uab.edu>. You will be then be given an Access Key and a Secret Access Key, both of which will be used later on. Keep track of both of these keys and do not share them with anyone else, these are your login credentials for LTS.

## Windows/Mac

To access LTS from Windows and Mac, we suggest using the [Cyberduck](https://cyberduck.io/download/) GUI which is free to download.

Once you have it installed and open, Cyberduck will look like this:

![!Cyberduck basic interface ><](images/cyberduck.png)

### Creating a Connection

First, download the [UAB CyberDuck Connection Profile](UAB S3 Object Storage.cyberduckprofile). After it's downloaded, double click the file to open it in Cyberduck. It will open the following connection creation window:

![!Cyberduck UAB Connection Creation ><](images/cyberduck-open-connection.png)

Input your Access Key and Secret Access Key sent to you by Research Computing after account creation in their appropriate fields. Once you've entered these keys you can close the connection creation window. This connection with the keys you entered is now saved as a bookmark for easy access in the future. Double click the created bookmark to open the connection to LTS.

### Creating a Bucket

Sets of storage objects are stored in what are called buckets. Buckets are sets of file systems for storing data. You can create different buckets for various purposes, such as separating buckets by dataset or project, or having a single bucket for all data you are moving off of Cheaha project storage.

In order to create a bucket, click `File > New Folder...` and then name the bucket you would like to create. Once the bucket is created, it will appear in the File window. An example could look like:

![!Example bucket creation ><](images/cyberduck-create-bucket.png)

The bucket will have the symbol of a hard disk with an Amazon A brand on it. This is the root of the file system for that bucket. You can then double click into it to open that file system.

<!-- markdownlint-disable MD046 -->
!!! important

    Bucket names are shared across all LTS. This means you cannot create a bucket with a name that has already been created by someone else, even if that bucket is not shared with you. When creating bucket names, make them specific and/or unique. For example, davislab for storing data for the entire Davis lab or the name of a specific dataset that is being stored. Do not make names like trial or my-storage.
<!-- markdownlint-enable MD046 -->

### Uploading and Downloading Data

Once you're inside the bucket, files can be uploaded easily through dragging and dropping from your local machine into the GUI. You can also use the `Upload` button in the toolbar to open a file browser and choose what to upload.

Downloading files from the bucket can be done by first selecting the file(s)/folder(s) to download and then clicking the `Actions` button in the toolbar. In that dropdown will be a `Download` option. You can also get to this dropdown through the `File` menu or by right-clicking.

<!-- markdownlint-disable MD046-->
!!! note

    By default, all buckets and files you upload are only available to you.Currently, there is not a known method to add permissions for individual researchers in the Cyberduck interface. If you need to add access to a bucket or set of files within a bucket, please look in the Linux guide below. If you do not have access to a personal Linux machine, Cheaha is available to use for this purpose.
<!-- markdownlint-enable MD046-->

### Alternative Interfaces

In addition to Cyberduck, there are other GUI based programs for interfacing with UAB LTS. [S3 Browser](https://s3browser.com/) is an easy-to-use program for uploading and downloading files. However more sophisticated tools, such as setting file permissions, are hidden behind a paywall. This tool is also only available on Windows platforms. researchers can investigate this tool if desired, however research computing will not provide direct support for this program.

## Linux/Command Line

Linux has very few workable GUIs capable of accessing S3 storage for free available, and so almost all tools for transferring from Cheaha to LTS will be command line interfaces (CLI). The positives for this are that CLIs offer a much broader range of function available to researchers for managing their LTS buckets.

There are a few different CLIs available to researchers on Cheaha to use. Current available CLIs on Cheaha are [rclone](https://rclone.org/), [s3cmd](https://github.com/s3tools/s3cmd), and the [AWS CLI](https://aws.amazon.com/cli/). This documentation will show how to perform each function using all three tools where possible and will give a comparison chart contrasting what each tool is useful for.

Both of these are available as modules under the `rclone` and `awscli` module names.

<!-- markdownlint-disable MD046 -->
!!! note

    Of note, all of these tools are available for Windows and Mac as well if you are comfortable using command line interfaces on those platforms. There are installation instructions for both of these tools on their respective websites.
<!-- markdownlint-enable MD046 -->

### Configuration

In order to access LTS through the command line no matter which CLI you use, you will need to perform some configuration. This will set up the remote connection from your local machine (or you Cheaha profile) to LTS. If you choose to use multiple CLIs, you will need to perform configuration for each one separately.

#### rclone

The instructions for setting up a remote connection with rclone can be found in [our main rclone documentation](../transfer/rclone.md#setting-up-an-s3-lts-remote). In the following examples, `uablts` is used as the name of the remote connection.

#### s3cmd

s3cmd can be easily installed via an [Anaconda environment](../../workflow_solutions/using_anaconda.md). Create the environment, activate it, then install using:

``` bash
pip install s3cmd
```

<!-- markdownlint-disable MD046 -->
!!! note

    Depending on how Anaconda chooses to install the package, the actual s3cmd script may be in your $HOME/.local/bin folder. This folder can be added to your path using `PATH=$PATH:$HOME/.local/bin`, and you will have access to the s3cmd script after that.
<!-- markdownlint-enable MD046 -->

Once you have s3cmd downloaded, you can start the configuration process like so:

``` bash
s3cmd --configure [-c $HOME/profile_name]
```

You can run the configuration either with or without the `[-c]` option. If you use it, a file named `profile_name` will be created in your home directory with your login credentials and other information. If you omit the `-c` option, a file called `$HOME/.s3cfg` will be created by default. This can be helpful if you have multiple S3 profiles you are using. If you use UAB LTS as your only S3 storage platform, it's suggested to omit the `-c` option.

<!-- markdownlint-disable MD046 -->
!!! note

    After configuration, the `s3cmd` command will default to using the `.s3cfg` file for credentials if it exists. If you create a separate named profile file, you will need to add that to the `s3cmd` call each time you run it.
<!-- markdownlint-enable MD046 -->

During configuration, you will be asked to enter some information. You can follow the example below, inputting your user-specific information where required. Lines requiring user input are highlighted.

``` text hl_lines="2 3 4 7 10 13 14 17 20 34 41"
Access key and Secret key are your identifiers for Amazon S3. Leave them empty for using the env variables.
Access Key: <access key>
Secret Key: <secret key>
Default Region [US]: <leave blank>

Use "s3.amazonaws.com" for S3 Endpoint and not modify it to the target Amazon S3.
S3 Endpoint [s3.amazonaws.com]: s3.lts.rc.uab.edu

Use "%(bucket)s.s3.amazonaws.com" to the target Amazon S3. "%(bucket)s" and "%(location)s" vars can be used if the target S3 system supports dns based buckets.
DNS-style bucket+hostname:port template for accessing a bucket [%(bucket)s.s3.amazonaws.com]: %(bucket).s3.lts.rc.uab.edu

Encryption password is used to protect your files from reading by unauthorized persons while in transfer to S3
Encryption password: <leave blank>
Path to GPG program [/usr/bin/gpg]: $HOME/bin/gpg

When using secure HTTPS protocol all communication with Amazon S3 servers is protected from 3rd party eavesdropping. This method is slower than plain HTTP, and can only be proxied with Python 2.7 or newer
Use HTTPS protocol [Yes]: <leave blank>

On some networks all internet access must go through a HTTP proxy. Try setting it here if you can't connect to S3 directly
HTTP Proxy server name: <leave blank>

New settings:
  Access Key: <access key>
  Secret Key: <secret key>
  Default Region: US
  S3 Endpoint: s3.lts.rc.uab.edu
  DNS-style bucket+hostname:port template for accessing a bucket: %(bucket).s3.lts.rc.uab.edu
  Encryption password:
  Path to GPG program: $HOME/bin/gpg
  Use HTTPS protocol: True
  HTTP Proxy server name:
  HTTP Proxy server port: 0

Test access with supplied credentials? [Y/n] Y
Please wait, attempting to list all buckets...
Success. Your access key and secret key worked fine :-)

Now verifying that encryption works...
Not configured. Never mind.

Save settings? [y/N] y
```

If your test access succeeded, you are now ready to use `s3cmd`.

#### AWS CLI

Setting up a remote connection using AWS CLI is fairly straightforward. After loading the `awscli` module, run `aws configure` in the terminal.

It will ask you enter four pieces of information, fill them out as so:

``` text
AWS Access Key [none]: <access key>
AWS Secret Access Key [none]: <secret key>
Default region name [none]: <Press Enter>
Default output format [none]: json
```

Your access key and secret key should have been given to you by research computing when you requested your account. Copy-paste these into the terminal when requested.

<!-- markdownlint-disable MD046 -->
!!! important

    AWS CLI assumes you are using the AWS service for S3 storage. In order to access UAB LTS, for all AWS CLI commands, you will need to add the `--endpoint-url https://s3.lts.rc.uab.edu` option to the `aws` function call.
<!-- markdownlint-enable MD046 -->

### General Command Structure

**RClone**:

``` bash
rclone <subcommand> [options] <remote>:<bucket>
```

<!-- markdownlint-disable MD046 -->
!!! important

    For all commands, replace everything in `<>` with the necessary values. Do not include the `<>` symbols in your command.
<!-- markdownlint-enable MD046 -->

To see a list of all subcommands available to rclone, you can use `rclone --help`. You can also use the `--help` option with any subcommand to see a detailed explanation of what it does plus any options you may want or need to set when calling it.

**s3cmd**:

``` bash
s3cmd [-c profile_file] <command> [options] [-n --dry-run]
```

As noted previously, the `[-c profile_file]` is only required if you are NOT using credentials saved in the `$HOME/.s3cfg` file. Otherwise, you can leave it out.

To see a list of commands available, use `s3cmd --help`. Additionally, if you want to test an action without actually running it (i.e. it prints all actions that would be performed), you can add the `-n` or `--dry-run` option.

**AWS CLI**:

``` bash
aws <command> <subcommand> [options]
```

The `<command>` for most commonly used functions will either be `s3` or `s3api`. You can use the `help` option to view available commands, subcommands, and options for AWS.

Additionally, when running basically any AWS CLI command, you can include the `--dryrun` option to see the exact actions that will be performed without actually performing them. This is useful for things like deleting files and folders to make sure you are not performing an unwanted action.

<!-- markdownlint-disable MD046 -->
!!! important

    If you are wanting to perform actions on a specific directory in S3, it is imperative to add the `/` at the end of the directory name. For more information on this, see [our FAQ](../../help/faq.md#why-do-i-need-to-add-the-trailing--to-the-end-of-path-names-in-my-s3-commands)
<!-- markdownlint-enable MD046 -->

### Make a Bucket

Buckets are essentially the root folder of a filesystem where you are storing your data. You will need to create a bucket before being able to copy data to LTS.

<!-- markdownlint-disable MD046 -->
!!! important

    Bucket names are shared across all LTS. This means you cannot create a bucket with a name that has already been created by someone else, even if that bucket is not shared with you. When creating bucket names, make them specific and/or unique. For example, davislab for storing data for the entire Davis lab or the name of a specific dataset that is being stored. Do not make names like trial or my-storage.
<!-- markdownlint-enable MD046 -->

**RClone**:

``` bash
rclone mkdir uablts:<bucket>
```

**s3cmd**:

``` bash
s3cmd mb s3://<bucket>
```

**AWS CLI**:

``` bash
aws s3api create-bucket --bucket <bucket> --endpoint-url https://s3.lts.rc.uab.edu
```

### Listing Buckets and Contents

**RClone**:

To list all buckets you have available, use the `lsd` subcommand with only the remote specified:

``` bash
rclone lsd uablts:
```

To list all contents inside a bucket, use the `ls` subcommand with the remote and bucket specified. You can also be specific about the path to the directory you want to list.

``` bash
rclone ls uablts:<bucket/path/directory>
```

This outputs all files along with their directory path recursively. So if you only specify the main bucket, it will output every file in the bucket no matter how deep in the directory tree.

To only list files and folders in a given directory, you can use the `lsf` subcommand

``` bash
rclone lsf uablts:<bucket/path/directory/>
```

**s3cmd**:

With s3cmd, you can use the `ls` command to list both buckets and their contents.

``` bash
s3cmd ls <s3://bucket/path/>
```

You can add the `--recursive` option to list all files in the given path. By default, it only lists objects or folders at the top level of the path.

**AWS CLI**:

``` bash
aws s3 ls <bucket/path/directory/> --endpoint-url https://s3.lts.rc.uab.edu
```

If you would like to list all objects recursively, you can add the `--recursive` tag. A couple of other helpful options are `--summarize` and `--human-readable` that will give a total number of objects and their size and make the size output more easily readable, respectively.

### Uploading Files and Folders

**RClone**:

Uploading files and folders can be done a couple of ways. The first is by using the `copy` subcommand. This will add files from the source to the destination.

``` bash
rclone copy <source> uablts:<bucket/destination>
```

The second method is using the `sync` subcommand. This subcommand makes the destination identical to the source. The `-i` option can be added to make it interactive, asking you whether to copy or delete each file.

``` bash
rclone sync [-i] <source> uablts:<bucket/destination/>
```

<!-- markdownlint-disable MD046 -->
!!! danger

    Be extremely cautious using sync. If there are files in the destination that are not in the source, it will delete those files in addition to adding files to the destination. If data is deleted from LTS, it is not recoverable.
<!-- markdownlint-enable MD046 -->

**s3cmd**:

s3cmd disinguishes between moving files between a local source and S3 versus moving files between two S3 locations using 3 different commands.

``` bash
# transfer from local to S3
s3cmd put <source> s3://<bucket/path/destination/>

# transfer from S3 to local
s3cmd get s3://<bucket/path/source/> <destination>

# transfer between two S3 locations
s3cmd cp s3://<bucket/path/> s3://<bucket/path/>
```

If you are transferring an entire folder from S3 to either another S3 location or a local destination, you will need to add the `--recursive` option, otherwise you will get an error.

Like rclone and AWS, there is also a `sync` command here as well.

``` bash
# sync an S3 location to a local source
s3cmd sync <source> s3://<bucket/path/destination>

# sync a local destination to an S3 location
s3cmd sync s3://<bucket/path/source> <destination>
```

**AWS CLI**:

Copying files and directories can be managed using the `cp` subcommand and has the same behavior as rclone's `copy`.

``` bash
aws s3 cp <source> s3://<bucket/path/destination> --endpoint-url https://s3.lts.rc.uab.edu [--recursive]
```

If you are copying a directory, you will need to add the `--recursive` option.

If you are wanting to copy data down from LTS to your local machine or Cheaha, just reverse the positions of the source and destination in the function call.

Like rclone, AWS also has a sync subcommand that performs the same functionality. You can use it like so:

``` bash
aws s3 sync <source> s3://<bucket/path/destination> --endpoint-url https://s3.lts.rc.uab.edu [--delete]
```

`sync` has an added benefit that only files that do not exist in the destination or files that have changed in the source will be transferred whereas `cp` copies everything no matter if it already exists in the destination. By default, `sync` DOES NOT cause files in the detination that are not in the source to be deleted like `rclone sync` does. If you want this functionality, you can add the `--delete` tag at the end of the function call.

<!-- markdownlint-disable MD046 -->
!!! danger

    Be extremely cautious using `--delete`. Only use if you are sure any data deleted is not important. Data deleted from LTS is not recoverable.
<!-- markdownlint-enable MD046 -->

### Deleting Files and Directories

**RClone**:

File deletion is performed using the `delete` subcommand.

``` bash
rclone delete uablts:<bucket/path/file>
```

Directory deletion is handled using the `purge` subcommand. Be very cautious with this, as this deletes all files and subdirectories within the directory as well.

``` bash
rclone purge uablts:<bucket/path/>
```

**s3cmd**:

File and directory deletion is handled by the `rm` command.

``` bash
s3cmd rm s3://<bucket/path/file> [--recursive]
```

If you want to delete a directory, you will need to add the `--recursive` option.

To delete an entire bucket, use the `rb` command.

``` bash
s3cmd rb s3://<bucket>
```

**AWS CLI**:

The subcommand for deleting files and folders from LTS is `rm`:

``` bash
aws s3 rm s3://<bucket/path/object> --endpoint-url https://s3.lts.rc.uab.edu [--recursive]
```

`rm` can delete both files and folders. If you are wanting to delete a folder and everything in it, you will need to add the `--recursive` option. Like with `sync` be very cautious using `rm` and make sure you know what you are deleting before you do so.

To delete an entire bucket, you will need to use the `s3api` command paired with the `delete-bucket subcommand. An example of this looks like:

``` bash
aws s3api delete-bucket --bucket <bucket> --endpoint-url https://s3.lts.rc.uab.edu
```

### Command Comparison Chart

<!-- markdownlint-disable MD046 -->
!!! note

    For brevity, the chart will exclude the `--endpoint-url` option from the AWS CLI commands, but it will need to be included if you choose to use that tool.
<!-- markdownlint-enable MD046 -->

| Action        | rclone                                                   | s3cmd                                            | AWS CLI                                                      |
| ------------- | -------------------------------------------------------- | ------------------------------------------------ | ------------------------------------------------------------ |
| Make Bucket   | `rclone mkdir uablts:<bucket>`                           | `s3cmd mb s3://<bucket>`                         | `aws s3api create-bucket --bucket <bucket>`                  |
| List Buckets  | `rclone lsd uablts:`                                     | `s3cmd ls`                                       | `aws s3 ls`                                                  |
| List Files    | `rclone lsf uablts:<bucket/path/>`                       | `s3cmd ls s3://<bucket/path/>`                   | `aws s3 ls s3://<bucket/path/>`                              |
| Full Upload   | `rclone copy <source> uablts:<bucket/destination>`       | `s3cmd put <source> s3://<bucket/destination/>`  | `aws s3 cp <source> s3://<bucket/destination>`               |
| Download      | `rclone copy uablts:<bucket/source/> <destination>`      | `s3cmd get s3://<bucket/source/> <destination>`  | `aws s3 cp s3://<bucket/source/> <destination>`              |
| Sync          | `rclone sync [-i] <source> uablts:<bucket/destination/>` | `s3cmd sync <source> s3://<bucket/destination/>` | `aws s3 sync <source> s3://<bucket/destination/> [--delete]` |
| Delete File   | `rclone delete uablts:<bucket/path/file>`                | `s3cmd rm s3://<bucket/path/file>`               | `aws s3 rm s3://<bucket/path/file>`                          |
| Delete Folder | `rclone purge uablts:<bucket/path/>`                     | `s3cmd rm s3://<bucket/path/> --recursive`       | `aws s3 rm s3://<bucket/path/> --recursive`                  |
| Delete Bucket | `rclone purge uablts:<bucket>`                           | `s3cmd rb s3://<bucket>`                         | `aws s3api delete-bucket --bucket <bucket>`                  |
