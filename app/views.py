from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection
from .models import *
from .forms import OrderForm
from .filters import OrderFilter

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the app index.")

def testpage(request):
    #response = "You're looking at the homepage."
    return render(request, 'apptemplates/projects.html')

def main(request):
    return render(request, 'apptemplates/main.html')

def dashboard(request):
    return render(request, 'apptemplates/dashboard.html')


def createOrder(request):
    form = OrderForm()
    if request.method == 'POST':
        #print('Printing POST:', request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'apptemplates/order_form.html', context)


def order_homepage(request):
    return render(request, 'apptemplates/order_home.html')

def homePage(request):
    return render(request, 'apptemplates/homepage.html')

def allDrinks(request):
    
    # if request.method == 'GET':
    #     form = request.POST
    #     if form.is_valid():
    #         form.save()
    #         return redirect('/')

    # context = {'form':form}
    return render(request, 'apptemplates/all_drinks.html')

cursor1 = connection.cursor()
def popularDrinks(request):
    cursor1.execute('call top_five_drinks')
    result = cursor1.fetchall()
    return render(request, 'stored_proc_popular.html', {'result':result})
    # drinks = Drink.objects.all()
    # return render(request, 'apptemplates/popular_drinks.html', {'drinks':drinks})

cursor2 = connection.cursor()
def storedProcedure(request):
    cursor2.execute('call select_menu')
    result = cursor2.fetchall()
    return render(request, 'stored_proc_all.html', {'result':result})
