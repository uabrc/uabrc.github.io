# Remote Access to Instances

All of the access methods described below are built on top of `ssh` and require completion of the steps in [Basic Security Setup](./security_setup_basic.md).

## Command Line via SSH

### Install an SSH Client

- Windows
    - There are several options for installing an SSH client on Windows. The details of installation of SSH on Windows is beyond the scope of this document, but we will detail some tricky parts as needed. Generally, these are listed from least to most complex.
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
- MacOS
    - MacOS comes with an SSH client installed. If you are on version Leopard `10.5.1` or lower, you may want to have the `ssh-agent` start automatically using the command `sudo touch /var/db/useLS` at a terminal window.
    - Versions newer than Leopard `10.5.1` start the `ssh-agent` automatically.
- Linux
    - Virtually all Linux distributions come with SSH preinstalled and configured appropriately for ease of use.

### Generating Key Pairs

The instructions are identical for all operating systems. [GitHub](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent) maintains excellent documentation on generating keypairs.

1. Open a terminal window.
2. Use the command `ssh-keygen -t ed25519 -C "your_email@example.com"`
3. You will be prompted to choose a location to store the key, including a file name.
4. You will be prompted to enter a passphrase to secure the key.

### Manage Private Keys

- All Operating Systems
    - Add key: `ssh-add <path/to/private_key_file>`
    - Remove key: `ssh-add -d <path/to/private_key_file>`
    - Remove invalid host fingerprint: `ssh-keygen -R <hostname>` where `<hostname>` is the URL or IP address of the server.

<!-- markdownlint-disable MD046 -->
        !!! danger

            Using the above command is risky when connecting to machines or instances controlled by other people. Be _absolutely certain_ you trust that the current fingerprint is invalid before removing it and accepting a new fingerprint!
<!-- markdownlint-enable MD046 -->

- MacOS Only
    - MacOS allows storing passphrases to the builtin Keychain with a special flag. Use `ssh-add -K <path/to/private_key_file>` to permanently store the passphrase that goes with the key file.

## Graphical Interface

## MobaXTerm

## Data Transfer

## `scp`

## `sftp`

## FileZilla
