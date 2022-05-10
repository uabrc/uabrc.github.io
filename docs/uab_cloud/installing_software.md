# Installing Software on Instances

An important part of managing instances is the installation of software. This page assumes you have a working instance and can [SSH](./instance_setup_basic.md#ssh-into-the-instance) into it. This page assumes you are using an Ubuntu image.

We highly recommend building your research software stack into a [Container](../environment_management/containers.md). While there is a learning curve and some setup time, containers make replicating and sharing environments simpler. Everything you develop is packaged into a self-contained unit that can be run on virtually any modern Linux system.

A particular command `sudo` will be used extensively. Be warned that `sudo` grants any commands used administrator privileges. If you use `sudo` with untrustworthy software, you may be allowing an attacker to compromise your system.

<!-- markdownlint-disable MD046 -->
!!! danger

    The `sudo` command should be used carefully and judiciously, as it creates security risks. Use with caution.
<!-- markdownlint-enable MD046 -->

## Before Installing Software

Before installing software, good practice is updating and upgrading operating system packages. For some software this is required. These updates often include critical security and bug fixes. To update the instance operating system, enter the following at the command line.

```bash
sudo apt update
sudo apt upgrade
```

## Installing Software

Most common software packages and NVIDIA drivers are available as `apt` packages. Some packages are available using custom installers. Be sure the website and installer author are trustworthy before installing!

### Finding Packages

1. Try using Google to locate the name of the package with something like `ubuntu apt <keywords>`
2. Try using <https://packages.ubuntu.com>
3. Try `apt-cache search <keyword>`
4. Ask [Support](../help/support.md) for help

### Installing Packages

If the software is available via `apt` then use `sudo apt install <package>`. An example would be `sudo apt install git` to install git software.

If the software uses a custom installer, then follow the instructions provided by the software's documentation. An example would be [Miniconda](#installing-miniconda), where a shell script is downloaded and then executed using `bash installer.sh`.

### Common Examples

#### Installing NVidia Drivers

1. Run the commands in [Before Installing Software](#before-installing-software).
2. `sudo apt install ubuntu-drivers-common`
3. `ubuntu-drivers devices`
4. Find the line with "recommended" and install the package on that line with `sudo apt install nvidia-driver-###`
5. Reboot the instance

#### Installing Miniconda

We recommend installing [Miniconda](https://docs.conda.io/en/latest/miniconda.html) on cloud.rc instances, as opposed to Anaconda, to conserve storage space.

1. Run the commands in [Before Installing Software](#before-installing-software).
2. `wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh`
3. `bash Miniconda3-latest-Linux-x86_64.sh`

<!-- markdownlint-disable MD046 -->
!!! tip

    Consider installing [Mamba](../environment_management/conda.md#mamba) to speed up environment installation.
<!-- markdownlint-enable MD046 -->

#### Installing Singularity

Follow the instructions located at <https://sylabs.io/guides/3.9/user-guide/quick_start.html#install-system-dependencies> under "Debian-based systems".

1. Run the commands in [Before Installing Software](#before-installing-software).
2. Run the following

    ```bash
    sudo apt-get install -y \
    build-essential \
    libseccomp-dev \
    pkg-config \
    squashfs-tools \
    cryptsetup
    ```

3. Install Go language using the following

    ```bash
    export VERSION=1.17.2 OS=linux ARCH=amd64 && \  # Replace the values as needed
    wget https://dl.google.com/go/go$VERSION.$OS-$ARCH.tar.gz && \ # Downloads the required Go package
    sudo tar -C /usr/local -xzvf go$VERSION.$OS-$ARCH.tar.gz && \ # Extracts the archive
    rm go$VERSION.$OS-$ARCH.tar.gz    # Deletes the ``tar`` file

    echo 'export PATH=/usr/local/go/bin:$PATH' >> ~/.bashrc && \
    source ~/.bashrc
    ```

4. Download SingularityCE

    ```bash
    export VERSION=3.9.5 && # adjust this as necessary \
    wget https://github.com/sylabs/singularity/releases/download/v${VERSION}/singularity-ce-${VERSION}.tar.gz && \
    tar -xzf singularity-ce-${VERSION}.tar.gz && \
    cd singularity-ce-${VERSION}
    ```

5. Compile SingularityCE

    ```bash
    ./mconfig && \
    make -C builddir && \
    sudo make -C builddir install
    ```

<!-- markdownlint-disable MD046 -->
!!! note

    For other versions of the Singularity documentation, visit <https://sylabs.io/docs/>.
<!-- markdownlint-enable MD046 -->
