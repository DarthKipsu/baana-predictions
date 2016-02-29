import ml.load_data as reader
import matplotlib.pyplot as plt
import numpy as np

from datetime import date, datetime, timedelta

labels = ['Jan 2013', 'Feb 2013', 'Mar 2013', 'Apr 2013', 'May 2013', 'Jun 2013', 'Jul 2013',
        'Aug 2013', 'Sep 2013', 'Oct 2013', 'Nov 2013', 'Dec 2013',
        'Jan 2014', 'Feb 2014', 'Mar 2014', 'Apr 2014', 'May 2014', 'Jun 2014', 'Jul 2014',
        'Aug 2014', 'Sep 2014', 'Oct 2014', 'Nov 2014', 'Dec 2014',
        'Jan 2015', 'Feb 2015', 'Mar 2015', 'Apr 2015', 'May 2015', 'Jun 2015', 'Jul 2015',
        'Aug 2015', 'Sep 2015', 'Oct 2015', 'Nov 2015', 'Dec 2015']

label_locations = [15, 46, 74, 105, 135, 166, 196, 227, 258, 288, 319, 349, 380,
        411, 438, 470, 500, 531, 561, 592, 623, 653, 684, 714, 745,
        776, 804, 835, 865, 896, 926, 957, 988, 1018, 1049, 1079, 1110]

def plot_cyclists_over_weather(weather_data, cyclist_data):
    plt.clf()
    x = range(1095)
    fig = plt.figure(figsize=(13, 4), dpi=100)
    plt.plot(x, weather_data[:,0], 'c-', label='rain (mm)')
    plt.plot(x, weather_data[:,1], 'g-', label='average temperature ($^\circ$C)')
    plt.plot(x, weather_data[:,2], 'b-', label='snow (cm)')
    plt.plot(cyclist_data, 'r-', label='cyclists / 100')
    plt.xticks(label_locations, labels, rotation='vertical')
    plt.xlim([0, 1095])
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .12), ncol=4, mode='expand', borderaxespad=0)
    fig.savefig('src/static/training_data_clean.png', bbox_inches='tight')

def plot_test(predictions, actual):
    plt.clf()
    fig = plt.figure(figsize=(10, 5), dpi=100)
    ax = fig.add_subplot(111)
    ax.set_xlabel('Actual data')
    ax.set_ylabel('Predicted data')
    plt.plot(actual, predictions, 'ro')
    plt.plot([0, 7000], [0, 7000], 'k--')
    fig.savefig('plot_test.png', bbox_inches='tight')

def plot_test_multi(predictions, actual, day):
    plt.clf()
    fig = plt.figure(figsize=(10, 5), dpi=100)
    ax = fig.add_subplot(111)
    ax.set_xlabel('Actual data')
    ax.set_ylabel('Predicted data')
    labels = ['Mondays', 'Tuesdays', 'Wednesdays', 'Thursdays', 'Fridays', 'Saturdays', 'Sundays']
    for i in range(7):
        plt.plot(actual[day == i], predictions[i], 'o', label=labels[i])
    plt.plot([0, 7000], [0, 7000], 'k--')
    plt.legend(loc=2)
    fig.savefig('plot_test_multi.png', bbox_inches='tight')

def plot_test_double(predictions, actual, day, filename):
    plt.clf()
    fig = plt.figure(figsize=(10, 5), dpi=100)
    ax = fig.add_subplot(111)
    ax.set_xlabel('Actual data')
    ax.set_ylabel('Predicted data')
    labels = ['Workdays', 'Weekends']
    plt.plot(actual[day < 5], predictions[0], 'ro', label=labels[0])
    plt.plot(actual[day > 4], predictions[1], 'bo', label=labels[1])
    plt.plot([0, 7000], [0, 7000], 'k--')
    plt.legend(loc=2)
    fig.savefig(filename, bbox_inches='tight')

def plot_history(predictions, actual):
    plt.clf()
    x = range(len(predictions))
    fig = plt.figure(figsize=(13, 4), dpi=100)
    plt.plot(x, predictions, 'r-', label='predicted cyclists')
    plt.plot(x, actual, 'g-', label='actual cyclists')
    start_date = date(2016, 2, 13)
    plt.xticks(x, [(start_date + timedelta(days=i)).strftime("%d.%m.%y") for i in x], rotation='vertical')
    plt.xlim([0, len(predictions)-1])
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .12), ncol=4, mode='expand', borderaxespad=0)
    fig.savefig('src/static/history.png', bbox_inches='tight')

#plot_cyclists_over_weather(reader.rain_temp_snow(), reader.cycklists_by_hundreds())
