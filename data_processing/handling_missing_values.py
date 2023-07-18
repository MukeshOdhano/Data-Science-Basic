import pandas as pd 

read_csv = pd.read_csv('data.csv') 
print(read_csv)  # read_csv.head()

print(f"\nmissing values: \n{read_csv.isnull().sum()}")

read_csv['Salary'] = read_csv['Salary'].fillna(read_csv['Salary'].mode()[0])
print(read_csv)

print(f"\nmissing values: \n{read_csv.isnull().sum()}")

read_csv['Age'] = read_csv['Age'].fillna(read_csv['Age'].mode()[0])
print(read_csv)

print(f"\nmissing values: \n{read_csv.isnull().sum()}")
