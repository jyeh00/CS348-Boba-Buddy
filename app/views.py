from django.shortcuts import render, redirect
from django.http import HttpResponse
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
def popularDrinks(request):
    drinks = Drink.objects.all()
    return render(request, 'apptemplates/popular_drinks.html', {'drinks':drinks})

# def storedProcedure(request):
