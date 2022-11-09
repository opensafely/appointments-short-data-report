import argparse
import pathlib
import shutil
import sys


def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "input",
        type=pathlib.Path,
        help="Path to the input CSV file",
    )
    parser.add_argument(
        "--output",
        required=True,
        type=pathlib.Path,
        help="Path to the output CSV file",
    )
    return parser.parse_args(args)


def copy(f_in, f_out):
    shutil.copy(f_in, f_out)


def main():  # pragma: nocover
    args = parse_args(sys.argv[1:])
    copy(args.input, args.output)


if __name__ == "__main__":
    main()  # pragma: nocover
