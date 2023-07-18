import pandas as pd

# one hot Encoding  
d_frame_1 = pd.read_csv("airport.csv")

category_1 = d_frame_1['type'].value_counts() 
type_col_1 = pd.get_dummies(d_frame_1, columns=['type'])
"""
print(d_frame_1.head())
print(category_1)
print(type_col_1.head())
"""

# Label Encoding
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

d_frame_2 = pd.read_csv('Iris.csv')
d_frame_2['Species'] = le.fit_transform(d_frame_2['Species'])

print(d_frame_2.head())