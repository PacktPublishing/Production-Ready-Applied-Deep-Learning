# One Hot Encoding

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

############################
# START of ORDINAL ENCODING
############################

# creating dataframe for research interest
ri_types = ('machine_learning', 'data_visualization', 'data_mining')
df_ri = pd.DataFrame(ri_types, columns=['research_interest'])
# label encoder instance
labelencoder = LabelEncoder()
# Assign integer value for each categorical value (each research_interest) and assign to new column
df_ri['ri_integer'] = labelencoder.fit_transform(df_ri['research_interest'])
############################
# END of ORDINAL ENCODING
############################

############################
# START of ONE-HOT ENCODING
############################
# one hot encoder instance
enc = OneHotEncoder(handle_unknown='ignore')
# pass either "research_interest" or "ri_integer"
enc_df = pd.DataFrame(enc.fit_transform(df_ri[['research_interest']]).toarray())
# merge
df_merge = df_ri.join(enc_df)
# print
print(df_merge)

############################
# END of ONE-HOT ENCODING
############################