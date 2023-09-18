# Modules and Applications

Most software available on Cheaha is installed as modules, managed by the Lmod system. This document will provide a basic rundown of using Lmod commands to customize a software environment. `module` is the main command used to interface with module files in Lmod.

## Listing and Searching Modules

To begin, all module commands are run from the terminal. To know what software is installed on Cheaha, use the `avail` command.

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

## Best Practice for Loading Modules

To reduce unexpected behavior and/or to get rid of Lmod errors,

1. Avoid using `module load` in .bashrc. Instead create a bash script with the module load commands and source it each time to load the modules needed in a shell/sbatch script . Here is an example of loading module in a bash script named `module_test.sh` and compilation,

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

    Currently Loaded Modules:
    1) shared                          9) hwloc/1.11.2-GCC-4.9.3-2.25                               17) ncurses/6.0-foss-2016a
    2) slurm/18.08.9                  10) OpenMPI/1.10.2-GCC-4.9.3-2.25                             18) zlib/1.2.8-foss-2016a
    3) rc-base                        11) OpenBLAS/0.2.15-GCC-4.9.3-2.25-LAPACK-3.6.0               19) SAMtools/1.3.1-foss-2016a
    4) DefaultModules                 12) gompi/2016a                                               20) bzip2/1.0.6-foss-2016a
    5) GCCcore/4.9.3                  13) FFTW/3.3.4-gompi-2016a                                    21) Boost/1.61.0-foss-2016a
    6) binutils/2.25-GCCcore-4.9.3    14) ScaLAPACK/2.0.2-gompi-2016a-OpenBLAS-0.2.15-LAPACK-3.6.0  22) TopHat/2.1.1-foss-2016a
    7) GCC/4.9.3-2.25                 15) foss/2016a
    8) numactl/2.0.11-GCC-4.9.3-2.25  16) Bowtie/1.1.2-foss-2016a
    ```

2. Before loading modules in a shell/bash/sbatch script, use a clean shell by using `module reset` at the beginning to restore to default system settings. Using `module reset` before loading modules separates what software is loaded in the working shell, from software loaded in the script shell. Be aware that forked processes (like scripts) and Slurm commands inherit the environment variables of the working shell, including loaded modules. Here is an example that show case module conflict between cuda11.8 and cuda11.4 version that may lead to unexpected behavior or an erroneous output.

```bash
# Working shell where you may try testing module load and your run script
$ module load cuda11.4/toolkit

$ module list
Currently Loaded Modules:
  1) shared   2) slurm/18.08.9   3) rc-base   4) DefaultModules   5) cuda11.4/toolkit/11.4.2
```

```bash
# bash/sbatch script you are submitting to slurm
#!/bin/bash
module load cuda11.8/toolkit
```

```bash
# Not using `module reset` at the beginning could cause CUDA conflict issues.
$ source ./module_test.sh

Currently Loaded Modules:
  1) shared   2) slurm/18.08.9   3) rc-base   4) DefaultModules   5) cuda11.4/toolkit/11.4.2   6) cuda11.8/toolkit/11.8.0
```

<!-- markdownlint-disable MD046 -->
!!! note

    The best practice would be to avoid using `module reset` in the `Environment Setup` of Open OnDemand jobs as the OOD session by default resets the module at the beginning of every session. It is observed to cause unexpected behavior while loading `module reset` in the Rstudio server OOD sessions.
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
