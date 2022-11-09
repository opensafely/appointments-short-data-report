import shutil

from .. import OUTPUT_DIR


ACTION_OUTPUT_DIR = OUTPUT_DIR / "date_range"


def main():
    f_in = ACTION_OUTPUT_DIR / "rows.csv"
    f_out = ACTION_OUTPUT_DIR / "results.csv"
    shutil.copy(f_in, f_out)


if __name__ == "__main__":
    main()
