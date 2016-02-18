import numpy as np

def read_weather_data():
    with open('data/clean/data', 'rb') as data_file:
        return np.array([[float(value) for value in line.split()] for line in data_file])

def read_cyclist_data():
    with open('data/clean/labels', 'rb') as data_file:
        return np.array([[float(value) for value in line.split()] for line in data_file])

def rain_temp_snow():
    return read_weather_data()[:,[0,1,2]]

def add_day_of_week(data):
    '''
    Monday = 0, Tuesday = 1, ..., Sunday = 6
    '''
    di = len(data[0])
    with_days = np.zeros((len(data), di+1))
    with_days[:,:-1] = data
    for i in range(6):
        days = with_days[i::7]
        days[:,[di]] = i+1
    return with_days

def rain_temp_snow_days():
    return add_day_of_week(read_weather_data()[:,[0,1,2]])

def cyclist_days():
    return add_day_of_week(read_cyclist_data())

def cycklists_by_hundreds():
    data = read_cyclist_data()
    return data / 100
