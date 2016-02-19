from datetime import datetime, timedelta

import data.data_fetcher as fetch
import ml.linear_classifier as lc
import os

def write_to_file(path, value):
    with open(path, 'a') as f:
        f.write("%s \n" % value)

def tomorrows_prediction():
    forecast = fetch.load_tomorrows_forecast(os.environ.get('FMIAPIKEY'))
    day = (datetime.today()+timedelta(1)).weekday()
    return lc.predict_for(forecast, day)

def yesterdays_cyclists():
    with open('data/clean/actual', 'rb') as cyclists:
        lines = [int(line.strip()) for line in cyclists]
        return lines[len(lines)-1]

def update_files():
    write_to_file('data/clean/predictions', tomorrows_prediction())
    write_to_file('data/clean/labels', yesterdays_cyclists())
    fetch.write_to_file('data/clean/data', fetch.yesterdays_actual_weather(os.environ.get('FMIAPIKEY')))

update_files()
#print('forecast tomorrow:', fetch.load_tomorrows_forecast(os.environ.get('FMIAPIKEY')))
#print('prediction for tomorrow:', tomorrows_prediction()) 
#print('prediction for 13.2:', lc.predict_for([6.3, 1.0, 0.0], 5))
#print('prediction for 14.2:', lc.predict_for([2.1, 0.6, 3.0], 6))
#print('prediction for 15.2:', lc.predict_for([-1.0, 0.4, 2.0], 0))
#print('prediction for 16.2:', lc.predict_for([-1.0, -2.0, 2.0], 1))
#print('prediction for 17.2:', lc.predict_for([-1.0, 0.5, 2.0], 2))
#print('prediction for 18.2:', lc.predict_for([2.1, 0.3, 2.0], 3))
#print('prediction for 19.2:', lc.predict_for([0.5, 0.5, 2.0], 4))
#lc.testing()
