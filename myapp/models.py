from django.db import models

class Car(models.Model):
    car_name = models.CharField(max_length=20)
    price = models.IntegerField ()
    number_plate = models.IntegerField(unique=True)

    def __str__(self):
        return f'Car ID: {self.number_plate} - {self.car_name} {self.price} '