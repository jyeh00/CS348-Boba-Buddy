from django.urls import path

from . import views
from django.contrib import admin
from django.urls import include, path



urlpatterns = [
    path('', views.main),
    path('test/', views.testpage),
    path('admin/', admin.site.urls),
    path('dashboard/', views.dashboard),
    path('create_order/', views.createOrder, name="create_order"),
    path('order_home/', views.order_homepage, name='order_home'),
    path('all_drinks/', views.allDrinks, name="all_drinks")
]
