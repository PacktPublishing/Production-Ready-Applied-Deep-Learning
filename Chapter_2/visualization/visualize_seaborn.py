# We will show to plot line chart and histogram chart using seaborn

import traceback
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from tabulate import tabulate


def seaborn_line_histogram(in_file):
    try:
        # read csv file
        df = pd.read_csv(in_file)
        # pretty print of data
        print(tabulate(df.head(10), headers='keys', tablefmt='psql'))
        # group by state and output sequence is converted to dataframe
        df_mean = df.groupby(["jurisdiction"])["_1st_dose_allocations"].mean().reset_index()
        # rename column names of data frame
        df_mean.columns = ["state", "count_vaccine"]
        # sort descending by # vaccine dose 1
        df_mean_sorted = df_mean.sort_values(by=['count_vaccine'], ascending=False)
        # top 10 stats by largest mean
        df_mean_sorted_top10 = df_mean_sorted[0:10]
        # top 10 sorted mean print
        print(tabulate(df_mean_sorted_top10, headers='keys', tablefmt='psql'))
        ####################
        # LINE CHART PLOTTING
        ####################
        # line plot
        sns.lineplot(data=df_mean_sorted_top10, x="state", y="count_vaccine")
        # rotate x-axis labels
        plt.xticks(rotation=90)
        # show the actual plot
        plt.show()
        ###########################
        # HISTOGRAM CHART PLOTTING
        ###########################
        # plot histogram bars with top 10 states mean distribution count of vaccine
        sns.displot(df_mean_sorted_top10['count_vaccine'], kde=False)
        plt.show()

    except Exception as e:
        traceback.print_exc()


if __name__ == "__main__":
    # Moderna vaccination distribution file
    in_file = "../csv_data/data/cdc-moderna-covid-19-vaccine-distribution-by-state.csv"
    # create bag of words for feature research interest with NLTK
    seaborn_line_histogram(in_file)
