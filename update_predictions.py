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
    print('fmi apikey:', os.environ.get('FMIAPIKEY'))
    day = (datetime.today()+timedelta(1)).weekday()
    return lc.predict_for(forecast, day)

def tomorrows_prediction_with_past(forecast):
    past_actual = read_actual()
    forecast[3] = float(past_actual[len(past_actual)-1])
    forecast[4] = float(past_actual[len(past_actual)-7])
    day = (datetime.today()+timedelta(1)).weekday()
    return lc.predict_for(forecast, day)

def tomorrows_prediction_with_past_week(forecast):
    past_actual = read_actual()
    forecast[3] = float(past_actual[len(past_actual)-6])
    day = (datetime.today()+timedelta(1)).weekday()
    return lc.predict_for(forecast, day)

def yesterdays_cyclists():
    with open('data/clean/actual', 'rb') as cyclists:
        lines = [int(line.strip()) for line in cyclists]
        return lines[len(lines)-1]

def create_history_plot():
    actual = dl.read_actual_data()
    predictions = dl.read_predictions_data()[:len(actual)]
    weather = dl.weather_data_multiplied(100)
    plot.plot_history(predictions, actual, weather[-len(predictions):])

def update_files():
    forecast = fetch.load_tomorrows_forecast(os.environ.get('FMIAPIKEY'))
    fetch.write_to_file('data/clean/forecasts', forecast)
    write_to_file('data/clean/predictions', tomorrows_prediction_with_past(forecast))
    write_to_file('data/clean/labels', yesterdays_cyclists())
    fetch.write_to_file('data/clean/data', fetch.yesterdays_actual_weather(os.environ.get('FMIAPIKEY')))
    create_history_plot()

update_files()
#create_history_plot()

#print('forecast tomorrow:', fetch.load_tomorrows_forecast(os.environ.get('FMIAPIKEY')))
#print('prediction for tomorrow:', tomorrows_prediction_with_past_week(fetch.load_tomorrows_forecast(os.environ.get('FMIAPIKEY')))) 
#lc.testing()
