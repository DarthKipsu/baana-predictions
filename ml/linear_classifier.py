from sklearn import linear_model
from sklearn.metrics import mean_squared_error
from sklearn.utils import shuffle

import load_data as reader
import numpy as np
import plotter as plot

def version1():
    X, y = shuffle(reader.rain_temp_snow(), reader.read_cyclist_data().ravel(), random_state=0)
    n = int((len(X)/10)*9)

    trainingX= X[:n]
    trainingY = y[:n]
    
    testX = X[n:]
    testY = y[n:]
    
    clf = linear_model.LinearRegression()
    clf.fit(trainingX, trainingY)
    return clf, testX, testY

def version2():
    X, y, days = shuffle(
            reader.rain_temp_snow(),
            reader.read_cyclist_data().ravel(),
            reader.day_of_week(),
            random_state=0)
    n = int((len(X)/10)*9)

    trainingX= X[:n]
    trainingY = y[:n]
    trainingD = days[:n]
    
    testX = X[n:]
    testY = y[n:]
    testD = days[n:]

    clf = np.array([linear_model.LinearRegression() for i in range(7)])
    for i in range(7):
        clf[i].fit(trainingX[trainingD == i], trainingY[trainingD == i])
    return clf, testX, testY, testD

def test_classifier1(clf, testX, testY):
    test_predictions = clf.predict(testX)
    test_predictions[test_predictions < 0] = 0
    print("Error:", mean_squared_error(test_predictions, testY))
    plot.plot_test(test_predictions, testY)

def test_classifier2(clf, testX, testY, testD):
    predictions = []
    errors = []
    for i in range(7):
        pred = clf[i].predict(testX[testD == i])
        pred[pred < 0] = 0
        errors.append(mean_squared_error(pred, testY[testD == i]))
        predictions.append(pred)
    print(np.sum(np.array(errors)))
    plot.plot_test_multi(predictions, testY, testD)

clf, testX, testY = version1()
test_classifier1(clf, testX, testY)

clf, testX, testY, testD = version2()
test_classifier2(clf, testX, testY, testD)
