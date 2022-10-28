import csv
import functools

from .. import OUTPUT_DIR


ACTION_OUTPUT_DIR = OUTPUT_DIR / "distinct_values"
MULTIPLE = 7

open_csv = functools.partial(open, newline="", encoding="utf-8")


def round_to_multiple(value):
    if value < MULTIPLE:
        return 0
    return int(MULTIPLE * round(value / MULTIPLE, 0))


def main():  # pragma: nocover
    with open_csv(ACTION_OUTPUT_DIR / "rows.csv") as f:
        rows = list(csv.DictReader(f))
    assert len(rows) == 1
    row = rows[0]

    num_distinct_values = int(row["num_distinct_values"])
    num_values = int(row["num_values"])

    is_appointment_id_a_pk = num_distinct_values == num_values
    num_distinct_values_rounded = round_to_multiple(num_distinct_values)
    num_values_rounded = round_to_multiple(num_values)

    with open_csv(ACTION_OUTPUT_DIR / "results.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(
            [
                "is_appointment_id_a_pk",
                "num_distinct_values_rounded",
                "num_values_rounded",
            ]
        )
        writer.writerow(
            [
                is_appointment_id_a_pk,
                num_distinct_values_rounded,
                num_values_rounded,
            ]
        )


if __name__ == "__main__":  # pragma: nocover
    main()
