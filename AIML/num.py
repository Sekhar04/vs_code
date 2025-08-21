# 1)	create a NumPy array from a Python list?
import numpy as np
array = np.array([1, 2, 3, 4, 5])
print("NumPy Array from Python List:")
print(array)

# 2)	calculate the mean of a NumPy array?
array_mean = np.mean(array)
print("Mean of the NumPy Array:")
print(array_mean)

# 3)	How do you reshape a NumPy array?
array_reshaped = array.reshape(5, 1)
print("Reshaped NumPy Array:")
print(array_reshaped)

# 4)	Create a NumPy array from a python tuple
tuple = (6, 7, 8, 9, 10)
array_from_tuple = np.array(tuple)
print("NumPy Array from Python Tuple:")
print(array_from_tuple)
# 5)	Finding third and fourth elements from the following array and add them
array2 = np.array([10, 20, 30, 40, 50])
third_element = array2[2]
fourth_element = array2[3]
sum_elements = third_element + fourth_element
print("Sum of third and fourth elements from the array:")
print(sum_elements)

