from django.forms import ModelForm
from .models import Order, Drink


class OrderForm(ModelForm):
    class Meta:
        model = Drink
        exclude = ['drink_id', 'order', 'drink_price']

class LookupForm(ModelForm):
    class Meta:
        model = Order
        exclude = ['order_price']
