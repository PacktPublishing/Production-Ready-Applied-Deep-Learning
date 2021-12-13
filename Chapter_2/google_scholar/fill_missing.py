# Fill the missing value for the feature "affiliation" of the authors with "not available"
import pandas as pd
import traceback
import csv

def fill_missing_values(in_file):
    try:
        df = pd.read_csv(in_file)
        print(df)
        df.affiliation.fillna(value="not found", inplace=True)
        # readCSV = csv.DictReader(in_file, delimiter=',')
        # for row in readCSV:
        #     print(row)

    except Exception as e:
        traceback.print_exc()


if __name__ == "__main__":
    in_file = "./output.csv"
    fill_missing_values(in_file)