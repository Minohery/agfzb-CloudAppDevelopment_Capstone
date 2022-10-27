from django.db import models
from django.utils.timezone import now


# Create your models here.

CHOICES = [
    ('sedan', 'Sedan'),
    ('suv', 'SUV'),
    ('wagon', 'WAGON')
]

class CarMake(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    def __str__(self):
        return self


class CarModel(models.Model):
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    dealer_id = models.IntegerField()
    name = models.CharField(max_length = 50)
    type = models.CharField(max_length=10, choices=CHOICES)
    year = models.DateField()
    def __str__(self):
        return self
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object


# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
