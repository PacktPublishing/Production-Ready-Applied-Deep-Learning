# We will show to plot line chart and histogram chart using seaborn

import traceback
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from tabulate import tabulate
import numpy as np

image_format = 'eps'  # image format to save

SMALL_SIZE = 12
MEDIUM_SIZE = 15
BIGGER_SIZE = 30

plt.rc('font', size=BIGGER_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=BIGGER_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=BIGGER_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=BIGGER_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=BIGGER_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=BIGGER_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title


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
        # fig = plt.figure(figsize=(12, 6))  # figure chart with size
        # ax = fig.add_subplot(111)
        # # rotate x-axis labels
        # ax.set_xticks(np.arange(len(df_mean_sorted_top10.keys())))
        # ax.set_xticklabels(df_mean_sorted_top10.keys(), rotation=45, zorder=100)
        plt.xticks(rotation=90)
        # alternate option without .gcf
        plt.subplots_adjust(bottom=0.42)
        plt.subplots_adjust(left=0.22)
        # write to a file
        image_name = 'linediagram.eps'  # image name
        plt.savefig(image_name, format=image_format, dpi=1200)
        # show the actual plot
        # plt.show()
        ###########################
        # HISTOGRAM CHART PLOTTING
        ###########################
        sns.set(font_scale=1.2)
        # plot histogram bars with top 10 states mean distribution count of vaccine
        p = sns.displot(df_mean_sorted_top10['count_vaccine'], kde=False)

        p.set_xlabels("count_vaccine", fontsize=30)
        p.set_ylabels("count", fontsize=30)
        plt.subplots_adjust(bottom=0.22)
        # plt.set_xticks(range(len(df.keys())))
        plt.xticks(rotation=90)
        # set font for x label and y label
        # p.set_xlabels("X-Axis", fontsize=12)
        # p.set_ylabels("Y-Axis", fontsize=12)
        # write to a file
        image_name = 'histogram.eps'  # image name
        plt.savefig(image_name, format=image_format, dpi=1200)
        plt.show()

    except Exception as e:
        traceback.print_exc()


if __name__ == "__main__":
    # Moderna vaccination distribution file
    in_file = "../csv_data/data/cdc-moderna-covid-19-vaccine-distribution-by-state.csv"
    # create bag of words for feature research interest with NLTK
    seaborn_line_histogram(in_file)
