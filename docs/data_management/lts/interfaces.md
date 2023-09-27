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

### s3cmd Commands

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

# sync an S3 location with a local source. The S3 destination will be made exactly the same as the source including file deletions. The source is unaltered. The S3 bucket/folder can be either the source or the destination
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
