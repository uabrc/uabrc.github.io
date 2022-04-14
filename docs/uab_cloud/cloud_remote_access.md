# Remote Access to Instances

All of the access methods described below are built on top of `ssh` and require completion of the steps in [Basic Security Setup](./security_setup_basic.md) to use with `cloud.rc`. Some of these steps are referenced in that document.

## Command Line via SSH

SSH stands for **S**ecure **SH**ell and is a powerful tool for executing terminal commands on remote machines. It is widely used and ubiquitous, and a number of other technologies are built on top of SSH, like `sftp` and `scp` for transferring files. It is also the primary mode of command line communication with Research Computing technologies like Cheaha and cloud.rc.

### Install an SSH Client

There are two main steps to working with SSH efficiently. The first is to ensure you have an SSH client installed, which will let your local machine communicate with remote machines. The second is to ensure you have `ssh-agent` running in each terminal window to automate management of key files. The `ssh-agent` software comes with most SSH clients, but does not always run automatically. How to start the `ssh-agent` software automatically varies depending on operating system and shell flavor, which we will describe below.

#### Install an SSH Client  (Linux)

Virtually all Linux distributions come with SSH preinstalled and configured appropriately for ease of use, including automatically starting the `ssh-agent`.

### Install an SSH Client  (MacOS)

MacOS comes with an SSH client installed.

If you are on version Leopard `10.5.1` or lower, you may want to have the `ssh-agent` start automatically using the command `sudo touch /var/db/useLS` at a terminal window. Versions newer than Leopard `10.5.1` start the `ssh-agent` automatically.

### Install an SSH Client (Windows)

There are several options for installing an SSH client on Windows, described below. It is highly recommended to install Windows Subsystem for Linux (WSL) as it provides a complete Linux environment within Windows.

#### Windows Subsystem For Linux (WSL)

Follow the instructions starting [here](https://docs.microsoft.com/en-us/windows/wsl/about) to install Windows Subsystem for Linux.

WSL shells do not automatically start or share the `ssh-agent`. To fix this we recommend installing `keychain` to automatically manage the `ssh-agent`. Run the following command depending on your Linux distribution.

- DEB-based (Debian, Ubuntu): `sudo apt install keychain`
- RPM-based (CentOS, Fedora, openSUSE): `sudo yum install keychain`

Then modify the `.*rc` file for your shell, generally `.bashrc` or `.zshrc`, to automate the `ssh-agent` by adding the following line.
        - ```eval `keychain -q --eval --agents ssh` ```

<!-- markdownlint-disable MD046 -->
!!! tip

    You can access WSL files from within Windows in two ways.

    In the WSL terminal, enter `explorer.exe .` to open a File Explorer window in the current directory.

    In Windows, open a File Explorer window, click in the top navigation bar and enter `\\wsl$`. Then select your distribution from the file window to access the filesystem of that WSL operating system.
<!-- markdownlint-enable MD046 -->

#### OpenSSH for Windows

Follow the instructions [here](https://docs.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse) to install the OpenSSH client. Only install the OpenSSH server if you need it, otherwise skip that part.

Once the OpenSSH client is installed, you'll want to enable the OpenSSH Agent service on your local machine to streamline adding and using keys.

- Open the Start Menu and search for "Services", and open the result shown in the image.
    ![!Searching for services in the start menu. ><](./images/openssh_search_services.png)
- Find the "OpenSSH Authentication Agent" service in the list. Double click it, or right-click it and select "Properties".
    ![!Services list showing OpenSSH Authentication Agent highlighted. ><](./images/openssh_services_list.png)
- In the dialog box, under the "General" tab, look for "Startup Type". Click the drop-down menu and select "Automatic (Delayed Start)". Click "Apply" at the bottom-right corner. This will cause the `ssh-agent` service to start when Windows starts.
- The "Start" button under the horizontal line should become enabled. Click it to start the `ssh-agent` service now.
    ![!OpenSSH Authentication Agent Properties dialog box. ><](./images/openssh_ssh_agent_service_dialog.png)

#### Git Bash terminal (Git for Windows)

The fine folks at Git have worked very hard to package everything needed to use Git on Windows into one installer. This includes and Linux command line interface emulator, Bash and SSH. Visit <https://git-scm.com> to download and install. Follow the installer instructions. It is recommended to use all of the default installation options. Once installed, locate "Git Bash" on your machine to open the Bash terminal. It should be searchable in the Start Menu.

To automate running `ssh-agent` add the following block to the file `.bash_profile` in the `~` directory within Git Bash. Then use `source .bash_profile` to start the `ssh-agent`, or open a new terminal.

```bash
env=~/.ssh/agent.env

agent_load_env () { test -f "$env" && . "$env" >| /dev/null ; }

agent_start () {
    (umask 077; ssh-agent >| "$env")
    . "$env" >| /dev/null ; }

agent_load_env

# agent_run_state: 0=agent running w/ key; 1=agent w/o key; 2= agent not running
agent_run_state=$(ssh-add -l >| /dev/null 2>&1; echo $?)

if [ ! "$SSH_AUTH_SOCK" ] || [ $agent_run_state = 2 ]; then
    agent_start
    ssh-add
elif [ "$SSH_AUTH_SOCK" ] && [ $agent_run_state = 1 ]; then
    ssh-add
fi
```

### Generating Key Pairs

The instructions for generating key pairs are identical for all operating systems. [GitHub](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) maintains excellent documentation on generating key pairs. The gist of those instructions follows.

1. Open a terminal window.
2. Use the command `ssh-keygen -t ed25519 -C "your_email@example.com"`
3. You will be prompted to choose a location to store the key, including a file name.
4. You will be prompted to enter a passphrase to secure the key. It is highly recommended to secure your key pair with a passphrase to minimize risk.

### Managing Keys

The instructions below are the same for all operating systems with one small exception noted below.

<!-- markdownlint-disable MD046 -->
!!! important

    If at any point you encounter an error like below, please check to be sure your `ssh-agent` is running based on how you [Installed your SSH Client](#install-an-ssh-client).

    ```bash
    Could not open a connection to your authentication agent.
    ```
<!-- markdownlint-enable MD046 -->

#### Starting the SSH Agent for a Single Session

If `ssh-agent` isn't already running and you encounter an error, use the following commands to start the `ssh-agent` depending on your environment. It is highly recommended to use the most appropriate method described in [Install an SSH Client](#install-an-ssh-client) to have `ssh-agent` start automatically.

- Linux, MacOS, Git Bash, WSL: `eval $(ssh-agent -s)`
- Windows OpenSSH: `start-ssh-agent`

#### Add a Private Key

- Move the key file to the `.ssh` directory under your home directory.
- Navigate to the `.ssh` folder in a terminal window.
- Run `ssh-add <private_key_file>`

    ![!MINGW64 terminal on Windows. Commands have been used to move the private key file into the ssh folder and add it to the ssh agent. ><](./images/key_pairs_005.png)

    <!-- markdownlint-disable MD046 -->
    !!! bug

        For Linux users and [WSL](https://docs.microsoft.com/en-us/windows/wsl/about) on Windows users. If you experience a `Warning: Unprotected Private Key File` error when using `ssh-add`, your `ssh` file and directory permissions may be incorrect. To fix, please use the following commands.

        ```
        sudo chmod 600 ~/.ssh/<private_key_file>
        sudo chmod 644 ~/.ssh/known_hosts
        sudo chmod 755 ~/.ssh
        ```
    <!-- markdownlint-enable MD046 -->

    <!-- markdownlint-disable MD046 -->
    !!! tip

        MacOS allows storing passphrases to the builtin Keychain with a special flag. Use `ssh-add -K <path/to/private_key_file>` to permanently store the passphrase that goes with the key file.
    <!-- markdownlint-enable MD046 -->

#### Remove a Private Key

Run `ssh-add -d <path/to/private_key_file>`

#### Push a New Public Key File to a Remote Machine

To push a new public key file to a remote machine, please use the `ssh-copy-id` command. If your `ssh-agent` is running and has a known-good private key added, then the command below will work as expected and add the `<new_public_keyfile>.pub` to the remote machine. You must also have the private key counterpart `<new_private_keyfile>` with the same name as the public key file, without the `.pub` extension.

```bash
ssh-copy-id -i ~/.ssh/<new_public_keyfile> <user>@<remote_ip>
```

The value `<user>` should be replaced with the remote user you will login as. The value `<remote_ip>` should be replaced with the IP address of the remote machine.

To verify, use `ssh -i ~/.ssh/<new_private_keyfile>.pub <user>@<remote_ip>`.

#### Remove an Invalid Host Fingerprint

This command should **only** be run when reusing a floating IP for a new instance in a cloud context.

Run `ssh-keygen -R <hostname>` where `<hostname>` is the URL or IP address of the server.

<!-- markdownlint-disable MD046 -->
!!! danger

    Using the command `ssh-keygen -R` is risky when connecting to machines or instances controlled by other people. Be _absolutely certain_ you trust that the current fingerprint is invalid before removing it and accepting a new fingerprint!
<!-- markdownlint-enable MD046 -->

### Setting up a Configuration File

SSH configuration files help streamline the process of logging in to remote terminals by storing commonly-used arguments and flags for each host. To create a configuration file, navigate to your `.ssh` directory. Create a new plain text file called `config` with no extension. Open the file and add content like the following. Note that indent matters.

```ssh-config
Host <host>
  HostName <remote_ip>
  User <user>
  IdentityFile <absolute_path_to_private_key_file>
```

Be sure to give a meaningful name under `<host>` so you can easily refer back to this config later. Only letters, numbers, dashes and underscores are allowed, and it must start with a letter. The value `<remote_ip>` can be any remote machine relevant to your work. For cloud.rc it should be whatever IP was assigned in [Creating a Floating IP](./network_setup_basic.md#creating-a-floating-ip). The value `<user>` should be whatever user name you will log in as. For cloud.rc, `ubuntu` or `centos` are typical, depending on instance operating system. The value `<path_to_private_key_file>` is the absolute path to the private key file, e.g. the path to your `.ssh` folder followed by the `<private_key_file>` file name.

Save the file. Start a new terminal and use the command `ssh <host>`, with no other flags, to test. You can also use `<host>` with [SCP](#scp) and [SFTP](#sftp).

### SSH Client Usage

If you've [Set up a Configuration File](#setting-up-a-configuration-file), simply use `ssh <remote_ip>` to connect.

If you haven't set up a configuration file, use the following.

```bash
ssh user@<remote_ip> -i <private_key_file>
```

## Graphical Interface

## MobaXTerm

**Coming soon!**

## Data Transfer

## `scp`

To install, see [Install an SSH Client](#install-an-ssh-client). The format for use is given below.

**More coming soon!**

## `sftp`

To install, see [Install an SSH Client](#install-an-ssh-client). The format for use is given below.

**More coming soon!**

## `rclone`

**Coming soon!**

## FileZilla

**Coming soon!**
