# Remote Access to Instances

All of the access methods described below are built on top of `ssh` and require completion of the steps in [Basic Security Setup](./security_setup_basic.md) to use with `cloud.rc`. Some of these steps are referenced in that document.

## Command Line via SSH

### Install an SSH Client

#### Windows SSH Clients

There are several options for installing an SSH client on Windows. The details of installation of SSH on Windows is beyond the scope of this document, but we will detail some tricky parts as needed. Generally, these are listed from least to most complex.

- Git Bash
    - The fine folks at Git have worked very hard to package everything needed to use Git on Windows into one installer. This includes and Linux command line interface emulator, Bash and SSH. Visit <https://git-scm.com> to download and install.
    - Follow the installer instructions. It is recommended to use all of the default installation options.
    - Once installed, locate "Git Bash" on your machine to open the Bash terminal. It should be searchable in the Start Menu.
- OpenSSH
    - Follow the instructions [here](https://docs.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse) to install the OpenSSH client.
    - Only install the OpenSSH server if you need it, otherwise skip that part.
    - Once the OpenSSH client is installed, you'll want to enable the OpenSSH Agent service on your local machine to streamline adding and using keys.
        - Open the Start Menu and search for "Services", and open the result shown in the image.
            ![!Searching for services in the start menu. ><](./images/openssh_search_services.png)
        - Find the "OpenSSH Authentication Agent" service in the list. Double click it, or right-click it and select "Properties".
            ![!Services list showing OpenSSH Authentication Agent highlighted. ><](./images/openssh_services_list.png)
        - In the dialog box, under the "General" tab, look for "Startup Type". Click the drop-down menu and select "Automatic (Delayed Start)". Click "Apply" at the bottom-right corner. This will cause the `ssh-agent` service to start when Windows starts.
        - The "Start" button under the horizontal line should become enabled. Click it to start the `ssh-agent` service now.
            ![!OpenSSH Authentication Agent Properties dialog box. ><](./images/openssh_ssh_agent_service_dialog.png)
- Windows Subsystem For Linux (WSL)
    - Follow the instructions starting [here](https://docs.microsoft.com/en-us/windows/wsl/about) to install Windows Subsystem for Linux.
    - We will not go into detail on installing or using this as it is quite involved. It is useful if you will be doing substantial Linux development on Windows, or need a full-fledged Linux operating system inside the Windows environment.

#### MacOS SSH Clients

- MacOS comes with an SSH client installed. If you are on version Leopard `10.5.1` or lower, you may want to have the `ssh-agent` start automatically using the command `sudo touch /var/db/useLS` at a terminal window.
- Versions newer than Leopard `10.5.1` start the `ssh-agent` automatically.

#### Linux SSH Clients

- Virtually all Linux distributions come with SSH preinstalled and configured appropriately for ease of use.

### Generating Key Pairs

The instructions are identical for all operating systems. [GitHub](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) maintains excellent documentation on generating keypairs.

1. Open a terminal window.
2. Use the command `ssh-keygen -t ed25519 -C "your_email@example.com"`
3. You will be prompted to choose a location to store the key, including a file name.
4. You will be prompted to enter a passphrase to secure the key.

### Managing Private Keys

The instructions are the same for all operating systems with one small exception noted below.

#### Add a Private Key

- Move the key file to the `.ssh` directory under your home directory.
- Navigate to the `.ssh` folder in a terminal window.
- Run `ssh-add <private_key_file>`

    ![!MINGW64 terminal on Windows. Commands have been used to move the private key file into the ssh folder and add it to the ssh agent. ><](./images/key_pairs_005.png)

    <!-- markdownlint-disable MD046 -->
    !!! bug

        For Linux users and [WSL](https://docs.microsoft.com/en-us/windows/wsl/about) on Windows users. If you experience a `Warning: Unprotected Private Key File` error when using `ssh-add`, your `ssh` file and directory permissions may be incorrect. To fix, please use the following commands.

        ```bash
        sudo chmod 600 ~/.ssh/<private_key_file>
        sudo chmod 644 ~/.ssh/known_hosts  # if you have ever connected to a remote machine
        sudo chmod 644 ~/.ssh/config  # if you have a config file
        sudo chmod 755 ~/.ssh
        ```
    <!-- markdownlint-enable MD046 -->

- MacOS Only
    - MacOS allows storing passphrases to the builtin Keychain with a special flag. Use `ssh-add -K <path/to/private_key_file>` to permanently store the passphrase that goes with the key file.

#### Remove a Private Key

Run `ssh-add -d <path/to/private_key_file>`

#### Remove an Invalid Host Fingerprint

<!-- markdownlint-disable MD046 -->
!!! danger

    The following command should **only** be run when reusing a floating IP for a new instance in a cloud context. Using it arbitrarily for remote machines you do not control can result in a security breach. Be absolutely certain you trust the source of the key change.
<!-- markdownlint-enable MD046 -->

A "Remote Host Identification Has Changed" error can be resolved by using the following command. It looks like the image below.

Run `ssh-keygen -R <hostname>` where `<hostname>` is the URL or IP address of the remote machine.

![!image showing remote host identification has changed error ><](./images/instances_ssh_host_key_error.png)

### Setting up a Configuration File

SSH configuration files help streamline the process of logging in to remote terminals by storing commonly-used arguments and flags for each host. To create a configuration file, navigate to your `.ssh` directory. Create a new plain text file called `config` with no extension. Open the file and add content like the following. Note that indent matters. Variable values in `<>` will be replaced with appropriate values before saving.

```ssh-config
Host <name>
  HostName <remote_ip>
  User <user>
  IdentityFile <absolute_path_to_private_key_file>
```

- Be sure to give a meaningful name under `<name>` so you can easily refer back to this config later and for ease of typing when using `ssh` with this configuration. Only letters, numbers, dashes and underscores are allowed, and it must start with a letter.
- The value `<remote_ip>` can be any remote machine relevant to your work. For cloud.rc it should be whatever IP was assigned in [Creating a Floating IP](./network_setup_basic.md#creating-a-floating-ip).
- The value `<user>` should be whatever user name you will log in as. For cloud.rc, `ubuntu` or `centos` are typical, depending on instance operating system.
- The value `<path_to_private_key_file>` is the absolute path to the private key file, e.g. the path to your `.ssh` folder followed by the `<private_key_file>` file name. For cloud.rc this will be whatever private key file was generated in [Creating a Key Pair](./security_setup_basic.md#creating-a-key-pair).

Save the `config` file. Start a new terminal and use the command `ssh <name>`, with no other flags, to test.

### SSH Client Usage

If you've [Set up a Configuration File](#setting-up-a-configuration-file), simply use `ssh <name>`, using the configuration name, to connect.

If you haven't set up a configuration file, use the following.

```bash
ssh <user>@<remote_ip> -i <private_key_file>
```

Where `user` is the remote username, `remote_ip` is the IP address of the remote machine, and `<private_key_file>` is the private key file used for access the remote machine. See [Generating Key Pairs](#generating-key-pairs) for general instructions on creating a key pair, or [Creating a Key Pair](./security_setup_basic.md#creating-a-key-pair) for cloud.rc specific instructions.

## Graphical Interface

## MobaXTerm

**Coming soon!**

## Data Transfer

## SCP

To install, see [Install an SSH Client](#install-an-ssh-client). The format for use is given below.

**More coming soon!**

## SFTP

To install, see [Install an SSH Client](#install-an-ssh-client). The format for use is given below.

**More coming soon!**

## `rclone`

**Coming soon!**

## FileZilla

**Coming soon!**
