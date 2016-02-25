import numpy as np

def read_weather_data():
    with open('data/clean/data', 'rb') as data_file:
        return np.array([[float(value) for value in line.split()] for line in data_file])

def read_cyclist_data():
    with open('data/clean/labels', 'rb') as data_file:
        return np.array([[float(value) for value in line.split()] for line in data_file])

def read_predictions_data():
    with open('data/clean/predictions', 'rb') as data_file:
        return np.array([int(line.strip()) for line in data_file])

def read_actual_data():
    with open('data/clean/actual', 'rb') as data_file:
        return np.array([int(line.strip()) for line in data_file])

def rain_temp_snow():
    return read_weather_data()[:,[0,1,2]]

def day_of_week():
    '''
    Monday = 0, Tuesday = 1, ..., Sunday = 6
    '''
    data_len = len(read_cyclist_data())
    days = np.zeros(data_len)
    for i in range(6):
        temp = days[i::7]
        temp[:] = i+1 # data starts from tuesday 1.1.2013
    return days

def rain_temp_snow_days():
    return add_day_of_week(read_weather_data()[:,[0,1,2]])

def cyclist_days():
    return add_day_of_week(read_cyclist_data())

def cycklists_by_hundreds():
    data = read_cyclist_data()
    return data / 100
