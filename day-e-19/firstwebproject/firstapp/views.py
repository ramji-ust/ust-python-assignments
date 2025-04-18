from django.shortcuts import render
from django.http import HttpResponse

import random

# Create your views here.

def home(request):
    return HttpResponse("<h1>Welcome to my first web project!</h1>")

def info(request):
    return HttpResponse("<h1>This is the info page!</h1>")

def index(request):
    print(request.GET)  # Print the GET request parameters to the console
    dept = request.GET.get('dept')
    context = {
        'name': 'John Doe',
        'age': random.randint(1, 100),
        'dept': dept,
    }
    return render(request, 'firstapp/index.html', context )

def check_age(request):
    context = {
        'name': 'John Doe',
        'age': 25,
    }
    return render(request, 'firstapp/age-check.html', context)

def fruit_list(request):
    fruitsList = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']
    context = {
        'name': 'John Doe',
        'age': 25,
        'fruits': fruitsList,
    }
    return render(request, 'firstapp/fruit_list.html', context)


def input_form(request):
    return render(request, 'firstapp/input.html') 

def result(request):
    print(request.method)
    print(request.POST)
    if request.method == 'POST': 
        name = request.POST.get('name', 'Unknown')
        age = request.POST.get('age', 'Unkown')
        context = {
            'name': name,
            'age' : age
        }
        return render(request, 'firstapp/output.html', context)
    else:
        return render(request, 'firstapp/input.html')
    
USD_TO_INR = 83.0  # 1 USD = 83 INR

def currency_converter(request):
    result = None
    if request.method == 'POST':
        amount = float(request.POST.get('amount', 0))
        direction = request.POST.get('direction')
        
        if direction == 'USD to INR':
            result = amount * USD_TO_INR
        elif direction == 'INR to USD':
            result = amount / USD_TO_INR

    return render(request, 'firstapp/converter.html', {'result': result})

def timer_view(request):
    return render(request, 'firstapp/timer.html')