# Fill the missing value for the feature "affiliation" of the authors with "not available"
import pandas as pd
import traceback
import csv


def fill_missing_values(in_file, out_file):
    try:
        df = pd.read_csv(in_file)
        df.affiliation.fillna(value="not found", inplace=True)
        # check for "not found" values
        print(df["affiliation"].unique())
        # writing to csv file
        df.to_csv(out_file,  encoding='utf-8', index=False)

    except Exception as e:
        traceback.print_exc()


if __name__ == "__main__":
    in_file = "./output.csv"
    out_file = "./output_fillna.csv"
    fill_missing_values(in_file, out_file)