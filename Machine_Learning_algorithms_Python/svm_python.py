# Plot different SVM classifiers in the Iris dataset

import numpy as np
import pylab as pl

from sklearn import svm, datasets

#importing iris data to play with

iris = datasets.load_iris()

X = iris.data[:, :2] # We only take first 2 features. Can be done using two-dim dataset

Y = iris.target

h = 0.02 # Step size in the mesh

#We create an instance of SVM and fit out data. We don't scale our data since we want to plot the support vectors.

C = 1.0 #SVM regularization parameter
svc = svm.SVC(kernel='linear', C=C).fit(X, Y)
rbf_svc = svm.SVC(kernel='rbf', gamma=0.7, C=C).fit(X,Y)
poly_svc = svm.SVC(kernel='poly', degree=3, C=C).fit(X,Y)
lin_svc = svm.LinearSVC(C=C).fit(X,Y)

#Create a mesh to plot in

x_min, x_max = X[:,0].min() - 1, X[:,0].max() + 1

y_min, y_max = X[:, 1].min() - 1, X[:,1].max() + 1

xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

#title for the plots

titles = ['SVC with linear kernel', 'SVC with RBF kernel', 'SVC with polynomial (degree 3) kernel', 'LinearSVC (linear kernel)']

for i, clf in enumerate((svc, rbf_svc, poly_svc, lin_svc)):
    # Plot the decision boundary. For that, we will assign a color to each
    # point in the mesh [x_min, m_max]x[y_min, y_max].
    pl.subplot(2, 2, i + 1)
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    pl.contourf(xx, yy, Z, cmap=pl.cm.Paired)
    pl.axis('off')

    # Plot also the training points
    pl.scatter(X[:, 0], X[:, 1], c=Y, cmap=pl.cm.Paired)

    pl.title(titles[i])

pl.show()

