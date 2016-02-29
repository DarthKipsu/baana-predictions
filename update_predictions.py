from datetime import datetime, timedelta

import matplotlib
matplotlib.use('Agg')

import data.data_fetcher as fetch
import ml.linear_classifier as lc
import ml.load_data as dl
import ml.plotter as plot
import os

def read_actual():
    with open('data/clean/actual', 'rb') as data_file:
        return [line for line in data_file]

def write_to_file(path, value):
    with open(path, 'a') as f:
        f.write("%s \n" % value)

def tomorrows_prediction():
    forecast = fetch.load_tomorrows_forecast(os.environ.get('FMIAPIKEY'))
    day = (datetime.today()+timedelta(1)).weekday()
    return lc.predict_for(forecast, day)

def tomorrows_prediction_with_past():
    forecast = fetch.load_tomorrows_forecast(os.environ.get('FMIAPIKEY'))
    past_actual = read_actual()
    forecast[3] = float(past_actual[len(past_actual)-1])
    forecast[4] = float(past_actual[len(past_actual)-7])
    day = (datetime.today()+timedelta(1)).weekday()
    return lc.predict_for(forecast, day)

def yesterdays_cyclists():
    with open('data/clean/actual', 'rb') as cyclists:
        lines = [int(line.strip()) for line in cyclists]
        return lines[len(lines)-1]

def create_history_plot():
    actual = dl.read_actual_data()
    predictions = dl.read_predictions_data()[:len(actual)]
    plot.plot_history(predictions, actual)

def update_files():
    write_to_file('data/clean/predictions', tomorrows_prediction_with_past())
    write_to_file('data/clean/labels', yesterdays_cyclists())
    fetch.write_to_file('data/clean/data', fetch.yesterdays_actual_weather(os.environ.get('FMIAPIKEY')))
    create_history_plot()

update_files()

#create_history_plot()
#print('forecast tomorrow:', fetch.load_tomorrows_forecast(os.environ.get('FMIAPIKEY')))
#print('prediction for tomorrow:', tomorrows_prediction_with_past()) 
#print('prediction for 13.2:', lc.predict_for([6.3, 1.0, 0.0], 5))
#print('prediction for 14.2:', lc.predict_for([2.1, 0.6, 3.0], 6))
#print('prediction for 15.2:', lc.predict_for([-1.0, 0.4, 2.0], 0))
#print('prediction for 16.2:', lc.predict_for([-1.0, -2.0, 2.0], 1))
#print('prediction for 17.2:', lc.predict_for([-1.0, 0.5, 2.0], 2))
#print('prediction for 18.2:', lc.predict_for([2.1, 0.3, 2.0], 3))
#print('prediction for 19.2:', lc.predict_for([0.5, 0.5, 2.0], 4))
#lc.testing()
