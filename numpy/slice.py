import numpy as np

arr_1d = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# slicing array
"""
print(arr_1d.size)
print(arr_1d)
print(arr_1d[4: ])
print(arr_1d[6: 8])
print(arr_1d[0: 9: 2])
"""

# slice 2-d array
arr_2d = np.array([
  [1, 2, 3, 4, 5], 
  [2, 4, 5, 7, 9]
])
"""
# (index of array, srtart : end)
print(arr_2d[0, 2 : ]) 
print(arr_2d[1, 2 : 5])
print(arr_2d[0, 0 : 5 : 2])
"""