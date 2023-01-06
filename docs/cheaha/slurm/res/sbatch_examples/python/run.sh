#! /bin/bash

#SBATCH --job-name=roll_dice_python
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

output_files=("${input_files[@]/inputs/outputs}")
output_files=("${output_files[@]/dice/rolls_py}")
OUTPUT_FILE=${output_files[$SLURM_ARRAY_TASK_ID]}

SEED=314159
ROLL_COUNT=20

module load Anaconda3
conda activate base

mkdir -p $(dirname "$OUTPUT_FILE")
python simulate_wrapper.py "$SEED" "$ROLL_COUNT" "$INPUT_FILE" "$OUTPUT_FILE"
