# Practical examples of `sbatch` usage

Suppose your task is to determine the statistical properties of dice rolls (pretend that you are unfamiliar with Bernoulli trials and the Central Limit Theorem). The dice have varying numbers of sides, and there are varying numbers of dice to be rolled as one unit. Because dice rolls are independent, the task is pleasingly parallel. Put another way, we can roll many dice at once, guaranteeing the same statistical properties as rolling them in sequence. To roll so many dice, we may thus use the Cheaha cluster.

Suppose you've previously written some serial code and wish to reuse it for the purpose of this larger experiment. The existing code transforms data as described in the code block below. The code is a function and does not yet have a command-line interface.

```shell
# a triplet of integers like the following...
# called:     quantity, sides   , modifier
# properties: positive, positive, negative or positive
2,6,1
# in tabletop gaming the above would be referred to as 2d6+1
# or rolling two six-sided dice, summing the rolls, and adding one.

# is transformed to a length $number_of_rolls sequence of positive integers
8,9,4,4,2,8,6,6,12,8

# based on a call like
simulate $rnd_seed $number_of_rolls $input_filepath_csv $output_filepath_csv
```

To run this code in parallel, we can use `sbatch` with the `--array` flag. To see how to translate the serial code into parallel, please click one of the links below for your preferred scientific computing language.

- [Matlab](#matlab)
- [Python](#python)
- [R](#r)

## Matlab

a

## Python

b

## R

c
