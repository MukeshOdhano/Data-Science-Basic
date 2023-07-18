import pandas as pd

data_frame = pd.read_csv('data.csv')

# show data from top 
print(data_frame.head(2))

# show data from bottom
print(data_frame.tail(1))

# info about data
print(data_frame.info())

# descibe data ---> only work on numrical data
print(data_frame.describe())

# data cor-relation 
# co_relation = data_frame.describe().corr()
print(data_frame.corr())