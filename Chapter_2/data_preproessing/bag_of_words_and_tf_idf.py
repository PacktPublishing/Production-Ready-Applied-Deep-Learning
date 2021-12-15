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

# list contains all the research interest from all the authors
lst_research_interest = []

def create_bow_with_nltk(in_file, out_file):
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
            lst_research_interest.append(curr_research_interest)
            # TODO: add stop words filtering before doing tokenization
            curr_research_int_token =  word_tokenize(curr_research_interest)
            curr_line = f"{curr_authorname},{curr_email},{curr_affiliation},{curr_coauthors_names},{curr_research_int_token}"
            f.write(curr_line + "\n")

        f.close()
    except Exception as e:
        traceback.print_exc()


def create_tf_idf_with_scikit():
    try:
        tfidf_vectorizer = TfidfVectorizer(use_idf=True)
        tfidf = tfidf_vectorizer.fit_transform(lst_research_interest)
        df = pd.DataFrame(tfidf[0].T.todense(), index=tfidf_vectorizer.get_feature_names(), columns=["tf-idf"])
        df = df.sort_values('tf-idf', ascending=False)
        # top 30 words with highest tf-idf
        print (df.head(30))

    except Exception as e:
        traceback.print_exc()


if __name__ == "__main__":
    in_file = "../google_scholar/output.csv"
    out_file = "./output_bow.csv"
    # create bag of words for feature research interest with NLTK
    create_bow_with_nltk(in_file, out_file)
    # create tf-idf for feature research interest with SCIKIT-LEARN
    create_tf_idf_with_scikit()

##############################################################################
# Note: The output file "output_bow.csv" now has research interest text convert into bag of words.
# For example: anomaly_detection converted to ["anomaly", detection"]

# Term Frequency
# Term frequency (TF) is how often a word appears in a document, divided by how many words there are.
# TF(t) = (Number of times term t appears in a document) / (Total number of terms in the document)

# Inverse document frequency
# Term frequency is how common a word is, inverse document frequency (IDF) is how unique or rare a word is.
# IDF(t) = log_e(Total number of documents / Number of documents with term t in it)