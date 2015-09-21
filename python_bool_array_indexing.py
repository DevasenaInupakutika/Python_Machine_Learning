# Boolean array indexing lets you pick out arbitrary elements of an array. 
# This type of indexing is used to select elements of an array that satisfy some condition.

import numpy as np

a = np.array([[1,2], [3,4], [5,6]])

bool_idx = (a > 2)  # Shape is same as a but this statement tells if each element of a is whether > 2.

print bool_idx

# Command to print the ones that satisfy above condition

print a[bool_idx]

# Above statement can be re-written in a different concise way

print a[a > 2]
