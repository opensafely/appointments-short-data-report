import contextlib
import csv

from .. import OUTPUT_DIR, utils


ACTION_OUTPUT_DIR = OUTPUT_DIR / "lead_time"


def main():
    with contextlib.ExitStack() as s:
        f_in = s.enter_context(utils.open_csv(ACTION_OUTPUT_DIR / "rows.csv"))
        f_out = s.enter_context(utils.open_csv(ACTION_OUTPUT_DIR / "results.csv", "w"))

        reader = csv.reader(f_in)
        writer = csv.writer(f_out)

        header = next(reader)
        writer.writerow(header)

        for row in reader:
            lead_time_in_days, frequency = row
            frequency = int(frequency)

            rounded_frequency = utils.round_to_seven(frequency)

            writer.writerow([lead_time_in_days, rounded_frequency])


if __name__ == "__main__":
    main()
