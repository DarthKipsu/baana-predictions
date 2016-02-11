from sklearn import linear_model
from sklearn.utils import shuffle

import load_data as reader
import numpy as np
import plotter as plot

X, y = shuffle(reader.rain_temp_snow(), reader.read_cyclist_data().ravel(), random_state=0)

trainingX= X[:900]
trainingY = y[:900]

testX = X[900:]
testY = y[900:]

clf = linear_model.LinearRegression()
clf.fit(trainingX, trainingY)

test_predictions = clf.predict(testX)
test_predictions[test_predictions < 0] = 0
print(test_predictions)
print("Error:", 1 - test_predictions.sum() / testY.ravel().sum())

plot.plot_test(test_predictions, testY)
