import pandas as pd

array_1 = [1, 3, 7, 18]
dict_1 = {'Mukesh': 22, "Subhash": 31, "Jeevan": 33, "Love": 35}

list_1 = pd.Series(array_1)
list_2 = pd.Series(dict_1)

print(list_1)
print(list_2)