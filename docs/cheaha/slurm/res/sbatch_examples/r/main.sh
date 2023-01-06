#! /bin/bash

shopt -s nullglob
input_files=(../inputs/**/dice.csv)
FILE_COUNT=${#input_files[@]}
FILE_COUNT=$(( $FILE_COUNT - 1 ))

sbatch --array=0-$FILE_COUNT run.sh
