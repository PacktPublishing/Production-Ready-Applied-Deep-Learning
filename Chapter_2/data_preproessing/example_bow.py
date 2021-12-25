# example_bow.py
# Simple example of Bag-of-Words
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from tabulate import tabulate
document_1 = "This is a great place to do holiday shopping"
document_2 = "This is a good place to eat food"
document_3 = "One of the best place to relax is home"
# 1-gram
count_vector = CountVectorizer(ngram_range=(1, 1), stop_words='english')
# transform the documents
count_fit = count_vector.fit_transform([document_1, document_2, document_3])
# create dataframe
df = pd.DataFrame(count_fit.toarray(), columns=count_vector.get_feature_names_out())
print(tabulate(df, headers="keys", tablefmt="psql"))