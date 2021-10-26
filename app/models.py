from django.db import models

# Create your models here.

class Drink(models.Model):
    DRINK_SIZING = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    ]

    DRINK_SUGAR_LEVELS = [
        (0, 0),
        (25, 25),
        (50, 50),
        (75, 75),
        (100, 100),
    ]
    drink_id = models.IntegerField(primary_key=True)
    drink_name = models.CharField(max_length=200)
    drink_price = models.DecimalField(max_digits=5, decimal_places=2)
    drink_size = models.CharField(max_length=200, choices=DRINK_SIZING)
    drink_sugar = models.IntegerField(choices=DRINK_SUGAR_LEVELS)

    def __str__(self):
        return "[" + str(self.drink_id) + "] " + self.drink_name