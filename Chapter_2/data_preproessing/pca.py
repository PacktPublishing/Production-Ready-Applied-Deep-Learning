# Dimentionality Reduction with PCA

import pandas as pd
from tabulate import tabulate
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np

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

print(df_features.dtypes)
print(tabulate(df_x.head(10), headers='keys'))
print(tabulate(df_y.head(10), headers='keys'))

# Step 1:Scale the data set
scaler = StandardScaler()

# train = scaler.fit(X)
X_std = scaler.fit_transform(X)

pca = PCA(n_components=7).fit(X_std)

print(type(X_std))
print(X_std)
print(X_std.shape)

# cumulative explained variance
plt.plot(np.cumsum(pca.explained_variance_ratio_))
plt.xlim(0,8,1)
plt.ylim([0, 1])
plt.xlabel('# components')
plt.ylabel('Cumulative explained variance')
plt.show()

print("Only first six principal components are worth to be used for features to Machine Learning Algorithm")