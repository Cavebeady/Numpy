#1 Numpy is a module in python used in working with arrays and is important in data analysis for studying and analysing data
#2 numpy arrays are more memory efficient, they are faster
#3 You create an array from a list by typing 'array = numpy.array([1,2,3,4,5])'
#4 1D arrays are made up of a collection of elements while 2D arrays are made up of a collection of 1D arrays
#5 You check the shape of an array by typing 'print(array.ndim)'
#6 array.size displays the total number of elements in an array, array.ndim displays the number of dimensions of the array
#7 You create an array with zeros by using the 'np.zeros()' function
#8 Broadcasting is the act of performing arithmetic operations on arrays of different shapes.
#9 
import numpy as np
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])
A = arr1 + arr2
print(A)

#10 If their shapes are not compatible, it will raise a value error and fail to broadcast them together
#11 Array slicing is the act of extracting specific elements from an array
arr1 = np.array([1, 2, 3, 4])
print(arr1[1:3])

#12 You reshape an array by using 'array.reshape()
#13 copy creates a new array with the same data while view is an array that shares the same memory
#14 mean is calculated using 'np.mean()' and standard deviation is calculated using 'np.std()'
#15 matrix multiplication is performed using np.dot(), A @ B, np.matmul(), np.multiply. The method used depends on the data or result needed
#16 np.dot() performs dot product between matrixes. that is the first row of the first matrix multiplied by the first column of the second matrix. While np.multiply() performs element wise multiplication
#17 Filtering is done using boolean indexing and comparison operators
#18 nan values can be checked using isnan() function
#19 they are both used to create arrays of values with equal spaces. np.arange specifies the step size while np.linspace specifies the number of elements in the array
#20 It is used in data analysis and machine learning