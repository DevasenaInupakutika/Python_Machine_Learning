from sklearn import linear_model, datasets
import numpy as np
import matplotlib.pyplot as plt

# Working with diabetes dataset as an example
#Load Train and Test datasets
#Identify feature and response variable(s) and values must be numeric and numpy arrays

#Loading diabetes dataset
diabetes=datasets.load_diabetes()

#Use only one feature
diabetes_X=diabetes.data[:,np.newaxis]
diabetes_X_temp=diabetes_X[:,:,2]

#Split the data into training and testing sets
diabetes_X_train=diabetes_X_temp[:-20]
diabetes_X_test=diabetes_X_temp[-20:]

#Split the targets into training/testing sets
diabetes_Y_train=diabetes.target[:-20]
diabetes_Y_test=diabetes.target[-20:]

#Create linear regression object
linear_regr=linear_model.LinearRegression()

#Train the model using training sets
linear_regr.fit(diabetes_X_train,diabetes_Y_train)

#The coefficients
print("Coefficients: \n", linear_regr.coef_)

#The mean-square error
print("Residual sum of squares: %0.2f" %  np.mean((linear_regr.predict(diabetes_X_test) - diabetes_Y_test) ** 2))

#Explained variance score: 1 is perfect prediction
print("Variance score: %.2f" % linear_regr.score(diabetes_X_test, diabetes_Y_test))

#Plot outputs
plt.scatter(diabetes_X_test, diabetes_Y_test, color="black")
plt.plot(diabetes_X_test, linear_regr.predict(diabetes_X_test), color="blue", linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()
