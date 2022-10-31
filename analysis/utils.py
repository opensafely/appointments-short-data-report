def round_to_multiple(value, multiple=7):
    if value < multiple:
        return 0
    return int(multiple * round(value / multiple, 0))
