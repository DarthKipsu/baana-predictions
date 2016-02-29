from sklearn import linear_model
from sklearn.metrics import mean_squared_error
from sklearn.utils import shuffle

import ml.load_data as reader
import numpy as np
import ml.plotter as plot

def version1():
    X, y = shuffle(reader.rain_temp_snow()[7:], reader.read_cyclist_data().ravel()[7:], random_state=0)
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
            reader.rain_temp_snow()[7:],
            reader.read_cyclist_data().ravel()[7:],
            reader.day_of_week()[7:],
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

def version2b():
    X, y, days = shuffle(
            reader.rain_temp_snow()[7:],
            reader.read_cyclist_data().ravel()[7:],
            reader.day_of_week()[7:],
            random_state=0)
    n = int((len(X)/10)*9)

    trainingX= X[:n]
    trainingY = y[:n]
    trainingD = days[:n]
    
    testX = X[n:]
    testY = y[n:]
    testD = days[n:]

    clf = np.array([linear_model.LinearRegression() for i in range(2)])
    clf[0].fit(trainingX[trainingD < 5], trainingY[trainingD < 5])
    clf[1].fit(trainingX[trainingD > 4], trainingY[trainingD > 4])
    return clf, testX, testY, testD

def version3():
    X, y, days = shuffle(
            reader.rain_temp_snow_prev(),
            reader.read_cyclist_data().ravel()[7:],
            reader.day_of_week()[7:],
            random_state=0)
    n = int((len(X)/10)*9)

    trainingX= X[:n]
    trainingY = y[:n]
    trainingD = days[:n]
    
    testX = X[n:]
    testY = y[n:]
    testD = days[n:]

    clf = np.array([linear_model.LinearRegression() for i in range(2)])
    clf[0].fit(trainingX[trainingD < 5], trainingY[trainingD < 5])
    clf[1].fit(trainingX[trainingD > 4], trainingY[trainingD > 4])
    return clf, testX, testY, testD

def predict_with_v2(forecast, day):
    X, y, days = reader.rain_temp_snow(), reader.read_cyclist_data().ravel(), reader.day_of_week()

    clf = np.array([linear_model.LinearRegression() for i in range(7)])
    for i in range(7):
        clf[i].fit(X[days == i], y[days == i])
    prediction = clf[day].predict([forecast])
    prediction[prediction < 0] = 0
    return prediction

def predict_with_v2b(forecast, day):
    X, y, days = reader.rain_temp_snow(), reader.read_cyclist_data().ravel(), reader.day_of_week()

    clf = np.array([linear_model.LinearRegression() for i in range(2)])
    clf[0].fit(X[days < 5], y[days < 5])
    clf[1].fit(X[days > 4], y[days > 4])
    if day < 5:
        prediction = clf[0].predict([forecast])
    else:
        prediction = clf[1].predict([forecast])
    prediction[prediction < 0] = 0
    return prediction

def predict_with_v3(forecast, day):
    X, y, days = reader.rain_temp_snow_prev(), reader.read_cyclist_data().ravel()[7:], reader.day_of_week()[7:]

    clf = np.array([linear_model.LinearRegression() for i in range(2)])
    clf[0].fit(X[days < 5], y[days < 5])
    clf[1].fit(X[days > 4], y[days > 4])
    if day < 5:
        prediction = clf[0].predict([forecast])
    else:
        prediction = clf[1].predict([forecast])
    prediction[prediction < 0] = 0
    return prediction

def test_classifier1(clf, testX, testY):
    test_predictions = clf.predict(testX)
    test_predictions[test_predictions < 0] = 0
    print("root-mean-square error v1:", mean_squared_error(testY, test_predictions) ** (1/2.0))
    plot.plot_test(test_predictions, testY)

def test_classifier2(clf, testX, testY, testD):
    predictions = []
    errors = []
    for i in range(7):
        pred = clf[i].predict(testX[testD == i])
        pred[pred < 0] = 0
        errors.append(mean_squared_error(pred, testY[testD == i]))
        predictions.append(pred)
    print('root-mean-square error v2:', (np.sum(np.array(errors))/len(errors)) ** (1/2.0))
    plot.plot_test_multi(predictions, testY, testD)

def test_classifier2b(clf, testX, testY, testD, name):
    pred0 = clf[0].predict(testX[testD < 5])
    pred0[pred0 < 0] = 0
    errors0 = mean_squared_error(pred0, testY[testD < 5])

    pred1 = clf[1].predict(testX[testD > 4])
    pred1[pred1 < 0] = 0
    errors1 = mean_squared_error(pred1, testY[testD > 4])

    print('root-mean-square error v2b & 3:', ((errors0 + errors1)/2) ** (1/2.0))
    plot.plot_test_double([pred0, pred1], testY, testD, name)

def testing():
    clf, testX, testY = version1()
    print("testisetin koko", len(testX))
    test_classifier1(clf, testX, testY)
    
    clf, testX, testY, testD = version2()
    test_classifier2(clf, testX, testY, testD)
    
    clf, testX, testY, testD = version2b()
    test_classifier2b(clf, testX, testY, testD, 'plot_test_double.png')
    
    clf, testX, testY, testD = version3()
    test_classifier2b(clf, testX, testY, testD, 'plot_test_prev.png')

def predict_for(forecast, day):
    return int(predict_with_v3(forecast, day))
    
