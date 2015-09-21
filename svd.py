# SVD Word vectors in Python example program

import os
import numpy as np
import matplotlib.pyplot as plt

os.environ[ 'MPLCONFIGDIR' ] = '/tmp/'

la = np.linalg

words = ["I", "like", "enjoy", "deep", "learning", "NLP", "flying","."]

X = np.array([[0,2,1,0,0,0,0,0],[2,0,0,1,0,1,0,0],[1,0,0,0,0,0,1,0],[0,1,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,1,0,0,0,0,0,1],[0,0,1,0,0,0,0,1],[0,0,0,0,1,1,1,0]])

U,s,Vh = la.svd(X, full_matrices=False)

# Printing first 2 columns of U corresponding to the 2 biggest singular values

# plt.show()

for i in xrange(len(words)):
    plt.text(U[i,0],U[i,1],words[i])

plt.show()
