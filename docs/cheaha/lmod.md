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
module spider \<string\>

# list modules matching a regular expression
module -r spider \<regex\>
```

## Loading Modules

To load modules, run:

``` bash
module load module1 module2 ...
```

!!! note
   If you only specify a module name without an accompanying version tag, the most recently installed version will be loaded into the workspace. If your scripts depend on specific versions of software being used, explicitly load the module version you need.

To unload packages, run:

``` bash
module unload package1 package2 ...
```

If you want to revert to the default modules, you can use:

``` bash
module reset
```
