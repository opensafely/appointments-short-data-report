import contextlib
import csv

from .. import OUTPUT_DIR, utils


ACTION_OUTPUT_DIR = OUTPUT_DIR / "num_rows_by_month"


def main():
    with contextlib.ExitStack() as s:
        f_in = s.enter_context(utils.open_csv(ACTION_OUTPUT_DIR / "rows.csv"))
        f_out = s.enter_context(utils.open_csv(ACTION_OUTPUT_DIR / "results.csv", "w"))

        reader = csv.reader(f_in)
        writer = csv.writer(f_out)

        next(reader)  # skip header
        writer.writerow(["column_name", "date", "num_rows"])

        for row in reader:
            column_name, year, month, num_rows = row
            num_rows = int(num_rows)

            date = utils.isoformat_date(year, month)
            rounded_num_rows = utils.round_to_seven(num_rows)

            writer.writerow([column_name, date, rounded_num_rows])


if __name__ == "__main__":
    main()
