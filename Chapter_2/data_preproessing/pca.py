# Dimentionality Reduction with PCA

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler, LabelEncoder
from tabulate import tabulate

# if set, it prints some variables
is_debug = False

# label encoder instance
labelencoder = LabelEncoder()

# read the HR data in csv format
df_features = pd.read_csv("./HR_comma_sep_2.csv")

print(tabulate(df_features.head(5), headers='keys'))

# convert sales using ordinal encoder (label encoder)

# Assign integer value for each categorical value (each research_interest) and assign to new column
df_features['sales_int'] = labelencoder.fit_transform(df_features['sales'])
df_features['salary_int'] = labelencoder.fit_transform(df_features['salary'])

df_features = df_features.drop(['sales', 'salary'], axis = 1)
# print(tabulate(df_features.head(10), headers='keys'))

df_x = df_features[["satisfaction_level", "last_evaluation", "number_project", "average_montly_hours", "time_spend_company"\
                      , "Work_accident", "promotion_last_5years", "sales_int", "salary_int"]]
df_y = df_features[["left"]]

X = df_x.iloc[:,0:9].values
y = df_y.iloc[:,0].values

if is_debug:
    print(df_features.dtypes)
    print(tabulate(df_x.head(10), headers='keys'))
    print(tabulate(df_y.head(10), headers='keys'))

# Step 1:Scale the data set
scaler = StandardScaler()
# train = scaler.fit(X)
X_std = scaler.fit_transform(X)

# Step 2: Instantiate PCA & choose minimum number of components
#         such that it covers 95% variance
pca = PCA(0.95).fit(X_std)

if is_debug:
    print(type(X_std))
    print(X_std)
    print(X_std.shape)

# cumulative explained variance (cummulative sum explained by i + 1)
plt.plot(np.cumsum(pca.explained_variance_ratio_))
# x axis and y axis scale
plt.xlim(0, 8, 1)
plt.ylim([0, 1])
# x axis and y axis labels
plt.xlabel('# components')
plt.ylabel('Cumulative explained variance')
# show the plot
plt.show()

# Observation from plot:
# -> Only first six principal components are worth to be used as new features for Machine Learning Algorithm
#    as it covers most of the variance as per the plot.
