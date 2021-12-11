from django.db import models

# Create your models here.
class Order(models.Model):
    order_id = models.IntegerField(primary_key=True)
    order_price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return "[" + str(self.order_id) + "] Price: $" + self.order_price

class Drink(models.Model):
    DRINK_SIZE = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    ]

    DRINK_SUGAR = [
        (0, 0),
        (25, 25),
        (50, 50),
        (75, 75),
        (100, 100),
    ]
    drink_id = models.IntegerField(primary_key=True)
    order = models.ForeignKey(
        'Order',
        on_delete=models.CASCADE,
        null=True
    ) # Many to one relationship (many Drink to one Order)
    temp = models.ForeignKey(
        'Temperature',
        on_delete=models.CASCADE,
        null=True
    ) # Many to one relationship (many Drink to one Temperature)
    milk = models.ForeignKey(
        'Milk',
        on_delete=models.CASCADE,
        null=True
    ) # Many to one relationship (many Drink to one Milk)
    tea = models.ForeignKey(
        'Tea',
        on_delete=models.CASCADE,
        null=True
    ) # Many to one relationship (many Drink to one Tea)
    # flavor = models.ForeignKey(
    #     'Flavor',
    #     on_delete=models.CASCADE,
    #     null=True
    # ) # Many to one relationship (many Drink to one Flavor)
    topping = models.ForeignKey(
        'Topping',
        on_delete=models.CASCADE,
        null=True
    ) # Many to one relationship (many Drink to one Topping)
    drink_flavor = models.CharField(max_length=100)
    drink_price = models.DecimalField(max_digits=5, decimal_places=2)
    drink_size = models.CharField(max_length=100, choices=DRINK_SIZE)
    drink_sugar = models.IntegerField(choices=DRINK_SUGAR)

    def __str__(self):
        return "[" + str(self.drink_id) + "] " + self.drink_flavor

class Temperature(models.Model):
    temp_id = models.IntegerField(primary_key=True)
    temp_name = models.CharField(max_length=100, default='')
    temp_price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return "[" + str(self.temp_id) + "] " + self.temp_name

class Milk(models.Model):
    milk_id = models.IntegerField(primary_key=True)
    milk_name = models.CharField(max_length=100, default='')
    milk_price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return "[" + str(self.milk_id) + "] " + self.milk_name

class Tea(models.Model):
    tea_id = models.IntegerField(primary_key=True)
    tea_name = models.CharField(max_length=100, default='')
    tea_price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return "[" + str(self.tea_id) + "] " + self.tea_name

# class Flavor(models.Model):
#     flavor_id = models.IntegerField(primary_key=True)
#     flavor_name = models.CharField(max_length=100, default='')
#     flavor_price = models.DecimalField(max_digits=5, decimal_places=2)

#     def __str__(self):
#         return "[" + str(self.flavor_id) + "] " + self.flavor_name

class Topping(models.Model):
    topping_id = models.IntegerField(primary_key=True)
    topping_name = models.CharField(max_length=100, default='')
    topping_price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return "[" + str(self.topping_id) + "] " + self.topping_name
