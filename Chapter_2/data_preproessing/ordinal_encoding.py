# Ordinal Encoding

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

# creating dataframe for research interest
ri_types = ('machine_learning','natural_language_processing','data_visualization', 'data_mining')
df_ri = pd.DataFrame(ri_types, columns=['research_interest'])
# label encoder instance
labelencoder = LabelEncoder()
# Assign integer value for each categorical value (each research_interest) and assign to new column
df_ri['ri_integer'] = labelencoder.fit_transform(df_ri['research_interest'])

print(df_ri)