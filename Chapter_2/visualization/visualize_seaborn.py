# We will show to plot line chart and histogram chart using seaborn

import traceback
import pandas as pd
from tabulate import tabulate
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np


def seaborn_line_histogram(in_file):
    try:
        # read csv file
        df = pd.read_csv(in_file)
        # pretty print of data
        print(tabulate(df.head(10), headers='keys', tablefmt='psql'))
        # group by state and output sequence is converted to dataframe
        df_mean = df.groupby(["jurisdiction"])["_1st_dose_allocations"].mean().reset_index()
        # rename column names of data frame
        df_mean.columns = ["state", "mean_1"]
        # sort descending by # vaccine dose 1
        df_mean_sorted = df_mean.sort_values(by=['mean_1'], ascending=False)
        # top 10 stats by largest mean
        df_mean_sorted_top10 = df_mean_sorted[0:10]
        # top 10 sorted mean print
        print(tabulate(df_mean_sorted_top10, headers='keys', tablefmt='psql'))
        ####################
        # LINE CHART PLOTTING
        ####################
        # line plot
        sns.lineplot(data=df_mean_sorted_top10, x="state", y="mean_1")
        # rotate x-axis labels
        plt.xticks(rotation=90)
        # show the actual plot
        plt.show()
        ####################
        # HISTOGRAM CHART PLOTTING
        ####################
        sns.distplot(df_mean_sorted_top10['mean_1'], kde=False)
        plt.show()

    except Exception as e:
        traceback.print_exc()


if __name__ == "__main__":
    # Moderna vaccination distribution file
    in_file = "../csv_data/data/cdc-moderna-covid-19-vaccine-distribution-by-state.csv"
    # create bag of words for feature research interest with NLTK
    seaborn_line_histogram(in_file)
