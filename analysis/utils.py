import functools


def round_to_multiple(value, multiple):
    if value < multiple:
        return 0
    return int(multiple * round(value / multiple, 0))


round_to_seven = functools.partial(round_to_multiple, multiple=7)
