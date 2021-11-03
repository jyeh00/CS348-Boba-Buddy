from django.shortcuts import render
from django.http import HttpResponse


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
    return render(request, 'accounts/order_form.html', context)
