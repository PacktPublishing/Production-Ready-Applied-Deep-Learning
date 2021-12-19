# Fill the missing value for the feature "affiliation" of the authors with "not available"
import pandas as pd
import traceback
import csv


def fill_missing_values(in_file, out_file):
    try:
        # Read the Google Scholar crawled & saved CSV file "output.csv"
        df = pd.read_csv(in_file)
        # Fill out the empty "affiliation" with "na"
        df.affiliation.fillna(value="na", inplace=True)
        # verify for "na" values which is the default for missing
        print(df["affiliation"].unique())
        # writing to csv file
        df.to_csv(out_file,  encoding='utf-8', index=False)
    except:
        traceback.print_exc()


if __name__ == "__main__":
    # crawled google scholar file
    in_file = "./output.csv"
    out_file = "./output_fillna.csv"
    fill_missing_values(in_file, out_file)