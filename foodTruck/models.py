from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)  # Store hashed in real apps

    def __str__(self):
        return self.name

class FoodTruck(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=7, decimal_places=5)
    longitude = models.DecimalField(max_digits=8, decimal_places=5)
    openTime = models.DecimalField(max_digits=2, decimal_places=0)
    closeTime = models.DecimalField(max_digits=2, decimal_places=0)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    indexes = [
        models.Index(fields=['name', 'location']),
    ]

    def __str__(self):
        return self.name

class Menu(models.Model):
    truck = models.ForeignKey(FoodTruck, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return f"{self.item_name} - ${self.price}"
