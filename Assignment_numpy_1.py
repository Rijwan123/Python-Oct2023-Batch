import numpy as np

# Assignment 2D & 3D
#1. Array of ones 2D

# Creating a 2D array of ones with 3 rows and 4 columns
arr_2d= np.ones((3,4))
print(arr_2d)
"""O/P:
[[1. 1. 1. 1.]
 [1. 1. 1. 1.]
 [1. 1. 1. 1.]]"""

print("************************")


#2. Array of ones 3D

# Creating a 3D array of ones with dimensions 2x3x4
arr_3d= np.ones((2,3,4))
print(arr_3d)

"""
O/P:
[[[1. 1. 1. 1.]
  [1. 1. 1. 1.]
  [1. 1. 1. 1.]]

 [[1. 1. 1. 1.]
  [1. 1. 1. 1.]
  [1. 1. 1. 1.]]]

"""
print("***********************************************")
a= np.array([[2,3,4],
             [5,6,7],
             [8,9,10]])

print(a)
# 1. Mean : Calculate mean of all elements in the array
"""np.mean() is a NumPy function used to calculate the arithmetic mean or 
average of elements within an array along a specified axis."""
print('Mean==',np.mean(a)) # 54/9= 6
print('Mean_0==',np.mean(a, axis=0))  # (column-wise)
print('Mean_1==',np.mean(a, axis=1))  # (row-wise)
#------------------------------------------------------------------------------------
# 2. np.Std(): Calculate standard deviation of all elements in the array
"""np.std() function is useful in statistics and data analysis to
 understand the spread or dispersion of data points within arrays
or datasets along specified axes."""
print("Standard deviation==",np.std(a))
print("Standard deviation 0 ==",np.std(a,axis=0)) # (column-wise)
print("Standard deviation 1 ==",np.std(a,axis=1)) # (row-wise)
#-------------------------------------------------------------------------------------
# 3. np.min()
"""np.min() function in NumPy is used to find the minimum value within 
an array or along a specified axis."""

# Calculate the minimum value of all elements in the array
print('min==',np.min(a)) # min== 2

# Calculate the minimum value along axis 0 (column-wise)
print('min_axis_0==',np.min(a,axis=0)) # min_axis_0== [2 3 4]

# Calculate the minimum value along axis 1 (row-wise)
print('min_axis_1==',np.min(a,axis=1)) # min_axis_1== [2 5 8]
#--------------------------------------------------------------------------------------
# 4. np.max()
"""np.max() function in NumPy is used to find the maximum value 
within an array or along a specified axis."""

# Calculate the maximum value of all elements in the array
print("max_all: ",np.max(a)) # OP: max_all:  10

# Calculate the maximum value along axis 0 (column-wise)
print("max_axis_0: ",np.max(a,axis=0)) # OP: max_axis_0:  [ 8  9 10]

# Calculate the maximum value along axis 1 (row-wise)
print("max_axis_1: ",np.max(a,axis=1)) # OP: max_axis_1:  [ 4  7 10]