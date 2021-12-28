import pandas as pd
import traceback
from tabulate import tabulate
from sklearn.preprocessing import MinMaxScaler
import numpy as np


# dictionary that helps to normalize
dict_norm = {"data_science": "artificial_intelligence",
             "machine_learning": "artificial_intelligence"
            }


def join_strings(conc, curr, dict_norm):
        """ Normalize based on dictionary
            :param conc: concatenate
            :param curr: current string
            :return:
        """
        try:
            if len(conc) == 0:
                if curr in dict_norm:
                    return dict_norm[curr]
                else:
                    return curr
            else:
                if curr in dict_norm:
                    return conc + "##" + dict_norm[curr]  # used ## as delimiter for concatenating research interest
                else:
                    return conc + "##" + curr # used ## as delimiter for concatenating research interest
        except Exception as e:
            traceback.print_exc()


def normalize_research(in_file, out_file):
    try:
        # read csv file
        df = pd.read_csv(in_file)
        # write csv file
        f = open(out_file, 'w')
        # header for output file
        header = "author_name,email,affiliation,coauthors_names,research_interest_normalized"
        for index, row in df.iterrows():
            # split delimiter ## to get individual research_interest like machine_learning or data_science
            curr_research_interest = str(row['research_interest']).split("##")
            conc_research_norm = ""  # reset
            for i in curr_research_interest:
                # normalize research interest
                if i in dict_norm:
                    conc_research_norm = join_strings(conc_research_norm, i, dict_norm)
                else:
                    conc_research_norm = join_strings(conc_research_norm, i, dict_norm)
            curr_authorname = row['author_name']
            curr_email = row['email']
            curr_affiliation = row['affiliation']
            curr_coauthors_names = row['coauthors_names']
            # split the normalized research interest, then remove duplicates post normalization
            set_research_norm = set(list(conc_research_norm.split("##")))
            conc_research_norm_str = "##".join(set_research_norm)
            # put together
            curr_line = f"{curr_authorname},{curr_email},{curr_affiliation},{curr_coauthors_names},{conc_research_norm_str}"
            f.write(curr_line + "\n")

        f.close()
    except Exception as e:
        traceback.print_exc()


def normalize_numeric(in_file_numeric):
    """ Normalize numeric values in range 0 to 1 with example from Corona Vaccine data set
    """
    df_in = pd.read_csv(in_file_numeric)
    # Step 1: calculate state-wise mean number for weekly corora vaccine distribution
    df = df_in.groupby("jurisdiction")["_1st_dose_allocations"]\
        .mean().to_frame("mean_vaccine_count").reset_index()
    print("State-wise Mean calculated for # vaccine distributed weekly")
    print(tabulate(df.head(10), tablefmt="psql", headers="keys"))
    # Step 2: calculate normalized mean vaccine count
    df["norm_vaccine_count"] = df["mean_vaccine_count"] / df["mean_vaccine_count"].max()
    print(tabulate(df.head(10), tablefmt="psql", headers="keys"))


if __name__ == "__main__":
    # Input file of Google Scholar
    in_file = "../google_scholar/output.csv"
    # Output file for normalized research_interest field in Google Scholar
    out_file = "./output_normalize.csv"
    # create bag of words for feature research interest with NLTK
    # normalize_research(in_file)

    # Input file for weekly corona vaccine distribution
    in_file_corona = "../csv_data/data/cdc-moderna-covid-19-vaccine-distribution-by-state.csv"
    normalize_numeric(in_file_corona)
