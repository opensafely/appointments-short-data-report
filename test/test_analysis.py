import pytest

from analysis import utils


@pytest.mark.parametrize("value,rounded_value", [(6, 0), (7, 7)])
def test_round_to_multiple(value, rounded_value):
    assert utils.round_to_seven(value) == rounded_value


@pytest.mark.parametrize(
    "args,isoformat_date",
    [
        (("2022",), "2022-01-01"),
        (("2022", "9"), "2022-09-01"),
        (("2022", "10"), "2022-10-01"),
        (("2022", "9", "9"), "2022-09-09"),
        (("2022", "10", "10"), "2022-10-10"),
        (("9999", "99", "99"), "9999-99-99"),  # doesn't validate arguments
    ],
)
def test_isoformat_date(args, isoformat_date):
    assert utils.isoformat_date(*args) == isoformat_date
