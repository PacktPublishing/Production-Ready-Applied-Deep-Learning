# Purpose of the script
# How to create bag of words from text column
# How to create term-frequency and inverse document frequency (tf-idf)
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
import traceback
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')
print(stopwords.words('english'))
# create a set of stop words
stop_words = set(stopwords.words('english'))
# list contains all the research interest from all the authors
lst_research_interest = []


def create_bow_with_nltk(in_file, out_file):
    """ Create bag-of-words for feature "research_interest" from google scholar data set and saved into
        a csv file named "output_bow.csv"
    """
    try:
        # read csv file
        df = pd.read_csv(in_file)
        # write csv file
        f = open(out_file, 'w')
        # header for the output CSV file with research interest bag-of-words
        header = "author_name,email,affiliation,coauthors_names,research_bag_of_words\n"
        f.write(header)
        # read each line in dataframe (i.e., each line of input file)
        for index, row in df.iterrows():
            curr_authorname = row['author_name']
            curr_email = row['email']
            curr_affiliation = row['affiliation']
            curr_coauthors_names = row['coauthors_names']
            curr_research_interest = str(row['research_interest']).replace("##", " ").replace("_", " ")
            lst_research_interest.append(curr_research_interest)
            # TODO: add stop words filtering before doing tokenization
            # word tokenize.
            curr_research_int_token = word_tokenize(curr_research_interest)
            curr_filtered_research = [w for w in curr_research_int_token if not w.lower() in stop_words]
            curr_line = f"{curr_authorname},{curr_email},{curr_affiliation},{curr_coauthors_names},{curr_filtered_research}"
            # write to csv file
            f.write(curr_line + "\n")
        # close the output file object
        f.close()
    except:
        traceback.print_exc()


def create_tf_idf_with_scikit():
    try:
        # create an instance for tf-idf vectorizer
        tfidf_vectorizer = TfidfVectorizer(use_idf=True)
        # use the td-idf instance to fit list of research_interest (feature)
        tfidf = tfidf_vectorizer.fit_transform(lst_research_interest)
        # tfidf[0].T.todense() provides the tf-idf dense vector calculated for the research_interest
        df = pd.DataFrame(tfidf[0].T.todense(), index=tfidf_vectorizer.get_feature_names_out(), columns=["tf-idf"])
        # sort the tf-idf calculated using `sort_values` of dataframe.
        df = df.sort_values('tf-idf', ascending=False)
        # top 30 words with highest tf-idf
        print(df.head(30))
    except:
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
##############################################################################
# Stop words
##############################################################################
# Mohamed M. E. A. Mahmoud,tntech.edu,Tennessee Tech University,nan,['security', 'and', 'privacy', 'preservation', 'for', 'wireless', 'networks']
#  To
# Mohamed M. E. A. Mahmoud,tntech.edu,Tennessee Tech University,nan,['security', 'privacy', 'preservation', 'wireless', 'networks']
# Michael Chau,business.hku.hk,University of Hong Kong,nan,['information', 'systems', 'web', 'mining', 'data', 'mining', 'it', 'education']
# To
# Michael Chau,business.hku.hk,University of Hong Kong,nan,['information', 'systems', 'web', 'mining', 'data', 'mining', 'education']
# Albert C. Gunther,wisc.edu,University of Wisconsin-Madison,Douglas Storey,['communication', 'journalism', 'mass', 'media', 'psychology', 'of', 'the', 'media', 'audience']
# To
# Albert C. Gunther,wisc.edu,University of Wisconsin-Madison,Douglas Storey,['communication', 'journalism', 'mass', 'media', 'psychology', 'media', 'audience']
##############################################################################
# Future improvement
#############################################################################
# - Also, apply the stemming concept with Bag of Words.
#   (Stemming is the process of reducing a word to word stem.)
