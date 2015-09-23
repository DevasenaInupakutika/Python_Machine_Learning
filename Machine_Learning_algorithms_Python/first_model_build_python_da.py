# Simple logistic regression model in Python

# Below are the steps involved:

# Import the required libraries
# Read the data
# Explore and clean the data
# Build logistic regression model
# Interpret the results

# Using already cleaned dataset (Iris) as an example and build a model on this dataset and will look at ways to split them into test and train datasets at a later point

import numpy as np
import matplotlib as plt

from sklearn import datasets
from sklearn import metrics
from sklearn import linear_model
from sklearn.linear_model import LogisticRegression

#Reading the dataset into an instance called dataset

dataset = datasets.load_iris()

lgr_model = linear_model.LogisticRegression()
# Feature names of a dataset are the data variables to predict
lgr_model.fit(dataset.data, dataset.target)

expected = dataset.target

predicted = lgr_model.predict(dataset.data)

print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))








