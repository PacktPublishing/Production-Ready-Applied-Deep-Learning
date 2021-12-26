# (1) We will show to plot histogram using matplotlib
# (2) We read Moderna weekly vaccination data per state and then take AVERAGE of vaccination distribution per state
# (3) We will plot the weekly mean distribution data from (2) as bar chart and pie chart

import traceback
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from tabulate import tabulate


def matplotlib_pie_bar(in_file):
    try:
        # read vaccination csv file "cdc-moderna-covid-19-vaccine-distribution-by-state.csv"
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
        # convert top 10 states dataframe to dictionary
        dict_top10 = dict(zip(df_mean_sorted_top10.state, df_mean_sorted_top10.count_vaccine))
        ####################
        # PIE CHART PLOTTING
        ####################
        # colors for pie chart
        colors = ['orange', 'green', 'cyan', 'skyblue', 'yellow', 'red', 'blue', 'white', 'black', 'pink']
        # pie chart plot
        plt.pie(list(dict_top10.values()), labels=dict_top10.keys(), colors=colors, autopct='%2.1f%%', shadow=True, startangle=90)
        # set axis
        plt.axis('equal')
        # show the actual plot
        plt.show()
        ####################
        # BAR CHART PLOTTING
        ####################
        x_states = dict_top10.keys()
        y_vaccine_dist_1 = dict_top10.values()
        fig = plt.figure(figsize=(12, 6))  # figure chart with size
        ax = fig.add_subplot(111)
        # bar values filling with x-axis/y-axis values
        ax.bar(np.arange(len(x_states)), y_vaccine_dist_1, log=1)
        # x-axis ticks range and labels
        ax.set_xticks(np.arange(len(x_states)))
        ax.set_xticklabels(x_states, rotation=45, zorder=100)
        plt.show()
    except Exception as e:
        traceback.print_exc()


if __name__ == "__main__":
    in_file = "../csv_data/data/cdc-moderna-covid-19-vaccine-distribution-by-state.csv"
    # create bag of words for feature research interest with NLTK
    matplotlib_pie_bar(in_file)
