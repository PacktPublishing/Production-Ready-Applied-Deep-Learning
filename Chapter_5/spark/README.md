## Introduction to Apache Spark

Apache Spark is an open-sourced data analytics engine that is used for the purpose of data processing. The most popular use case is ETL. As an introduction to Spark, we cover key concepts of Spark and provide some common Spark operations in [this notebook](./spark.ipynb).

In the provided notebook, we will
* Use Google Scholar data set in CSV file format with fields research_interest, author_name, email.
* Read research_interest field from a csv file in Google Drive into RDD and then use flatMap and reduceByKey to count occurrence for each of the research_interest with a map function. flatMap helps to apply a transformation on a RDD/DataFrame and convert into another RDD/DataFrame. reduceByKey helps to merge the values of keys (words) by applying an reducing operator (add) on it. In our example, we apply add reducing operator on word occurrence count on each document/row of a DataFrame.
* Apply Aggregate function and sort by column of a DataFrame.
* Create a new column and fill it with a User Defined Function (UDF) applied on a field in spark DataFrame.
* Convert a RDD into a DataFrame with or without schema.
* Apply filter on Spark DataFrame.
* Write spark DataFrame as a single CSV to a Google Drive Folder.
* Introduce Spark Join concept applied on DataFrames.
