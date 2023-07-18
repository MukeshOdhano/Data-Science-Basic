import numpy as np
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values=np.nan, strategy='mean')

data = [[12, np.nan, 34], [10, 32, np.nan], [np.nan, 12, 32]]

print(f"Origninal Data: {data}")

new_imputer = imputer.fit(data)
new_data = new_imputer.transform(data)
print(f"Imputed Data: {new_data}")