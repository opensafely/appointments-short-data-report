import pytest

from analysis.distinct_values import wrangle


@pytest.mark.parametrize("value,rounded_value", [(6, 0), (7, 7)])
def test_round_to_multiple(value, rounded_value):
    assert wrangle.round_to_multiple(value) == rounded_value
