#Import libraries

from sklearn import linear_model
from sklearn.linear_model import LogisticRegression
import numpy as np
import matplotlib.pyplot as plt

#Some test data for logistic regression as an example
xmin, xmax = -5, 5
n_samples = 100

np.random.seed(0)
X=np.random.normal(size=n_samples)
Y=(X>0).astype(np.float)
X[X>0] *= 4
X += 0.3 * np.random.normal(size=n_samples)

X=X[:,np.newaxis]

#Run the classifier
clf=linear_model.LogisticRegression(C=1e5)
clf.fit(X,Y)

#Plot the result
plt.figure(1, figsize=(4,3))
plt.clf()
plt.scatter(X.ravel(), Y, color="black", zorder=20)
X_test=np.linspace(-5, 10, 300)

#Model definition

def model(x):
    return 1/(1+np.exp(-x))

loss=model(X_test*clf.coef_ + clf.intercept_).ravel()
plt.plot(X_test, loss, color="blue", linewidth=3)

ols=linear_model.LinearRegression()
ols.fit(X, Y)
plt.plot(X_test, ols.coef_*X_test + ols.intercept_, linewidth=1)
plt.axhline(.5,color='0.5')

plt.ylabel('y')
plt.xlabel('X')
plt.xticks(())
plt.yticks(())
plt.ylim(-0.25, 1.25)
plt.xlim(-4,10)

plt.show()
