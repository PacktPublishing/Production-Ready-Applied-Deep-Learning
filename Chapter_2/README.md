# Chapter_2

The first step in every Machine Learning (ML) project consists of data collection and data preparation. As a subset of ML, Deep Learning (DL) involves the same data processing processes. This chapter introduces various techniques for data collection, data cleaning, data preprocessing, as well as feature extraction. Additionally, we introduce popular tools for data visualization.

* [anaconda](https://github.com/PacktPublishing/Production-Ready-Applied-Deep-Learning/tree/main/Chapter_2/anaconda) - Anaconda Installation can be done using: 
  * Installation of Anaconda using command line [link](https://github.com/PacktPublishing/Production-Ready-Applied-Deep-Learning/blob/main/Chapter_2/anaconda/anaconda_zsh.md) (or) 
  * Anaconda GUI based Installation [link](https://github.com/PacktPublishing/Production-Ready-Applied-Deep-Learning/blob/main/Chapter_2/anaconda/anaconda_graphical_installer.md) 
* [csv_data](https://github.com/PacktPublishing/Production-Ready-Applied-Deep-Learning/tree/main/Chapter_2/csv_data) - Location of CSV DataSet (Corona and Titanic)
* [data_preprocessing](https://github.com/PacktPublishing/Production-Ready-Applied-Deep-Learning/tree/main/Chapter_2/data_preprocessing) - Python scripts for Data Preprocessing
* [dockerfiles](https://github.com/PacktPublishing/Production-Ready-Applied-Deep-Learning/tree/main/Chapter_2/dockerfiles) - Docker image files to run Jupyter. 
* [google_scholar](https://github.com/PacktPublishing/Production-Ready-Applied-Deep-Learning/tree/main/Chapter_2/google_scholar) - Data Crawling Python scripts for Google Scholar.
* [rest](https://github.com/PacktPublishing/Production-Ready-Applied-Deep-Learning/tree/main/Chapter_2/rest) - Python scripts to call rest API to collect
  JSON data, parse it, extract required features from it.
* [visualization](https://github.com/PacktPublishing/Production-Ready-Applied-Deep-Learning/tree/main/Chapter_2/visualization) - Data Visualization for plotting bar chart, pie chart etc.


# Preparing python environment

We recommend using anaconda to create virtual environments.
```python
conda create --name bookenv python=3.8
conda activate bookenv
pip install -r requirements
python <target .py script>
```

# Docker

This chapter also introduce how Docker improves development and deployment experiences. We also provide a sample docker image which you can use to run the examples in our book. Details can be found [here](https://github.com/PacktPublishing/Production-Ready-Applied-Deep-Learning/tree/main/Chapter_2/dockerfiles)
