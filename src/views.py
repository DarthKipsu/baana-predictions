from datetime import date, datetime, timedelta
from django.shortcuts import render
from django.template import Context, loader 
from django.http import HttpResponse

def read_predictions():
    with open('data/clean/predictions', 'rb') as data_file:
        return [line for line in data_file]

def read_actual():
    with open('data/clean/actual', 'rb') as data_file:
        return [line for line in data_file]

def prediction_objects():
    actual = read_actual()
    prediction = read_predictions()
    n = len(prediction) - 1
    start_date = date(2016, 2, 13)
    history = []
    for i in range(len(actual)):
        history.insert(0, {
            'prediction' : prediction[i],
            'actual' : actual[i],
            'date' : (start_date + timedelta(days=i)).strftime("%d. %B %Y")
            })
    today = {
            'prediction' : prediction[n-1],
            "date" : "Today, " + datetime.today().strftime("%A %d. %B")
            }
    tomorrow = {
            'prediction' : prediction[n],
            "date" : "Tomorrow, " + (datetime.today()-timedelta(days=1)).strftime("%A %d. %B")
            }
    return [history, today, tomorrow]

def index(request):
    data = prediction_objects()
    context = Context({
        'history' : data[0],
        'today' : data[1],
        'tomorrow' : data[2]
        })
    return render(request, 'index.html', context)

