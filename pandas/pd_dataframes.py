# pandas data frame
"""
is a 2 dimensional data structure, 
like 2-d arrayo 
or table with rows and columns
"""

import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

data_frame = pd.DataFrame(data)

print(data_frame)
print(data_frame.loc[1])
