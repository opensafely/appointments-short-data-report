import pytest

from analysis import utils


@pytest.mark.parametrize("value,rounded_value", [(6, 0), (7, 7)])
def test_round_to_multiple(value, rounded_value):
    assert utils.round_to_multiple(value) == rounded_value
