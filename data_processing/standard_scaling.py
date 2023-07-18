import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

df = pd.DataFrame({"weight": [13, 23, 15],
                   'price': [5, 15, 8.2],
                  },
                  index=['Orange', 'Apple', "Mango"])
print(df)
ax = df.plot.scatter(
  x='weight',
  y="price",
  c=['green', 'red', 'blue'],
  marker= '*',
  s=80,
  label="BEFORE SCALING",
)
plt.axhline(0, color='red', alpha=0.2)

df_1 = pd.DataFrame(scaler.fit_transform(df),
                    columns=["weight", "price"],
                    index=["Orange", "Apple", "Mango"])
print(df_1)

df_1.plot.scatter(
  x='weight',
  y='price',
  c=['green', 'red', 'blue'],
  marker = 'o',
  s=60,
  label='AFTER SCALING',
  ax = ax
)
plt.axhline(0, color='red', alpha=0.2)

plt.grid(True)
plt.show()
