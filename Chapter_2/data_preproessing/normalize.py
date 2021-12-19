import pandas as pd
import traceback

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


if __name__ == "__main__":
    in_file = "../google_scholar/output.csv"
    out_file = "./output_normalize.csv"
    # create bag of words for feature research interest with NLTK
    normalize_research(in_file, out_file)
