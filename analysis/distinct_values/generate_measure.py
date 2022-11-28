import csv

from .. import OUTPUT_DIR, utils


def main():
    measure_id = "prop_distinct_values_by_organisation_id"
    p_in = OUTPUT_DIR / "distinct_values" / "reindexed_rows.csv"
    p_out = OUTPUT_DIR / "distinct_values" / f"measure_{measure_id}.csv"
    with utils.open_csv(p_in) as f_in, utils.open_csv(p_out, "w") as f_out:
        reader = csv.reader(f_in)
        writer = csv.writer(f_out)

        # header
        next(reader)
        writer.writerow(["Organisation_ID", "value", "date"])

        for row in reader:
            organisation_id, booked_date, num_distinct_values, num_values = row
            num_distinct_values = int(num_distinct_values)
            num_values = int(num_values)
            prop_distinct_values = num_distinct_values / num_values
            writer.writerow([organisation_id, prop_distinct_values, booked_date])


if __name__ == "__main__":
    main()
