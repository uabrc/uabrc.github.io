# Linux Permissions and Access Control Lists (ACLs)

Linux has two features for controlling who can access what data: permissions and access control lists (ACLs). As a researcher responsible for research data, it is up to you to use these tools to control access to data within your shared storage allocations.

While permissions and ACLs may seem overwhelming at first, there are only a few common setups that cover most use cases, and we will cover these first.

- Data accessible to everyone.
- Data accessible only to a specific subset of people.
- Read-only data.

You can check the permissions of any

Further along on this page are the details you can put together to cover other cases. This article assumes the good practice of keeping data for each of your research projects in separate directories.

<!-- markdownlint-disable MD046 -->
!!! note

    In Linux, folders are called directories.
<!-- markdownlint-enable MD046 -->

## Terminology

- **permission**: A set of binary bits that instruct the Linux operating system who can access what.
- **mode**: The
- **user**: The three binary bits that describe permissions for the **user owner**.
- **user owner**: The individual who owns a given file or directory.
- **group**: The three binary bits that describe permissions for the **group owner**.
- **group owner**: The "group", or collection of individuals, who own a given file or directory.
- **other**: The three binary bits that describe permissions for everyone else.

## Anatomy of Permissions

There are two ways to communicate permissions

- As a three or four digit decimal number representing a binary number, called
  the mode.
    - If the number is three digits, then the digits apply to, in order:
        1. the user owner
        1. the group owner
        1. everyone else
    - If the number is four digits...
        - the first digit applies only to directories and affects special
      features of the folder: `setuid`, `setgid` and the sticky bit.
        - the remaining three digits should be treated as the three digit case above.
- As a string of 10 letters and dashes, called the mode string.
    - The first character indicates the type of the file or directory. `d`
      indicates a directory, `-` indicates a regular data file. Other types
      exist but are uncommon and outside the scope of this article.
    - The remaining 9 characters are split into three triplets.
        - In order, the triplets apply to:
            - the user owner
            - the group owner
            - everyone else
        - The characters in each triplet mean the following:
            - `r` for read
            - `w` for write
            - `x` for execute
        - If the character is a letter, then that permission is allowed.
        - If the character is a dash `-`, then that permission is not allowed.
        - Each possible combination  of the decimal representation
      digits. The following conversion table will show how.

`file type`

## How Do I Check Permissions?

Use the following to see the permissions for any file or directory you can access.

```shell
ls -al /path/to/a/directory/
ls -al /path/to/a/file
```

Here are a couple of lines from an example output, with annotations.

```bash
# mode-string  links  user-owner  group-owner  bytes  last-modified-date  name.....
  drwxrws---   2     wwarr       wwarr-lab    4096   Mar 12 11:20        directory
  -rw-rw-r--   1     wwarr       wwarr-lab    5538   Mar 13 16:47        file.txt
# ||  |  |
# ||  |  other permissions (r--)
# ||  group permissions (rw-)
# |user permissions (rw-)
# file type ("d": directory, "-": regular file)
```

- The mode string tells us what the file type and who can do what with the file or directory. It is composed of a single character, followed by three triplets of characters, for a total of ten characters. For the file type character, `-` indicates a regular data file, `d` a directory.
- The user owner (`wwarr`) is the person who created the file and "owns" it. The first triplet of the mode string shows what permissions the owner has. `rwx` for the directory, `rw-` for the file. This allows the user owner to set different permissions for themselves than the group. Useful for read-only files!
- The group owner (`wwarr-lab`) is the group who can access the file with the second triplet of permissions. `rws` for the directory, `rw-` for the file. Like with the user owner, the group owner triple allows settings different permissions for a group than for everyone else.
- The third and final triplet reflects what permissions everyone outside the user owner and group owner have. `---` for the directory, `r--` for the file.

The letters in each triple are `r` for read, `w` for write, and `x` for execute. The letter is present if the permission is allowed, and is replaced with a dash if not allowed. The letter `s` means that the `x` execute permission was granted _and_ a special `setgid` bit was set. The special bit will be discussed further along.

Note that mode can alternatively be represented as an integer with three digits, one for each triplet, in the same order. The digits are written in decimal and correspond to the binary representation of the triplets. Read has decimal value `r=4`, write has value `w=2`, and execute has value `x=1`, while dashes `-=0`. Add the three values `r+w+x` together, with dashes equal to zero, and you get the integer mode representation for that triplet. The `setgid` bit is treated specially, and goes into a fourth leading digit for directories as value `2`.
    - `rwx = 7`
    - `rw- = 6`
    - `r-x = 5`
    - `r-- = 4`
    - `-wx = 3`
    - `-w- = 2`
    - `--x = 1`
    - `--- = 0`
    - The directory `directory` with `rwxrws---` would have mode `2770`.
    - The file `file.txt` with `rw-rw-r--` would have mode `664`.

Mode for directories can be represented with three digits, or with a special fourth leading digit.

The other components are outside the scope of this article.

## Common Use Cases

Regardless of your needs, please read all three of the following use cases in full. They will help you gain a more complete understanding of how permissions and ACLs work.

### Data Accessible to My Whole Group

This case applies for projects that involve everyone in your research group. It also applies when you don't need to spend the extra effort to restrict access to specific people.

For a brand new project directory, you can assign permissions when you create the directory using the `--mode` flag.

```shell
mkdir --mode 2770 /data/project/my-lab/project-for-all/
```

If you've created the project directory and it is still empty, you can use `chmod` to change the permissions.

```shell
chmod 2770 /data/project/my-lab/project-for-all/
```

Let's break down the meaning of the so called "mode". In our case we are using a four-digit integer to instruct the operating system who to grant access to the directory. In many online tutorials you will see three digits. Let's see what it means.

- `2` turn on the `setgid` bit, so that every subdirectory will have access from the same group.
- `7` the person who created the file (the user owner) has read, write, and execute permissions.
- `7` anyone in the same group as the folder has read, write, and execute permissions.

Each digit of our integer ranges from 0 to 7, and is the decimal number corresponding to a three-bit binary number. Zero would be `b000` in binary and 7 would be `b111`.

- `2` or `b010`, the first digit in our case, turns on a special feature for
  directories referred to as `SETGID`. When this bit is set, every newly-created
  subdirectory within this directory will inherit the group owner of the parent directory.

### Data Accessible to Part of My Group

### Read-Only Data
