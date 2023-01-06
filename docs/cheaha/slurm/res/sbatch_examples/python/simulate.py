import csv
import random
from pathlib import PurePath
from typing import List


def simulate(
    seed: int,
    number_of_rolls: int,
    input_filepath_csv: PurePath,
    output_filepath_csv: PurePath,
) -> None:
    """
    Takes a collection of dice rolls from csv input filepath. Each dice roll is
    of the form (quantity,size,modifier) and results in a size-sided die rolled
    quantity times, the results summed up, and modifier added to the total. For
    each dice roll the process is repeated number_of_rolls times to create a
    list of rolls (for downstream statistics).

    The net result is a list of lists of integers, which is then written to a
    csv output filepath, one list of integers per line.

    Seed is provided for reproducibility of random simulation.

    One roll of a set of dice, plus modifier, is set to 1 if less than 1.
    """
    # Read input values
    with open(input_filepath_csv) as f:
        reader = csv.reader(f, delimiter=",")
        rows = [row for row in reader]

    # Simulate
    roll_data: List[List[int]] = []
    for row in rows:
        random.seed(seed)

        quantity = int(row[0])
        size = int(row[1])
        modifier = int(row[2])

        # actually perform the rolls
        rolls = simulate_many_dice_rolls(
            number_of_rolls=number_of_rolls,
            quantity=quantity,
            size=size,
            modifier=modifier,
        )

        roll_data.append(rolls)

    # Write output values
    with open(output_filepath_csv, "w") as f:
        writer = csv.writer(f, delimiter=",")
        writer.writerows(roll_data)


def simulate_many_dice_rolls(
    number_of_rolls: int, quantity: int, size: int, modifier: int
) -> List[int]:
    """
    Simulate rolling a set of dice many times.

    Returns a list of integers, one per roll.
    """
    values: List[int] = []
    for _ in range(number_of_rolls):
        value = roll_dice(quantity=quantity, size=size, modifier=modifier)
        values.append(value)
    return values


def roll_dice(quantity: int, size: int, modifier: int) -> int:
    """
    Simulate rolling a set of dice one time.

    If quantity is 2, size is 6 and modifier is 3, then in tabletop gaming
    notation this would roll 2d6+3, or two 6-sided dice and add 3 to the result.

    The sum of rolls plus modifier is returned. The returned value is set to 1
    if it would be less than 1.
    """
    rolls: List[int] = []
    for _ in range(quantity):
        roll = random.randint(1, size)
        rolls.append(roll)
    total = sum(rolls) + modifier
    total = max(1, total)  # roll may not be negative
    return total
