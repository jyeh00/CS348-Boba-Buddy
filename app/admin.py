from django.contrib import admin
from . models import Drink, Menu, Order, Temperature, Milk, Tea, Topping

def duplicateDrink(modeladmin, request, queryset):
    for object in queryset:
        object.drink_id = None
        object.save()
duplicateDrink.short_description = "Duplicate drink"

class DrinkAdmin(admin.ModelAdmin):
    model = Drink
    # fields = ['order', 'temperature', 'milk', 'tea', 'topping', 'drink_flavor', 'drink_price', 'drink_size', 'drink_sugar']
    list_display = ['drink_flavor', 'order', 'drink_price']
    ordering = ['order']
    actions = [duplicateDrink]

def duplicateOrder(modeladmin, request, queryset):
    for object in queryset:
        object.order_id = None
        object.save()
duplicateOrder.short_description = "Duplicate order"

class OrderAdmin(admin.ModelAdmin):
    model = Drink
    list_display = ['order_id', 'order_price']
    ordering = ['order_price']
    actions = [duplicateOrder]

# Register your models here.
admin.site.register(Drink, DrinkAdmin)
admin.site.register(Menu)
admin.site.register(Order, OrderAdmin)
admin.site.register(Temperature)
admin.site.register(Milk)
admin.site.register(Tea)
admin.site.register(Topping)