import numpy as np

import ml.load_data as dl

def print_table_headers():
    print('\\begin{table}[h!]')
    print('\\centering')
    print('\\begin{tabular}{|c|c|c|}')
    print('\\hline')
    print('Predicted change & Actual change & Absolute difference \\\\')
    print('\\hline')

def print_table_end(version_number):
    print('\\hline')
    print('\\end{tabular}')
    print('\\caption{Predicted and actual change in cyclist count between predictions with version '
            + version_number + ' classifier, as well as the absolute difference between the '
            + 'prediction and actual value.}')
    print('\\label{table:v' + version_number + '}')
    print('\\end{table}')

def print_change(predictions, actual):
    pred_change = np.array([predictions[i] - predictions[i - 1] for i in range(1, len(actual))])
    act_change = np.array([actual[i] - actual[i - 1] for i in range(1, len(actual))])
    print('v2 classifier')
    print_table_headers()
    for i in range(len(pred_change)):
        if i == 15:
            print_table_end('2b')
            print('\nv3 classifier:')
            print_table_headers()
        if (pred_change[i] < 0 and act_change[i] < 0):
            print(pred_change[i], '&', act_change[i], '&', abs(pred_change[i] - act_change[i]), '\\\\')
        elif (pred_change[i] >= 0 and act_change[i] >= 0):
            print(pred_change[i], '&', act_change[i], '&', abs(pred_change[i] - act_change[i]), '\\\\')
        else:
            print('\\rowcolor{red!10}')
            print(pred_change[i], '&', act_change[i], '&', abs(pred_change[i] - act_change[i]), '\\\\')
    print_table_end('3')

actual = dl.read_actual_data()
predictions = dl.read_predictions_data()[:len(actual)]

print_change(predictions, actual)
