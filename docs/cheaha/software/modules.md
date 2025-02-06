# Pre-installed Modules

Most software available on Cheaha is installed as modules, managed by the Lmod system. This document will provide a basic rundown of using Lmod commands to customize a software environment. `module` is the main command used to interface with module files in Lmod.

As of the most recent update of this page there are 4,445 active modules installed on Cheaha. The most commonly used general research software modules are listed in the table below. Read on to learn more about searching for and loading modules. If you can't find what you need in our modules, learn more about [getting software installed](./software.md). If you need further assistance, please [contact Support](../../help/support.md).

<!--
Count modules with the following command
`module -t avail 2>&1 >/dev/null | wc -l`
-->

{{ read_csv('cheaha/software/res/common_software.csv', keep_default_na=False) }}

## Listing and Searching Modules

To begin, all module commands are run from the [terminal](../open_ondemand/ood_layout.md#opening-a-terminal). To know what software is installed on Cheaha, use the `avail` command.

``` bash
module avail
```

If you need to know what software is already loaded in your environment, run:

``` bash
module list
```

If there is specific software you want to search for, you can use the `spider` subcommand, and provide a string or regular expression to match against. All modules containing the string (case-insensitive) or matching the regular expression will be returned along with their installed versions.

``` bash
# list modules containing string
module spider <string>

# list modules matching a regular expression
module -r spider <regex>
```

## Loading Modules

To load modules, run:

``` bash
module load module1 module2 ...
```

<!-- markdownlint-disable MD046 -->
!!! note

    If you only specify a module name without an accompanying version tag, the most recently installed version will be loaded into the workspace. If your scripts depend on specific versions of software being used, explicitly load the module version you need.
<!-- markdownlint-enable MD046 -->

To unload packages, run:

``` bash
module unload package1 package2 ...
```

If you want to revert to the default modules, you can use:

``` bash
module reset
```

## Saving Modules using Collections

To save time in typing in long list of modules everytime you work on a project, you can save the desired list of modules using module collection. To acheive this, load the desired modules and save them to a collection using a module collection name, as shown below.

```bash
module load module_1 module_2 ...

module save collection_name
```

Here, the `collection_name` can be something relevant to your project and easy to remember.

To load the desired modules using the saved collection use,

``` bash
module restore collection_name
```

To delete a collection use the below command,

``` bash
module disable collection_name
```

To list the save list of module collection use,

``` bash
module savelist
```

<!-- markdownlint-disable MD046 -->
!!! warning

    Using `module save` command without a collection name saves the desired modules in the name `default` to the location $HOME/.lmod.d/default, and causes issue in launching [Open On Demand (OOD) HPC desktop job](../../cheaha/open_ondemand/hpc_desktop.md). The user gets a VNC error such as, `Unable to contact settings server` and/or `Unable to load a failsafe session`.  To address this issue, it is recommended to follow the instructions outlined in the [FAQ entry](https://ask.cyberinfrastructure.org/t/why-do-i-get-an-error-when-launching-an-open-ondemand-hpc-interactive-session/2496/3).
<!-- markdownlint-enable MD046 -->

## Best Practice for Loading Modules

When using modules in Cheaha, we recommend users to follow these best practices to avoid any potential module conflicts, reduce unexpected behavior and/or to get rid of Lmod errors:

1. Avoid using `module load` in `$HOME/.bashrc`. Instead, create a bash script with the module load commands and source it each time to load the modules needed in a shell/[sbatch script](../slurm/submitting_jobs.md). Here is an example of loading module in a bash script named `module_test.sh` and compilation,

    ```bash
    #!/bin/bash
    module reset
    module load Bowtie/1.1.2-foss-2016a
    module load SAMtools/1.3.1-foss-2016a
    module load TopHat/2.1.1-foss-2016a
    module -t list
    ```

    ```bash
    $ chmod +x module_test.sh
    $ source ./module_test.sh

    Resetting modules to system default

    # Currently Loaded Modules
    shared
    slurm/18.08.9
    rc-base
    DefaultModules
    GCCcore/4.9.3
    binutils/2.25-GCCcore-4.9.3
    GCC/4.9.3-2.25
    numactl/2.0.11-GCC-4.9.3-2.25
    hwloc/1.11.2-GCC-4.9.3-2.25
    OpenMPI/1.10.2-GCC-4.9.3-2.25
    OpenBLAS/0.2.15-GCC-4.9.3-2.25-LAPACK-3.6.0
    gompi/2016a
    FFTW/3.3.4-gompi-2016a
    ScaLAPACK/2.0.2-gompi-2016a-OpenBLAS-0.2.15-LAPACK-3.6.0
    foss/2016a
    Bowtie/1.1.2-foss-2016a
    ncurses/6.0-foss-2016a
    zlib/1.2.8-foss-2016a
    SAMtools/1.3.1-foss-2016a
    bzip2/1.0.6-foss-2016a
    Boost/1.61.0-foss-2016a
    TopHat/2.1.1-foss-2016a
    ```

1. Be selective and only load a specific module version that you need for your current workflow. Loading unnecessary modules can lead to conflicts and inefficiencies.
1. Before loading modules in a shell/bash/sbatch script, use a clean shell by using `module reset` at the beginning.
      - What it does:
         - Clearing loaded modules.
         - Loading default modules specified by the system administrator.
      - What it prevents from happening:
          - Module conflicts.
      - Why it is a best-practice:
          - Ensures reproducibility by starting with a clean environment.
          - Manages software dependencies effectively.

Using `module reset` before loading modules separates what software is loaded in the working shell from the software loaded in the script shell. Be aware that forked processes (like scripts) and Slurm commands inherit the environment variables of the working shell, including loaded modules. Here is an example that shows module conflict between cuda11.8 and cuda11.4 versions that may lead to unexpected behavior or an erroneous output.

```bash
# Working shell where you may try testing module load and your run script
$ module load cuda11.4/toolkit

$ module -t list

#Currently Loaded Modules
shared
slurm/18.08.9
rc-base
DefaultModules
cuda11.4/toolkit/11.4.2
```

```bash
# bash script you are passing in a sbatch script
#!/bin/bash
module load cuda11.8/toolkit
module -t list
```

```bash
# Not using `module reset` at the beginning of the bash script could cause CUDA conflict issues.
$ source ./module_test2.sh

#Currently Loaded Modules
shared
slurm/18.08.9
rc-base
DefaultModules
cuda11.4/toolkit/11.4.2
cuda11.8/toolkit/11.8.0
```

<!-- markdownlint-disable MD046 -->
!!! note

    The best practice would be to avoid using `module reset` in the `Environment Setup` of [Open OnDemand jobs](../open_ondemand/ood_layout.md#environment-setup-window) as the OOD session, by default, resets the module at the beginning of every session. It is observed to cause unexpected behavior if `module reset` is used in the Rstudio server OOD sessions.
<!-- markdownlint-enable MD046 -->

## Licensed and Commercial Software Restrictions

The following software have license restrictions that may preclude some researchers or collaborators depending on their departmental or group affiliations. In the table, "affiliated" means employed by, or a student of, unless otherwise noted. External collaborators are not considered affiliated with UAB for the purposes of software licensing and access, unless otherwise noted. These software packages may be commercial paid software. If you believe you should have access to software that you do not have access to, please contact [Support](../../help/support.md).

{{ read_csv('cheaha/software/res/restricted_software.csv', keep_default_na=False) }}

Use of these software packages without authorization may be a violation of the [UAB IT Acceptable Use Policy](../../policies.md#acceptable-use-policy-aup).

## Security Issues

### IGV

<!-- markdownlint-disable MD046 -->
!!! danger

    Versions of IGV prior to `2.11.9` use a compromised version of log4j. Those versions are affected by a serious [remote code execution issue](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-44832). Please transition your software to use versions of IGV >= `2.11.9`.
<!-- markdownlint-enable MD046 -->

### GSEA

<!-- markdownlint-disable MD046 -->
!!! danger

    Versions of GSEA prior to `4.2.3` use a compromised version of log4j. Those versions are affected by a serious [remote code execution issue](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-44832). Please transition your software to use versions of GSEA >= `4.2.3`.
<!-- markdownlint-enable MD046 -->

### Rsync

<!-- markdownlint-disable MD046 -->
!!! danger

    Versions of Rsync prior to `3.4.0` contain [six known vulnerabilities](https://www.openwall.com/lists/oss-security/2025/01/14/3), some of which allow for arbitrary code execution. The risk to our system is minimal because of scoped user permissions. Nevertheless, Cheaha is now using version 3.4.1. Older versions have been removed, apologies for any inconvenience.
<!-- markdownlint-enable MD046 -->

## Known Issues

### Matlab Issues

There is a critical, hard-to-diagnose MATLAB parpool bug in versions before R2022a.

The issue arises when using a `parpool` for multiple jobs simultaneously, as with an `sbatch --array` job. MATLAB `parpool` can be started manually, or at the first `parfor` loop encountered, among other functionality. See the [MATLAB Documentation](https://www.mathworks.com/help/parallel-computing/run-code-on-parallel-pools.html) for more information and a complete list.

Before R2022a, MATLAB assumed that only one parpool will be used at a time for each user, and put necessary communication files in a common directory. When multiple parpools are run simultaneously by the same user, they may attempt to write to those files at the same time, corrupting the files, resulting in a range of obscure Parallel Computing Toolbox (PCT) errors. The collisions are effectively random, which can make the issue hard to reproduce and hard to diagnose. The more parpools open simultaneously, the more likely there will be at least one error. In the worst case, we have seen unrecoverable corruption of the parpool common directory, which can be fixed by deleting the directory.

Symptoms of the bug include:

- Excessive load and context switching on affected nodes
- Inconsistent and varied PCT errors
- Inability to start Matlab parpool

To avoid the bug, please use the latest available version of MATLAB and no earlier than R2022a. Upgrading MATLAB versions may require some effort and testing of your code, because MATLAB is not always backwards compatible. Be sure to test that your code works as expected on the new version before using it for research.

If you aren't able to use R2022a or newer, there is a workaround available. Please navigate to this [GitHub repository](https://github.com/wwarriner/matlab_parpool_slurm_fix) and follow the instructions in `README.md`. Some light MATLAB programming is required to effectively use the workaround. Please contact [Support](../../help/support.md) if you would like assistance.
