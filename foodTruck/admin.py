from django.contrib import admin
from .models import FoodTruck, Menu, User

# Register your models here.
admin.site.register(FoodTruck)
admin.site.register(Menu)
admin.site.register(User)