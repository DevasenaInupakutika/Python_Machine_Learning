# Numpy arrays

# Numpy arrays can be initialized from nested Python lists, and access elements using square brackets.

import numpy as np

a = np.array([1, 2, 3])  # Create a rank 1 array
print type(a)            # Prints "<type 'numpy.ndarray'>"
print a.shape            # Prints "(3,)"
print a[0], a[1], a[2]   # Prints "1 2 3"
a[0] = 5                 # Change an element of the array
print a                  # Prints "[5, 2, 3]"

b = np.array([[1,2,3],[4,5,6]])   # Create a rank 2 array
print b.shape                     # Prints "(2, 3)"
print b[0, 0], b[0, 1], b[1, 0]   # Prints "1 2 4"


# Numpy also provides many functions to create arrays.

c = np.zeros((2,2))  # Creating an array of all zeros.
print c 


# Creating array of all ones

d = np.ones((2,2))
print d

# Create an identity matrix

e = np.eye(2)
print e

# Creating a constant array

f = np.empty((2,2))
f.fill(7)
print f

# Creating an array filled with random values

g = np.random.random((2,2))
print g

# Array Indexing

# Numpy offers several ways to index into arrays

# Slicing --> similar to Python lists, numpy arrays can be sliced. Arrays are multi-dimensional, hence, slice for each dimension of array must be mentioned.

import numpy as np

a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

# Slicing to pull out the subarray

b = a[:2, 1:3]

# A slice of an array is a view into the same data, so modifying it will modify the original array.

print a[0,1]

b[0,0] = 77

print a[0,1]


# Mixing integer indexing with slice indexing. Accessing the data in the middle row of the array. This mixing yields lower rank array, while using 
# only slices yield an array of same rank as the original array.


a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print a

row_r1 = a[1,:]   # Rank 1 view of second row of the array a
row_r2 = a[1:2, :] # Rank 2 view of the second row of array a

print row_r1, row_r1.shape
print row_r2, row_r2.shape

# We can make the same distinction when accessing columns of an array:
col_r1 = a[:, 1]
col_r2 = a[:, 1:2]
print col_r1, col_r1.shape  # Prints "[ 2  6 10] (3,)"
print col_r2, col_r2.shape  # Prints "[[ 2]

# Integer array indexing

# It allows to construct arbitrary arrays using the data from another array. 

i = np.array([[1,2],[3,4],[5,6]])

# ARRAY integer indexing
print i[[0,1,2], [0,1,0]]

# Similar command to above indexing command

print np.array([i[0,0], i[1,1], i[2,0]])

# When using integer array indexing, you can reuse the same element from the source array

print i[[0,0], [1,1]]

# Equivalent to the previous integer array indexing example

print np.array([i[0,1], i[0,1]])




