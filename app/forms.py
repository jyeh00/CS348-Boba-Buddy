from django.forms import ModelForm
from .models import Order, Drink


class OrderForm(ModelForm):
    class Meta:
        model = Drink

        exclude = ['drink_id', 'order', 'drink_flavor', 'drink_price', 'tea']

class LookupForm(ModelForm):
    class Meta:
        model = Order
        exclude = ['order_price']
