import argparse
import contextlib
import csv
import pathlib
import sys

from .. import utils


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
    parser.add_argument(
        "--column-names",
        required=True,
        action="extend",
        nargs="+",
        help="The names of the columns to round. Separate them with a space",
    )
    return parser.parse_args(args)


def round_columns(path_in, path_out, column_names):
    with contextlib.ExitStack() as stack:
        f_in = stack.enter_context(utils.open_csv(path_in))
        f_out = stack.enter_context(utils.open_csv(path_out, "w"))

        reader = csv.reader(f_in)
        writer = csv.writer(f_out)

        header = next(reader)
        writer.writerow(header)

        header_idx = {h: i for h, i in zip(header, range(len(header)))}
        for row in reader:
            for column_name in column_names:
                i = header_idx[column_name]
                # FIXME: We assume an integer is to be rounded to seven
                row[i] = str(utils.round_to_seven(int(row[i])))
            writer.writerow(row)
    # coverage complains if we don't have an explicit return statement that isn't
    # covered.
    return  # pragma: nocover


def main():  # pragma: nocover
    args = parse_args(sys.argv[1:])
    round_columns(args.input, args.output, args.column_names)


if __name__ == "__main__":
    main()  # pragma: nocover
