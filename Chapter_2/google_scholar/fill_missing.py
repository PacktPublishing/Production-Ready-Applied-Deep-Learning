# Fill the missing value for the feature "affiliation" of the authors with "not available"
import pandas as pd
import traceback


def fill_missing_values(in_file):
    try:
        df = pd.read_csv(in_file)
        print(df)
        # df.a.fillna(value=0, inplace=True)

    except Exception as e:
        traceback.print_exc()


if __init__ == "__main__":
    in_file = "./output.csv"
    fill_missing_values(in_file)