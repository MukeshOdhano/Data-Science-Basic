import seaborn as sb
import matplotlib.pyplot as plt
import pandas as pd


# boxPlot
df = sb.load_dataset("tips")
# print(df)

df.boxplot(by="day", column = ['total_bill'], grid = False)
plt.show()
