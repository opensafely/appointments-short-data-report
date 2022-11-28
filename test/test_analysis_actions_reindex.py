import csv
import pathlib

import pandas
import pytest

from analysis.actions import reindex


def test_parse_args():
    args = reindex.parse_args(
        [
            "--output",
            "output.csv",
            "--date-column-name",
            "date",
            "input.csv",
            "--group-by-column-names",
            "organisation_id",
        ]
    )
    assert args.output == pathlib.Path("output.csv")
    assert args.input == pathlib.Path("input.csv")
    assert args.date_column_name == "date"
    assert args.group_by_column_names == ["organisation_id"]


@pytest.fixture
def input_csv(tmp_path):
    f_out = tmp_path / "input.csv"
    f_out.write_text("organisation_id,date,num_values\n1,2022-01-01,1\n")
    return f_out


def test_read_csv(input_csv):
    columns, data_frame = reindex.read_csv(input_csv, "date", ["organisation_id"])
    assert columns == ["organisation_id", "date", "num_values"]
    assert len(data_frame) == 1  # number of rows
    assert len(data_frame.columns) == 1
    assert data_frame.index.nlevels == 2
    assert data_frame.index.get_level_values(0).name == "date"
    assert data_frame.index.get_level_values(1).name == "organisation_id"


@pytest.fixture
def input_data_frame():
    return pandas.Series(
        1,
        index=pandas.DatetimeIndex(["2022-01-01", "2022-04-01"], name="date"),
        name="organisation_id",
    ).to_frame()


def test_reindex(input_data_frame):
    reindexed_data_frame = reindex.reindex(input_data_frame, "date")
    organisation_id = reindexed_data_frame["organisation_id"]  # for brevity
    assert len(organisation_id) == 4
    assert all(organisation_id.loc[["2022-01", "2022-04"]] == 1)
    assert all(organisation_id.loc[["2022-02", "2022-03"]].isna())


def test_write_csv(tmp_path, input_data_frame):
    # arrange
    path_out = tmp_path / "output.csv"

    # act
    reindex.write_csv(input_data_frame, ["organisation_id", "date"], path_out)

    # assert
    with path_out.open(newline="") as f:
        rows = list(csv.reader(f))
        assert len(rows) == 3
        assert rows[0] == ["organisation_id", "date"]
        assert rows[1] == ["1", "2022-01-01"]
        assert rows[2] == ["1", "2022-04-01"]
