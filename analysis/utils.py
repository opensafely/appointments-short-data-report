import functools


def round_to_multiple(value, multiple):
    """Rounds value to the nearest multiple.

    If value is less than or equal to multiple, then returns multiple.
    """
    if value <= multiple:
        return multiple
    return int(multiple * round(value / multiple, 0))


round_to_seven = functools.partial(round_to_multiple, multiple=7)


open_csv = functools.partial(open, newline="", encoding="utf-8")
