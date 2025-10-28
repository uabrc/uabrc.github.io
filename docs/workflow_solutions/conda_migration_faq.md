# Conda Migration FAQ

## Why Do I Need to Stop Using Anaconda?

In April, 2020, Anaconda changed from a free-for-everyone licensing model to a free-for-some licensing model. At that time, Anaconda was free to use by individuals for personal use, non-profit organizations of any size (including UAB), and for-profit organizations up to 200 employees.

In March, 2024, Anaconda further restricted its licensing model. Anaconda is now free to use only for individuals for personal use, organizations up to 200 employees, and non-profit educational organizations when used by instructos and students in a curriculum-based course.

Use of Anaconda by UAB employees for research purposes violates the Anaconda Terms of Service.

## What Counts as "Use of Anaconda"?

- Downloading and installing Anaconda Software Distributions, including `anaconda` and `miniconda`.
- Using the `defaults`, `anaconda`, and `r` channels for packages.
- Using Anaconda Navigator.

Using the `conda` executable does not violate the terms of service, provided it is not used to access the channels listed above.

## What Is Changing on Cheaha?

We have installed Minforge as a module. To use it, **run `module load Miniforge3`** wherever you would have used `module load Anaconda3`. At a future date, we plan to archive old `Anaconda3` modules and alias the most recent on to the `Miniforge3`. When that has been completed, `module load Anaconda3` will emit a warning and then load the `Miniforge3` module instead. There will be ample notice as we roll out this change.

## Do I Need to Learn Any New Technologies?

No. However, to avoid violating the Anaconda Terms of Service, there are some actions you will need to take.

## Does This Impact My UAB Owned Laptop, Desktop, Workstation, or Server?

Yes. If you are currently using Anaconda channels or any part of the Anaconda Distribution for work purposes as an employee of UAB, then that use is in violation of the Anaconda Terms of Service, regardless of the device or computer.

To remedy this situation, you will need to transition from Anaconda to Miniforge on the affected machines. For UAB managed machines, please contact your IT representatives for assistance with this process.

## What Do I Need to Do to Avoid Violating the Terms of Service on Cheaha?

- Replace `module load Anaconda3` with `module load Miniforge3` in your current projects.
- Remove `defaults`, `anaconda`, and `r` from your channel lists in environment YAML definition files.
- Stop using the `defaults`, `anaconda`, and `r` channels in `conda` commands.
    - Avoid `-c defaults`, `-c anaconda`, and `-c r` as part of `conda install` commands.
    - Avoid `conda install defaults::$package`, `... anaconda::$package`, and `... r::$package`.
- If you encounter any errors building environments, please contact support.

## How Can I Migrate My Existing Environments?

- Export existing environments using `conda env export --name $env_name > $env_name.yml` to produce a written record of the environment packages.
- Open the `$env_name.yml` file in a text editor
- Using the text editor, remove the lines under `channels:` that read `- anaconda`, `- defaults`, and `- r`.
- Save the file.
- Reinstall the environment with Miniforge using the command `conda env create --file $env_name.yml`.

If you encounter any errors please contact support.

## How Can I Install a New Environment From a File?

<!-- markdownlint-disable MD046 -->
!!! danger

    Only install environments from files coming from sources you trust.
<!-- markdownlint-enable MD046 -->

- Obtain a copy of the file from its original source.
- Open the `$env_name.yml` file in a text editor
- Using the text editor, remove the lines under `channels:` that read `- anaconda`, `- defaults`, and `- r`.
- Save the file.
- Install the environment with Miniforge using the command `conda env create --file $env_name.yml`.

If you encounter any errors please contact support.

## What Are Good Practices to Minimize Impacts in the Future?

- Record your packages and versions in environment YAML files to make your environments reproducible. `<link>`
- Store your environment YAML files in a git repository on GitHub or GitLab to make your environments shareable and collaborative. `<link>`

## What Do I Do if I Use Anaconda Navigator to Build Environments?

At this time there does not appear to be a free-to-use alternative to Anaconda Navigator. You will need to use the terminal to create and manage environments. We have a tutorial and ample documentation covering this `<links>`. If you would like further assistance, please contact support.

## What Do All of the Terms Relating to Conda Mean?

- **Anaconda** - An ambiguous term that may refer to the company, its package distribution channels, or its software distribution. Sometimes used to reference the package management software `conda`, though this is not correct.
- **Anaconda Inc.** - The for-profit company that created the well-known ecosystem for scientific python packages. Website: <https://www.anaconda.com/>
- **Anaconda Distribution** - The system owned and maintained by Anaconda Inc. that distributes software packages through the `conda` software.
- **`anaconda` channel** - A channel for delivering packages owned and maintained by Anaconda Inc. that is subject to the Anaconda Terms of Service.
- **`conda`** - The software used to manage environments and install packages from the Anaconda Distribution.
