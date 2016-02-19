from datetime import datetime, timedelta

import data.data_fetcher as fetch
import ml.linear_classifier as lc
import os

def tomorrows_cyclists():
    forecast = fetch.load_tomorrows_forecast(os.environ.get('FMIAPIKEY'))
    day = (datetime.today()+timedelta(1)).weekday()
    return lc.predict_for(forecast, day)

print('prediction for tomorrow:', tomorrows_cyclists()) 
