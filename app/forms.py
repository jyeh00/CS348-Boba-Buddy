from django.forms import ModelForm
from .models import Order, Drink


class OrderForm(ModelForm):
    class Meta:
        model = Drink
        exclude = ['drink_id', 'order']