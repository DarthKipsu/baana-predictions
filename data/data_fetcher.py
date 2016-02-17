from bs4 import BeautifulSoup
from datetime import datetime, timedelta

import numpy as np
import os
import urllib.request

def rain_and_temp(apikey):
    '''
    The amountount of rain and average temperature for 24 hour time span 12 hours from now.
    '''
    xml = urllib.request.urlopen("http://data.fmi.fi/fmi-apikey/" + apikey + "/wfs?request=getFeature&place=kaisaniemi,Helsinki&storedquery_id=fmi::forecast::hirlam::surface::point::timevaluepair")
    soup = BeautifulSoup(xml, 'lxml-xml')
    for feature in soup.find_all('MeasurementTimeseries'):
        feature_name = feature.get('gml:id')
        if feature_name == "mts-1-1-Temperature":
            i = 0
            temp = np.zeros(24)
            for value_tag in feature.find_all('value'):
                if i >= 12:
                    temp[i-12] = float(value_tag.string)
                i += 1
        if feature_name == "mts-1-1-Precipitation1h":
            i, rain = 0, 0
            for value_tag in feature.find_all('value'):
                if i >= 12:
                    rain += float(value_tag.string)
                i += 1
    return rain, np.sum(temp)/24, -1, np.min(temp), np.max(temp)

def snow_from_yesterday(apikey):
    '''
    No forecast for snow is available so taking todays value.
    '''
    xml = urllib.request.urlopen("http://data.fmi.fi/fmi-apikey/" + apikey + "/wfs?request=getFeature&place=kaisaniemi,Helsinki&storedquery_id=fmi::observations::weather::daily::timevaluepair&starttime=" + datetime.today().strftime("%Y-%m-%d") + "T00:00:00Z&endtime=" + datetime.today().strftime("%Y-%m-%d") + "T00:00:00Z")
    soup = BeautifulSoup(xml, 'lxml-xml')
    for feature in soup.find_all('MeasurementTimeseries'):
        feature_name = feature.get('gml:id')
        if feature_name == "obs-obs-1-1-snow":
            for value_tag in feature.find_all('value'):
                return float(value_tag.string)

def load_tomorrows_forecast(apikey):
    rain_temp = np.array(rain_and_temp(apikey))
    rain_temp[2] = snow_from_yesterday(apikey)
    return list(map(lambda x: '%.1f' % round(x, 1), rain_temp))

def yesterdays_actual_weather(apikey):
    yesterday = (datetime.today()-timedelta(days=1)).strftime("%Y-%m-%d")
    xml = urllib.request.urlopen("http://data.fmi.fi/fmi-apikey/" + apikey + "/wfs?request=getFeature&place=kaisaniemi,Helsinki&storedquery_id=fmi::observations::weather::daily::timevaluepair&starttime=" + yesterday + "T00:00:00Z&endtime=" + yesterday + "T00:00:00Z")
    soup = BeautifulSoup(xml, 'lxml-xml')
    data = []
    i = 0
    for feature in soup.find_all('MeasurementTimeseries'):
        j = 0
        feature_name = feature.get('gml:id')
        for value_tag in feature.find_all('value'):
            value = float(value_tag.string)
            if value != value:
                value = -1.0
            data.append(value)
            j += 1
        i += 1
    return data

def write_to_file(path, data):
    """
    Takes a path to file and data to br written as an array.
    Appends the file with the given data.
    """
    with open(path, 'a') as f:
        for column in data:
            f.write("%s " % column)
        f.write('\n')

def update_data_file():
    write_to_file('clean/data', yesterdays_actual_weather(os.environ.get('FMIAPIKEY')))

print(yesterdays_actual_weather(os.environ.get('FMIAPIKEY')))
print(load_tomorrows_forecast(os.environ.get('FMIAPIKEY')))
