import load_data as reader
import matplotlib.pyplot as plt
import numpy as np

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

plot_cyclists_over_weather(reader.rain_temp_snow(), reader.cycklists_by_hundreds())
