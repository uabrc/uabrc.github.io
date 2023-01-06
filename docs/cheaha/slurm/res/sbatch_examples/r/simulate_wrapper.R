# Wrapper for use of simulate() in Rscript call, e.g., with SLURM.
args <- commandArgs(trailingOnly=TRUE)

stopifnot(length(args) == 4)

seed = strtoi(args[1])
number_of_rolls = strtoi(args[2])
input_filepath_csv = args[3]
output_filepath_csv = args[4]

source("simulate.R")

simulate(seed, number_of_rolls, input_filepath_csv, output_filepath_csv)
