# Chapter_2

This folder contains the code related to data collection, data cleaning, data preprocessing, and feature extraction.
Data collection techniques for Html and Json are explained in code [google_scholar.py](./google_scholar/google_scholar.py) 
with libraries `Beautifulsoup` and `urllib`. Feature Extraction related techniques such as bag-of-words, term frequency-inverse document frequency (tf-idf), ordinal 
encoding, one hot encoding, normalize features are explained with codes referred in [readme file](./data_preproessing/ordinal_encoding.py).

In normalize feature example, you will learn how to fill up empty values with a default value with a example from
google scholar data set. Filling up the missing values will be shown by using `fillna` method with google scholar 
data set. Similarly, in case of empty `text` feature in reddit data set, use custom function to fill it up in script 
[get_rest_api_data.py](./rest/get_rest_api_data.py). 


# How to start 

We recomend using anaconda to create virtual environments. 
```python
conda create --name bookenv python=3.8
conda activate bookenv
```
Run below command to install needed libraries:
```python
pip install -r requirements
```

# Docker 

In the final sections of this chapter, we discuss docker based environment for Data Science. 
The instructions how to set up docker are presented.
To use dockerfile prepared by us please follow instructions located [here](https://github.com/PacktPublishing/Production-Ready-Applied-Deep-Learning/tree/main/Chapter_2/dockerfiles/jupyter-notebook)


