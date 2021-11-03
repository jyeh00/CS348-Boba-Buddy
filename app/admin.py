from django.contrib import admin
from . models import Drink, Order, Temperature, Milk, Tea, Flavor, Topping

# Register your models here.
admin.site.register(Drink)
admin.site.register(Order)
admin.site.register(Temperature)
admin.site.register(Milk)
admin.site.register(Tea)
admin.site.register(Flavor)
admin.site.register(Topping)