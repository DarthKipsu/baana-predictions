import numpy as np

def read_weather_data():
    with open('data/clean/data', 'rb') as data_file:
        return np.array([[float(value) for value in line.split()] for line in data_file])

def read_cyclist_data():
    with open('data/clean/labels', 'rb') as data_file:
        return np.array([[int(value) for value in line.split()] for line in data_file])
