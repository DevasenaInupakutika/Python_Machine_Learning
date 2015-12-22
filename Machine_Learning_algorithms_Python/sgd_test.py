#SGD classifier usage in discriminative learning of linear classifiers. Its applied to large-scale and sparse machine learning problems often encountered in text classification and NLP.

#Shuffling the training data before fitting the model.

from sklearn.linear_model import SGDClassifier

X=[[0., 0.], [1., 1.]]
y=[0, 1]

clf = SGDClassifier(loss="hinge", penalty="l2")

# Model fitting
print("Fitting: ",clf.fit(X, y))

# Model to be used to predict new values
print("Prediction: ",clf.predict([[2.,2.]]))

# Model parameters
print("Model parameter: ",clf.coef_)

# Model intercept (aka offset or bias)
print("Model Intercept: ",clf.intercept_)

# Signed distance to the hyperplane
print("Hyperplane distance: ",clf.decision_function([[2., 2.]])) 

# Concrete loss function (logistic parameter)
clf = SGDClassifier(loss="log").fit(X, y)

print("Classifier with LR: ",clf.predict_proba([[1., 1.]])) 

print(clf)




