import functools


def round_to_multiple(value, multiple):
    if value < multiple:
        return 0
    return int(multiple * round(value / multiple, 0))


round_to_seven = functools.partial(round_to_multiple, multiple=7)


open_csv = functools.partial(open, newline="", encoding="utf-8")


def isoformat_date(year, month="1", day="1"):
    year, month, day = [int(x) for x in [year, month, day]]
    return f"{year}-{month:02d}-{day:02d}"
