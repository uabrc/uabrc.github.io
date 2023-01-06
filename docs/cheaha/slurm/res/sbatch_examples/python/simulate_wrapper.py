# Wrapper for use of simulate() in python call, e.g., with SLURM.
if __name__ == "__main__":
    import argparse

    from simulate import *

    parser = argparse.ArgumentParser()
    parser.add_argument("seed", type=int)
    parser.add_argument("number_of_rolls", type=int)
    parser.add_argument("input_filepath_csv", type=PurePath)
    parser.add_argument("output_filepath_csv", type=PurePath)
    args = parser.parse_args()

    simulate(
        seed=args.seed,
        number_of_rolls=args.number_of_rolls,
        input_filepath_csv=args.input_filepath_csv,
        output_filepath_csv=args.output_filepath_csv,
    )
