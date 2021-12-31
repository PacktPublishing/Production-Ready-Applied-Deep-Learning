# Dimentionality Reduction with PCA

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler, LabelEncoder
from tabulate import tabulate

# if set, it prints some variables
is_debug = False
# set this to true if you want to plot Principal Components visualization in browser using pyplot
is_plot = False

# label encoder instance
labelencoder = LabelEncoder()

# read the HR data in csv format
df_features = pd.read_csv("./HR_comma_sep_2.csv")
# make a copy of the original data before any manipulation
df_features_original = df_features.copy()

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
# returns numpy array
X = df_x.iloc[:, 0:9].values
y = df_y.iloc[:, 0].values

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
################################
# VISUALIZE cumulative variance
################################
# cumulative explained variance (cumulative sum explained by i + 1)
plt.plot(np.cumsum(pca.explained_variance_ratio_))
# x axis and y axis scale
plt.xlim(0, 8, 1)
plt.ylim([0, 1])
# x axis and y axis labels
plt.xlabel('# components')
plt.ylabel('Cumulative explained variance')
# show the plot
plt.show()
##############################################################################################
# VISUALIZE PCA COMPONENTS AS MATRIX. SET VARIABLE is_plot = TRUE FOR BELOW PLOT TO WORD
##############################################################################################
if is_plot:
    features = ['satisfaction_level', 'last_evaluation', 'number_project', 'average_montly_hours', 'time_spend_company'
        ,'Work_accident', 'promotion_last_5years', 'sales_int', 'salary_int']
    # create a PCA instance without any variance need
    pca = PCA()
    # generate principal components
    components = pca.fit_transform(df_features[features])
    # labels for the plot
    labels = {
        str(i): f"PC {i+1} ({var:.1f}%)"
        for i, var in enumerate(pca.explained_variance_ratio_ * 100)
    }
    # plot scatter matrix
    fig = px.scatter_matrix(
        components,
        labels=labels,
        dimensions=range(2),
        color=df_features["left"]
    )
    # mark diagonal as invisible
    fig.update_traces(diagonal_visible=False)
    fig.show()
##############################
# Observation from plot:
##############################
# -> Only first two principal components are worth to be used as new features for Machine Learning Algorithm
#    as it covers most of the variance as per the plot.
