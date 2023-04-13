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
