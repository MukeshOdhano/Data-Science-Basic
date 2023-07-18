# n_P_m ---> numpy _ Pandas _ Matplotlib 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

december_depth=[0,120,140,0,150,80,0,10]
january_depth=[20,180,140,0,170,170,30,30]
february_depth=[0,100,100,40,100,160,40,40]

depth = np.array([december_depth, january_depth, february_depth])
# print(depth)

for month in depth:
  plt.plot(month)

plt.show()