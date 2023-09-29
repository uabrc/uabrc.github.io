# Connecting to LTS

LTS is not available as a mounted filesystem on local computers or Cheaha. You must use an interface to transfer data between LTS and whichever machine you are using. There a variety of interfaces with the following recommendations.

## Globus

[Globus](../transfer/globus.md#long-term-storage-s3-lts-connector) is a general file transfer system that operates through a web browser and is recommended for most file transfer needs. UAB has an S3 connector for Globus that can transfer data to and from LTS as long as the user has access to the desired buckets.

To connect to the LTS endpoint in Globus, search `UAB Research Computing LTS` in the search bar and enter your access and secret keys given to you by Research Computing staff. You will be able to see the buckets owned by the account associated with the keys you entered.

<!-- markdownlint-disable MD046 -->
!!! important

    If your LTS account was given permission to access a bucket owned by another account, it will not automatically appear in the Globus file browser. You can access buckets you have `s3:ListBucket` permissions on by typing `/<bucket-name>/` in the Path field under the LTS endpoint.

    ![!Access a shared bucket in Globus](images/globus-bucket.png) 
<!-- markdownlint-enable MD046 -->

Globus is very useful for single transfers of data either to or from LTS and is available on any computer with an internet connection. However, it is currently not capable of managing buckets. This must be done through a command line interface.

## Command Line

While globus is the recommended tool for most data transfers, command line tools are necessary for planned, regular transfers as well as managing permissions on buckets. We recommend the following two tools for different purposes:

1. [s3cmd](https://github.com/s3tools/s3cmd) is a Python tool that we suggest using for managing bucket permissions as well as small transfers.
2. [s5cmd](https://github.com/peak/s5cmd) is a Go package that transfers data much more quickly than s3cmd, especially as the file size and/or quanitity increases. It does not have full bucket management capabilities.

You do not need to install both tools if they aren't necessary. Both are available to install into [Anaconda](../../workflow_solutions/using_anaconda.md) environments. Specific install and usage commands for each are given in their respecitve sections.

### s3cmd

s3cmd is our suggested tool for managing bucket permissions and small, periodic file transfers. It can be easily installed via an Anaconda environment. Create the environment, activate it, then install using:

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

You can run the configuration either with or without the `[-c]` option. If you use it, a file named `profile_name` will be created in your home directory with your login credentials and other information. If you omit the `-c` option, a file called `$HOME/.s3cfg` will be created by default. This can be helpful if you have multiple S3 profiles you are using. If you use UAB LTS as your only S3 storage platform and are only managing a single account, it's suggested to omit the `-c` option. If you are a PI or data manager and are managing both a personal and lab/core LTS account, you will need to make a separate profile for each account.

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
S3 Endpoint [s3.amazonaws.com]: https://s3.lts.rc.uab.edu

Use "%(bucket)s.s3.amazonaws.com" to the target Amazon S3. "%(bucket)s" and "%(location)s" vars can be used if the target S3 system supports dns based buckets.
DNS-style bucket+hostname:port template for accessing a bucket [%(bucket)s.s3.amazonaws.com]: %(bucket).s3.lts.rc.uab.edu

Encryption password is used to protect your files from reading by unauthorized persons while in transfer to S3
Encryption password: <leave blank or enter password>
Path to GPG program [/usr/bin/gpg]: <leave blank>

When using secure HTTPS protocol all communication with Amazon S3 servers is protected from 3rd party eavesdropping. This method is slower than plain HTTP, and can only be proxied with Python 2.7 or newer
Use HTTPS protocol [Yes]: <leave blank>

On some networks all internet access must go through a HTTP proxy. Try setting it here if you can't connect to S3 directly
HTTP Proxy server name: <leave blank>

New settings:
  Access Key: <access key>
  Secret Key: <secret key>
  Default Region: US
  S3 Endpoint: https://s3.lts.rc.uab.edu
  DNS-style bucket+hostname:port template for accessing a bucket: %(bucket).s3.lts.rc.uab.edu
  Encryption password:
  Path to GPG program: $HOME/bin/gpg
  Use HTTPS protocol: True
  HTTP Proxy server name:
  HTTP Proxy server port: 0

Test access with supplied credentials? [Y/n] n

Save settings? [y/N] y
```

<!-- markdownlint-disable MD046 -->
!!! note

    If you choose to test access using your credentials, the test may fail. Do not rely on the automatic test results, test access yourself by either creating a bucket or listing files from a existing bucket using the commands listed below.
<!-- markdownlint-enable MD046 -->

#### s3cmd Commands

``` bash
# General command structure for s3cmd
s3cmd [-c profile_file] <command> [options] [-n --dry-run]
```

The `[-c profile_file]` is only required if you are using credentials NOT saved in the `$HOME/.s3cfg` file. Otherwise, you can omit it.

To see a list of all available commands, use `s3cmd --help`. Additionally, if you want to test an action without actually running it (i.e. it prints all actions that would be performed), you can add the `-n` or `--dry-run` option. A list of selected commands are provided below for reference

``` bash
# Create a bucket 
s3cmd mb s3://<bucket>

# List a bucket/path within the bucket
s3cmd ls [-r, --recursive] s3://<bucket/path>

# Check bucket or folder size
s3cmd du -H s3://<bucket/path/>

# transfer a file or folder from local to a bucket
s3cmd put <source> s3://<bucket/path/destination/>

# transfer a file or folder from a bucket to a local drive
s3cmd get s3://<bucket/path/source/> <destination>

# transfer between two S3 locations
s3cmd cp s3://<bucket/path/> s3://<bucket/path/>

# sync an S3 location with a local source. The S3 destination will be made exactly the same as the source including file deletions. 
# The source is unaltered. The S3 bucket/folder can be either the source or the destination
s3cmd sync <source> s3://<bucket/path/destination>

# remove a single object or all objects within a given path
s3cmd rm s3://<bucket/path/file> [--recursive]

# remove an entire bucket
s3cmd rb s3://<bucket>

# get info about the bucket
s3cmd info s3://<bucket>
```

<!-- markdownlint-disable MD046 -->
!!! danger

    Be extremely cautious using `sync`. If there are files in the destination that are not in the source, it will delete those files in addition to adding files to the destination. If data is deleted from LTS, it is not recoverable.
<!-- markdownlint-enable MD046 -->

<!-- markdownlint-disable MD046 -->
!!! note

    When using `ls` to list buckets, it will only show the buckets you own, not buckets you have been given permissions on. This is a limitation of the S3 system. You can still interact with any buckets you have been given relevant permissions on, but you will need to remember the names of the buckets you don't own.
<!-- markdownlint-enable MD046 -->

### s5cmd

s5cmd is a parallel transfer tool suggested for period transfers of large and/or many files at a time. It has options for customizing how many processors are available for transferring data as well as how many chunks files can be broken into during transfer to minimize transfer time. s5cmd can be installed easily in an Anaconda environment using the following command.

``` bash
conda install -c conda-forge s5cmd
```

#### Configuring s5cmd

s5cmd does not use the same authentication file as s3cmd. Instead, it uses official AWS SDK to access S3 including LTS. The default credentials file for AWS CLI would found at `${HOME}/.aws/credentials`. This file is then populated with different profiles and their access and secret keys. You can create the necessary file with the following commands.

``` bash
mkdir ${HOME}/.aws
touch ${HOME}/.aws/credentials
```

Open the credentials file with your favorite editor (i.e. `vim`, `nano`, `gedit`, etc.) and create a default profile by adding the following lines.

``` text
[default]
aws_access_key_id = <access_key>
aws_secret_access_key = <secret_key>
```

<!-- markdownlint-disable MD046 -->
!!! note

    Do not include the `<>` symbols in the credentials file when saving your keys
<!-- markdownlint-enable MD046 -->

One of the benefits of this credential method is that multiple sets of credentials can be kept in the same file. For instance, if you have both a lab/core LTS account and a personal account, you could set your personal account as the default profile and then add your lab credentials under a named profile like so:

``` text
[default]
aws_access_key_id = <personal_access_key>
aws_secret_access_key = <personal_secret_key>

[example-lab]
aws_access_key_id = <lab_access_key>
aws_secret_access_key = <lab_secret_key>
```

#### s5cmd Commands

s5cmd has the following general form.

``` bash
s5cmd --endpoint-url https://s3.lts.rc.uab.edu [global_options] command [command options] [arguments]
```

Here, global options must be kept separate from command specific options. For instance, the `--endpoint-url` option is a global option that specifies the URL for the S3 server. This must be included with every s5cmd command to communicate with UAB LTS, otherwise it will default to accessing AWS servers. Other global options include `--numworkers` and `--profile`, the number of available CPUs and which account to use in the `credentials` file, respectively. You can see a list of global options and the list of available commands by running `s5cmd --help`. A selection of commands are listed below.

``` bash
# copy all files from a local directory to a bucket using a single CPU
s5cmd --endpoint-url https://s3.lts.rc.uab.edu cp /path/to/directory/* s3://bucket/

# copy all files from a local directory to a bucket using 10 CPUs  and allowing the files to be broken into 5 parts during transfer
s5cmd --endpoint-url https://s3.lts.rc.uab.edu --numworkers 10 cp --concurrency 5 /path/to/directory/* s3://bucket/

# sync an S3 bucket (destination) to a local directory (source)
s5cmd --endpoint-url https://s3.lts.rc.uab.edu sync /path/to/directory/ s3://bucket/

# remove all objects with a given prefix from a bucket
s5cmd --endpoint-url https://s3.lts.rc.uab.edu rm s3://bucket/prefix/*
```

As with s3cmd, be very careful using the `sync` and `rm` commands as these can/will delete files either locally or on LTS. There are many more commands s5cmd can use as well as a number of command options that can be used to customize how an operation is performed. Please see the help documentation for a full list.

It's important to note that the main functionality of s5cmd over s3cmd is the parallelization options given by the `--numworkers` global option and the `--concurrency` local option for `cp` and `sync` commands. Choosing not to use these options will result in unoptimized performance.

<!-- markdownlint-disable MD046 -->
!!! important

    When setting the value for `--numworkers`, do not select a value beyond the number of CPUs you have requested for your job! This can cause high context switching (meaning individual CPUs are switching between multiple running processes) which can affect job performance for all jobs on a node.
<!-- markdownlint-enable MD046 -->

## Alternatives

There are other tools for interfacing with LTS such as rclone. Please see our [rclone documentation](../transfer/rclone.md) for more details.
