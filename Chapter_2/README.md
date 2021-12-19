# Chapter_2

This folder contains the code related to data collection, data cleaning, data preprocessing, and feature extraction.
Data collection techniques for Html and Json are explained in code [google_scholar.py](./google_scholar/google_scholar.py) 
with libraries `Beautifulsoup` and `urllib`. Feature Extraction related techniques such as bag-of-words, term frequency-inverse document frequency (tf-idf), ordinal 
encoding, one hot encoding, normalize features are explained with codes referred in [readme file](./data_preproessing/ordinal_encoding.py).

In normalize feature example, you will learn how to fill up empty values with a default value with a example from
google scholar data set. Filling up the missing values will be shown by using `fillna` method with google scholar 
data set and reddit data set. 


Run below command to install libraries

    pip install -r requirements
    