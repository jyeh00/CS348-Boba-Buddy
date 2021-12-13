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
    context = {}

    drinks = Menu.objects.all()
    context['drinks'] = drinks

    #grabs the menu item clicked button. Converts it to a string. Adds string to context dictionary.
    menu_data = request.POST.get('menu', None)
    string_menu = str(menu_data)
    context['menu'] = string_menu

    try:
        selected_menu_item = Menu.objects.get(menu_flavor=string_menu)

        print(selected_menu_item.menu_flavor)
        print(selected_menu_item.tea)
    
        form = OrderForm()
        if request.method == 'POST':
            #print('Printing POST:', request.POST)
            form = OrderForm(initial={
                        'drink_flavor': selected_menu_item.menu_flavor,
                        'tea': selected_menu_item.tea})
        
        if form.is_valid():
            form.save()
            return redirect('/')
    except Menu.DoesNotExist:
        selected_menu_item = None
        form = OrderForm()
        if request.method == 'POST':
            #print('Printing POST:', request.POST)
            form = OrderForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('/')

    context['form'] = form
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

    drinks = Menu.objects.all()
    context = {}
    context['drinks'] = drinks
    return render(request, 'apptemplates/all_drinks.html', context)

cursor1 = connection.cursor()
def popularDrinks(request):
    cursor1.execute('call top_five_drinks')
    drinks = cursor1.fetchall()
    return render(request, 'apptemplates/popular_drinks.html', {'drinks':drinks})
    #drinks = Menu.objects.all()
    #return render(request, 'apptemplates/popular_drinks.html', {'drinks':drinks})

cursor2 = connection.cursor()
def storedProcedure(request):
    cursor2.execute('call select_menu')
    result = cursor2.fetchall()
    return render(request, 'stored_proc_all.html', {'result':result})
