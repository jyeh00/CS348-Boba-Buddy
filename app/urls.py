from django.urls import path

from . import views
from django.contrib import admin
from django.urls import include, path



urlpatterns = [
    path('', views.index, name='index'),
    path('test/', views.testpage),
    path('main/', views.main),
    path('dashboard/', views.dashboard)
]
