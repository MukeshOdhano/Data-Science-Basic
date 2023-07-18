import seaborn as sb
import matplotlib.pyplot as plt
import pandas as pd


data = sb.load_dataset('mpg')
data.head()

sb.regplot(x = 'mpg', y='acceleration', data = data)
plt.show()