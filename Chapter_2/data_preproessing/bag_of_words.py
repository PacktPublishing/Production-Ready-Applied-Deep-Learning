# Purpose of the script
# How to create bag of words from text column
# How to create term-frequency and inverse document frequency (tf-idf)
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

import nltk
from nltk.tokenize import word_tokenize
import re
import traceback
from nltk.corpus import stopwords
nltk.download('punkt')

def create_bow(in_file, out_file):
    try:
        # read csv file
        df = pd.read_csv(in_file)
        # write csv file
        f = open(out_file, 'w')

        for index, row in df.iterrows():
            curr_authorname = row['author_name']
            curr_email = row['email']
            curr_affiliation = row['affiliation']
            curr_coauthors_names = row['coauthors_names']
            curr_research_interest = str(row['research_interest']).replace("##", " ").replace("_", " ")
            TODO: add stop words filtering before doing tokenization
            curr_research_int_token =  word_tokenize(curr_research_interest)
            curr_line = f"{curr_authorname},{curr_email},{curr_affiliation},{curr_coauthors_names},{curr_research_int_token}"
            f.write(curr_line + "\n")

        f.close()
    except Exception as e:
        traceback.print_exc()


if __name__ == "__main__":
    in_file = "../google_scholar/output.csv"
    out_file = "./output_bow.csv"
    create_bow(in_file, out_file)

# Note: The output file "output_bow.csv" now has research interest text convert into bag of words.
# For example: anomaly_detection converted to ["anomaly", detection"]