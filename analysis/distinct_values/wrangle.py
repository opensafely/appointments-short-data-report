import csv

from .. import OUTPUT_DIR, utils


ACTION_OUTPUT_DIR = OUTPUT_DIR / "distinct_values"


def main():
    with utils.open_csv(ACTION_OUTPUT_DIR / "rows.csv") as f:
        rows = list(csv.DictReader(f))
    assert len(rows) == 1
    row = rows[0]

    num_distinct_values = int(row["num_distinct_values"])
    num_values = int(row["num_values"])

    is_pk = num_distinct_values == num_values
    num_distinct_values_rounded = utils.round_to_seven(num_distinct_values)
    num_values_rounded = utils.round_to_seven(num_values)

    with utils.open_csv(ACTION_OUTPUT_DIR / "results.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(
            [
                "is_pk",
                "num_distinct_values_rounded",
                "num_values_rounded",
            ]
        )
        if (num_distinct_values_rounded == 0) or (num_values_rounded == 0):
            # If we write this row, then we can infer that the unrounded values are
            # between 1 and 6.
            return
        writer.writerow(
            [
                is_pk,
                num_distinct_values_rounded,
                num_values_rounded,
            ]
        )


if __name__ == "__main__":
    main()
