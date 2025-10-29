# Practical Examples of `sbatch` Usage With the `--array` Flag and Dynamic Indices

Do you find yourself tediously creating many `sbatch` job scripts for the same type of data set? Or do you modify the same job script? Have you ever experienced frustrating errors or typos while doing this? Would you like to save time by using one script for many similar tasks? If so then please read on for how to use `sbatch` jobs with the `--array` flag.

The `--array` flag transforms an `sbatch` job script for a single task into a collection of tasks that are all scheduled simultaneously. For programmers, the `--array` flag turns a job script into a parallel loop, or a loop where each iteration is run independently and in no particular order. Naturally, this means that your tasks must be independent and similar. The most common use case is running the same software with different inputs or on different data sets. To get the most out of this page, you'll want to be familiar with [Submitting Jobs](submitting_jobs.md).

We will show how to create and use `sbatch` jobs with the `--array` flag, or `sbatch --array` jobs. We will use a simplified, practical example that parallels the process of a computational scientific experiment. The practical task we will solve is simplified to enhance focus on the structure of the problem, rather than the content of the problem. The structure of the problem is what makes `sbatch --array` jobs more or less suitable for a particular need. Specifically, whether there are many independent subtasks that all have the same structure, with similar or the same parameters.

For other examples of using Slurm and its other tools, please see [Submitting Jobs](submitting_jobs.md) and [Managing Jobs](job_management.md).

## The Task

Your task is to determine the statistical properties of dice rolls. To measure these properties, you'll need to simulate rolling the dice many times to obtain a lot of data. Because dice rolls are independent, the task of simulating many dice rolls can be subdivided into many independent subtasks, all with the same parameters. While we could simulate dice rolls one at a time, in sequence, we could instead use an `sbatch --array` job to simulate dice rolls in parallel.

Suppose you've already written some code called `simulate` that performs these simulations. The code transforms three integer inputs into an output sequence of positive integers. Based on the usual rules for tabletop role-playing game (TTRPG) dice rolling. The block below shows a sample input requesting ten rolls that are the sum of two six-sided die rolls plus one. In TTRPG notation we would write this as `2d6+1` rolled ten times. The output, in the case below, is a sequence of ten integers. Each element of the sequence falls in the possible range of the `2d6+1` die roll, which is `[3,13]`.

```shell title="Inputs, Outputs, How to Call"
# a tuplet of integers like the following...

# name       | number of rolls | quantity | sides    | modifier
# properties | positive        | positive | positive | any integer
               10              , 2        , 6        , 1

# is transformed to sequence of positive integers
8,9,4,4,3,8,6,6,13,8

# based on a call like
simulate $SEED $INPUT_FILE $OUTPUT_FILE
```

The input data takes the form of a simple text file (specifically a comma-separated value or CSV file) with four integers as described above. The upstream source of this data puts each simulation in a separate file in a separate folder. This may feel contrived for a simple example, but real experimental data is often structured with one treatment per folder, so we are using it in this example. We do not necessarily know in advance how many data folders will be present when we run the code. Sure, we could count manually and then hardcode that value, but we are trying to automate our process to avoid introducing errors and to save time in the future.

All of the above constraints must fit within the framework provided by Slurm and the `sbatch --array` job style. Now that we have a complete list of requirements, we are ready to start forming a solution.

## Building a Solution

We are going to need three components to effectively use `sbatch array` jobs given the requirements and constraints of the task.

1. The `simulate` code that transforms inputs to outputs. We are assuming this exists and will not discuss the implementation in detail here.
1. A `job` shell script file that instructs Slurm how to allocate each array job task.
1. A `main` shell script to automate the `--array` bounds and call the `job` script.

### Job Script

The job shell script file will be very much like a typical `sbatch` job script. The preamble will contain the details of Slurm scheduler instructions in the form of flags. After the preamble comes the payload, where we instruct the shell what commands need to be run within each task.

#### Preamble

The preamble of an `sbatch` job script instructs Slurm how to queue the job and what resources to allocate. Our preamble is relatively straightforward and should look familiar if you've written job scripts before. For more detailed information on what the flags mean please see [Slurm Flags](submitting_jobs.md#slurm-flags-and-environment-variables).

```shell title="job script preamble"
#! /bin/bash

#SBATCH --job-name=simulate_dice_rolls
#SBATCH --output=%x-%A-%a.log
#SBATCH --error=%x-%A-%a.log

#SBATCH --partition=express
#SBATCH --time=00:02:00

#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=1G
```

If we had a fixed number of datasets, say ten, we could add the line `#SBATCH --array=0-9` to the preamble and not require a `main.sh` file. In that case we would just use `sbatch job.sh` and be done. However, for this example, we require a dynamic upper bound on the `--array` flag, which isn't possible in the preamble of a script file.

#### Payload

For our example, the payload consists of multiple parts. We will need to extract the file from just one of the folders, ensuring that each folder is used exactly once. Dependencies must be loaded, and then the software must be run. The most interesting part will be extracting the files.

##### File Extraction

The general idea for file extraction, and generally use of the `$SLURM_ARRAY_TASK_ID` variable, is for each task to pull one unique element out of a list of possibilities. The list of possibilities can take many forms. In our case, we can use a shell array of strings constructed from a [glob pattern](../../workflow_solutions/shell.md#glob-syntax).

Other workflows may extract lines from a manifest file, or even have a computation that transforms the job array index provided by `$SLURM_ARRAY_TASK_ID` into some other number or collection of numbers.

Below is the file extraction portion of `job.sh`, along with descriptions of each line.

```shell title="Job Script Payload: File Extraction"
shopt -s nullglob

input_files=(../inputs/**/dice.csv)
INPUT_FILE=${input_files[$SLURM_ARRAY_TASK_ID]}

OUTPUT_FILE=${INPUT_FILE/inputs/outputs}
OUTPUT_FILE=${OUTPUT_FILE/dice/rolls}
```

1. The line `shopt -s nullglob` instructs `bash` to allow empty arrays created with glob patterns.

1. The line `input_files=(../inputs/**/dice.csv)` uses the glob pattern `../inputs/**/dice.csv` to create a shell array of paths to files in our dataset. Note that this shell array is distinct from the job `--array`, though they should have the same total number of elements, one for each task.

    The glob pattern can be read as:

    - `../`: move up one folder then...
    - `inputs/`: look in the folder `inputs` for...
    - `**/`: any number of nested subfolders containing...
    - `dice.csv`: the file `dice.csv`.

    The parentheses around the glob pattern instructs `bash` to create a shell array of strings from the results of the glob pattern. If there are multiple folders, each with one `dice.csv` file, then the shell array will have one entry for each of them.

    The shell array is then stored in the variable `input_files`.

1. The line `INPUT_FILE=${input_files[$SLURM_ARRAY_TASK_ID]}` extracts exactly one entry from the `input_files` shell array and puts it in the variable `INPUT_FILE`. The value of `$SLURM_ARRAY_TASK_ID` is set by the Slurm schedule when each task starts. If there are ten tasks, as with `--array=0-9`, then each task has `$SLURM_ARRAY_TASK_ID` set to a unique value from `[0,9]`. We index the shell array `input_files` using `$SLURM_ARRAY_TASK_ID` to get a single entry from the shell array. Putting it all together, each task will pull out exactly one file from the set of data folders.

    <!-- markdownlint-disable MD046 -->
    !!! tip

        Curly braces with a leading dollar sign like `${...}` are used for evaluating some modification to a variable.
    <!-- markdownlint-enable MD046 -->

1. The line `OUTPUT_FILE=${INPUT_FILE/inputs/outputs}` transforms the variable `INPUT_FILE` so that any instance of the word `inputs` is replaced with the word `outputs`. The result is assigned to the variable `OUTPUT_FILE`. The net result is the output file currently will be `../outputs/folder/dice.csv`.

1. We're not quite done setting up the output path. The line `OUTPUT_FILE=${OUTPUT_FILE/dics/rolls}` further replaces `dice` with `rolls`. The net result is `../outputs/folder/rolls.csv`.

    Lines 4 and 5 result in a parallel folder structure between inputs and outputs. It is possible to use other structures such as all outputs in the same folder, or outputs in the same folders as inputs, but we won't go into detail here on how to achieve those.

##### Running the Software

Running the software requires setting up the random number generator seed (for repeatability), loading [module](../software/modules.md) dependencies, creating the output directory, and finally running the simulation.

```shell title="Job Script Payload: Running the Software"
SEED=314159

module load ...

OUTPUT_DIRECTORY=$(dirname "$OUTPUT_FILE")
mkdir -p $OUTPUT_DIRECTORY

simulate $SEED $INPUT_FILE $OUTPUT_FILE
```

1. The line `SEED=314159` sets the variable `SEED` with a static number for repeatability. It is set in a variable, rather than directly on the final line, so future readers of the code will understand the purpose of the number.

1. The line `module load ...` is where any necessary `module load` or `conda activate` executions would go to prepare dependencies.

1. The line `OUTPUT_DIRECTORY=$(dirname "$OUTPUT_FILE")` extracts the directory part of the output file path and assigns it to the variable `OUTPUT_DIRECTORY`.

    <!-- markdownlint-disable MD046 -->
    !!! tip

        Single parentheses with a leading dollar sign like `$(...)` are used for capturing the string output of a command in a variable.
    <!-- markdownlint-enable MD046 -->

1. The line `mkdir -p $OUTPUT_DIRECTORY` creates the directory at the path stored in the variable `$OUTPUT_DIRECTORY`. The flag `-p` means the `mkdir` command will not produce an error if the directory already exists.

    <!-- markdownlint-disable MD046 -->
    !!! tip

        If you know your software will create any necessary output directories, then this and the previous line are not necessary.
    <!-- markdownlint-enable MD046 -->

1. The line `simulate $SEED $INPUT_FILE $OUTPUT_FILE` runs the simulation.

### Main Script

The `main` shell script will determine the upper bound `$N` of the `--array` flag, and then call `sbatch --array=1-$N job.sh`. It will be up to `job.sh` to determine how to use `$SLURM_ARRAY_TASK_ID`. Before we go too much further, it may be helpful to think of `sbatch --array=1-$N job.sh` as creating an indexed loop, from 1 to `$N`, and running `job.sh` on each of those index values. The important point is that the loop indices are run in parallel, so whatever happens in each call to `job.sh` must be independent. The `main.sh` file is the same for all languages and is shown in the code block below. The comments describe what each segment of code is doing.

<!-- markdownlint-disable MD046 -->
!!! important
    To effectively manage resource usage, it's essential to implement [throttling](./submitting_jobs.md#throttling-in-slurm-array-jobs) by limiting the number of concurrent jobs that can run at the same time. This helps prevent the overloading of computing resources. For example, you can limit the number of simultaneously running array jobs to 4 with the percent `%` symbol in your submission command: `sbatch --array=1-$N%4 job.sh`.
<!-- markdownlint-enable MD046 -->

```bash title="main.sh"
#! /bin/bash

shopt -s nullglob

input_files=(../inputs/**/dice.csv)

{% raw %}
FILE_COUNT=${#input_files[@]}
{% endraw %}
FILE_COUNT=$(( $FILE_COUNT - 1 ))

sbatch --array=0-$FILE_COUNT%4 job.sh
```

1. The line `#! /bin/bash` instructs the operating system what interpreter to use if called without an explicit interpreter, like `./main.sh`. It is best practice to have this line for scripts running in `bash`. Other lines are possible for other interpreters.

1. The line `shopt -s nullglob` instructs `bash` to allow empty arrays created with glob patterns.

1. The line `input_files=(../inputs/**/dice.csv)` uses the glob pattern `../inputs/**/dice.csv` to create a shell array of paths to files in our dataset. The details of this are discussed above in [File Extraction](#file-extraction).

1. The line {% raw %}`FILE_COUNT=${#input_files[@]}`{% endraw %} gets all entries from the `input_files` array using the special index `@` (for all elements), then counting them with the prefix symbol `#`.

    <!-- markdownlint-disable MD046 -->
    !!! tip

        Curly braces with a leading dollar sign like `${...}` are used for evaluating string modifications to a variable.
    <!-- markdownlint-enable MD046 -->

1. The line `FILE_COUNT=$(( FILE_COUNT - 1 ))` subtracts one from the file count. We must do this because array variables, as used in `job.sh`, start counting at zero (they are zero-indexed). So instead of counting from `1` to `10`, we would count from `0` to `9`.

    <!-- markdownlint-disable MD046 -->
    !!! tip

        Double parentheses with a leading dollar sign like `$((...))` are used for evaluating integer arithmetic to a variable.
    <!-- markdownlint-enable MD046 -->

1. The line `sbatch --array=0-$FILE_COUNT%4 job.sh` puts the array tasks in the Slurm queue using the `job.sh` script. The array of tasks runs from 0 to $FILE_COUNT as determined earlier, where %4 limits the number of simultaneous tasks to 4.

To use the script, enter the command `bash main.sh` at the terminal.

<!-- markdownlint-disable MD046 -->
!!! Note

    When writing `sbatch` scripts for job submission and managing modules, begin your script by resetting the module environment with `module reset` to ensure a clean environment for subsequent configurations. See [best practice for loading modules](../software/modules.md#best-practice-for-loading-modules) for more information.
<!-- markdownlint-enable MD046 -->

## Putting It All Together

We needed three parts to make the `sbatch --array` job work for our task. Each of these parts has been described above in some detail.

1. `simulate` program to run a simulation.
1. `job.sh` to instruct the Slurm scheduler what to do in each parallel task.
1. `main.sh` to run everything.

Executing `bash main.sh` at the terminal will first compute the number of array tasks, then call `sbatch --array` with that number of tasks on `job.sh`. The scheduler will then schedule that many jobs to be run. Each job will have a unique task ID, which will be used to access unique input files and write to unique output files. All of them will be run in parallel.

The reason `sbatch --array` could be used on our dice rolling statistics task is because dice rolls are independent. It doesn't matter when I roll the dice or whether I roll them together or sequentially, the results will be statistically the same.

Any task that can be broken into independent subtasks with similar input parameters can be used with `sbatch --array` in this way. Please feel free to use the scripts provided as a template for your own `sbatch --array` jobs, modifying them as appropriate.

### The Example Scripts

For reference, here are the full scripts.

```shell title="job.sh"
#! /bin/bash

#SBATCH --job-name=simulate_dice_rolls
#SBATCH --output=%x-%A-%a.log
#SBATCH --error=%x-%A-%a.log

#SBATCH --partition=express
#SBATCH --time=00:02:00

#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=1G

shopt -s nullglob

input_files=(../inputs/**/dice.csv)
INPUT_FILE=${input_files[$SLURM_ARRAY_TASK_ID]}

OUTPUT_FILE=${INPUT_FILE/inputs/outputs}
OUTPUT_FILE=${OUTPUT_FILE/dice/rolls}

SEED=314159

module load ...

OUTPUT_DIRECTORY=$(dirname "$OUTPUT_FILE")
mkdir -p $OUTPUT_DIRECTORY

simulate $SEED $INPUT_FILE $OUTPUT_FILE
```

```shell title="main.sh"
#! /bin/bash

shopt -s nullglob

input_files=(../inputs/**/dice.csv)

{% raw %}
FILE_COUNT=${#input_files[@]}
{% endraw %}
FILE_COUNT=$(( $FILE_COUNT - 1 ))

sbatch --array=0-$FILE_COUNT%4 job.sh
```
