from django import forms
from .models import User, FoodTruck, Menu

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']

class FoodTruckForm(forms.ModelForm):
    class Meta:
        model = FoodTruck
        fields = ['name', 'location', 'latitude', 'longitude', 'openTime', 'closeTime', 'owner']

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['truck', 'item_name', 'price', 'description']