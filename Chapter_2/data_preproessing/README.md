# Data Preprocessing  

- Code [fill_missing.py](../google_scholar/fill_missing.py) for filling missing values.

Input File for the code:

    https://github.com/PacktPublishing/Production-Ready-Applied-Deep-Learning/blob/main/Chapter_2/google_scholar/output.csv

Output File for the code:
    
    https://github.com/PacktPublishing/Production-Ready-Applied-Deep-Learning/blob/main/Chapter_2/google_scholar/output_fillna.csv

- Code [bag_of_words_tf_idf.py](./bag_of_words_tf_idf.py) for bag-of-words. `word_tokenize` from NLTK library is applied to `research_interest`
  feature from google scholar and saved the bag-of-words as feature `research_bag_of_words` in output file 
  CSV file [output_bow.csv](./output_bow.csv). The results for `research_interest` tf-idf scores are shown in 
  image [tf-idf-result-ri.png](./images/tf-idf-result-ri.png)

- Code [bag_of_words_tf_idf.py](./bag_of_words_tf_idf.py) for Term Frequency-Inverse Document Frequency (tf-idf).

- Code [ordinal_encoding.py](./ordinal_encoding.py) for Ordinal Encoding.

    Ordinal Encoding is shown [here](./images/ordinal_encoding.png).
    `ri_integer` column in the image shows the encoded ordinal value for the feature `research_intererst`.

- Code [one_hot_encoding.py](./one_hot_encoding.py) for One Hot Encoding.

    One Hot Encoding output is shown in image [here](./images/one_hot_encoding.png).
    In the image, the one hot encoding is applied for feature `is_artificial_intelligence` which holds one of the categorical value 
    in ["yes", "no"]. One hot encoding produced two columns "0" and "1" representing "no" and "yes". "0" column shows the value 1, is_artificial_intelligence is
    "no." If "1" column shows the value 1, then is_artificial_intelligence is "yes."     

- Code [normalize.py](./normalize.py) to normalize feature `research_interest` in google scholar data set. If research interest belongs to  
  data_science or machine_learning, they are normalized to artificial_intelligence.

- Code [pca.py](./pca.py) for PCA analysis of features with HR data set from Kaggle located [here](https://www.kaggle.com/jacksonchou/hr-data-for-analytics/version/1)
 
- Code [Kaggle example](https://www.kaggle.com/pierremegret/gensim-word2vec-tutorial) related to `Word2Vec` algorithm, which uses bag-of-words kine of features for
   word similarity.