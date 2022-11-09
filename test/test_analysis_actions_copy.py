import pathlib

from analysis.actions import copy


def test_parse_args():
    args = copy.parse_args(["--output", "output.csv", "input.csv"])
    assert args.input == pathlib.Path("input.csv")
    assert args.output == pathlib.Path("output.csv")


def test_copy(tmp_path):
    # arrange
    f_in = tmp_path / "input.csv"
    f_in.write_text("col_a,col_b\n1,1\n")
    assert f_in.exists()
    f_out = tmp_path / "output.csv"
    assert not f_out.exists()

    # act
    copy.copy(f_in, f_out)

    # assert
    assert f_in.read_text() == f_out.read_text()
