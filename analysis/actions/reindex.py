import argparse
import pathlib
import sys

import pandas


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
        "--date-column-name",
        required=True,
        help="The name of the date column to resample",
    )
    parser.add_argument(
        "--group-by-column-names",
        required=True,
        action="extend",
        nargs="+",
        help="The names of the columns to group by. Separate them with a space",
    )
    return parser.parse_args(args)


def read_csv(path_in, date_column_name, group_by_column_names):
    data_frame = pandas.read_csv(path_in, parse_dates=[date_column_name])
    columns = list(data_frame.columns)
    data_frame = data_frame.set_index([date_column_name] + group_by_column_names)
    return columns, data_frame


def reindex(data_frame, date_column_name):
    level_values = data_frame.index.get_level_values(date_column_name)
    full_date_range = pandas.date_range(
        start=level_values.min(),
        end=level_values.max(),
        freq="MS",  # month start
        normalize=True,  # normalize start and end to midnight
        name=date_column_name,
    )
    return data_frame.reindex(index=full_date_range, level=date_column_name)


def write_csv(data_frame, columns, path_out):
    data_frame.reset_index().loc[:, columns].to_csv(path_out, index=False)


def main():  # pragma: nocover
    args = parse_args(sys.argv[1:])
    path_in = args.input
    path_out = args.output
    date_column_name = args.date_column_name
    group_by_column_names = args.group_by_column_names

    columns, data_frame = read_csv(path_in, date_column_name, group_by_column_names)
    reindexed_data_frame = reindex(data_frame, date_column_name)
    del data_frame
    write_csv(reindexed_data_frame, columns, path_out)


if __name__ == "__main__":
    main()  # pragma: nocover
