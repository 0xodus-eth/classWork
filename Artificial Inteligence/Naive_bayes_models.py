from sklearn import datasets
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from pandas import DataFrame
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# The dataset
iris = datasets.load_iris()
X = iris.data
Y = iris.target
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=1/3)

# Training a Gaussian Naive Bayes classifier
model = GaussianNB()
model.fit(X_train, Y_train)

# Predictions
model_predictions = model.predict(X_test)
print("\n", model_predictions)
print("\n", Y_test)

# Accuracy of prediction
accuracyScore = accuracy_score(Y_test, model_predictions)
print("\naccuracyScore is", accuracyScore)

# Creating a confusion matrix
cm = confusion_matrix(Y_test, model_predictions)
print("\nconfusion matrix", cm)