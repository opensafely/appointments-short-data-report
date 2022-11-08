import pathlib

import pytest

from analysis.actions import round as round_columns


def test_parse_args():
    args = round_columns.parse_args(
        [
            "--output",
            "output.csv",
            "input.csv",
            "--column-names",  # this argument must come last, because nargs="+"
            "col_a",
            "col_b",
        ]
    )
    assert args.output == pathlib.Path("output.csv")
    assert args.input == pathlib.Path("input.csv")
    assert args.column_names == ["col_a", "col_b"]


@pytest.fixture
def unrounded_csv(tmp_path):
    f_out = tmp_path / "unrounded.csv"
    f_out.write_text("col_a,col_b,col_c\n1,1,8\n")
    return f_out


def test_round_columns(unrounded_csv):
    rounded_csv = unrounded_csv.parent / "rounded.csv"
    round_columns.round_columns(unrounded_csv, rounded_csv, ["col_a", "col_b"])
    assert rounded_csv.read_text() == "col_a,col_b,col_c\n7,7,8\n"
