import seaborn as sb
import matplotlib.pyplot as plt
import pandas as pd

titanic = sb.load_dataset('titanic')
titanic.head()

age_1 = titanic['age'].dropna()
sb.distplot(age_1, bins=30, kde=False)
plt.show()