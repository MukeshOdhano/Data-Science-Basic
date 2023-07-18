import numpy as np
array_1d = np.arange(10)
"""
print(f"1_d: {array_1d}")
"""
array_2d = np.arange(12).reshape(3, 4)
"""print(f"2_d: {array_2d}")"""

# -----------------------------------------------------------
december_depth=[0,120,140,0,150,80,0,10]
january_depth=[20,180,140,0,170,170,30,30]
february_depth=[0,100,100,40,100,160,40,40]

depth = np.array([december_depth, january_depth, february_depth])

mean_1 = np.mean(depth[:, 0]) # (0+20+0) / 3 
print(mean_1)

# ------------------------------------------------------------
arr_1d = np.array([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 24])
arr_2d = np.array([['a', 'b', 'c', 'c'], [1, 2, 3, 4]])

# dimension of array 
"""
print(arr_1d.ndim) 
print(arr_2d.ndim)
"""

# shape 
# --> represent the number of elements of array 
"""
print(arr_1d.shape)
print(arr_2d.shape)
"""

# ReShaping array 
# --> row x col == size of array which you want to reshap
"""
print(arr_1d.reshape(4, 3))
"""

# Flattening arrays or reshaping
# converting multidimensional array into 1-dimensional array
"""print(arr_2d.reshape(-1))"""

# access element of 2-d array
"""print(arr_2d[0, 2])"""

