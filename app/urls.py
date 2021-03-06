from django.urls import path

from . import views
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import include



urlpatterns = [
    path('', views.main),
    path('test/', views.testpage),
    path('admin/', admin.site.urls),
    path('dashboard/', views.dashboard),
    path('create_order/', views.createOrder, name="create_order"),
    path('order_home/', views.order_homepage, name='order_home'),
    path('order_home/popular_drinks/', views.popularDrinks, name='popular_drinks'),
    path('stored_proc_all/', views.storedProcedure, name="stored_proc_all"),
    # path('stored_proc_popular/', views.popularDrinks, name="stored_proc_popular"),
    path('order_home/all_drinks/', views.allDrinks, name="all_drinks"),
    path('order_lookup/', views.orderLookup, name = "order_lookup"),
    path('order_drink_list/', views.orderDrinkList, name="order_drink_list"),
    path('checkout/', views.checkout, name="checkout"),
    path('checkout/order_checkout/', views.orderCheckout, name="checkout"),
    path('qr_code/', include('qr_code.urls', namespace="qr_code")),
]

SERVE_QR_CODE_IMAGE_PATH = 'qr-code-image/'