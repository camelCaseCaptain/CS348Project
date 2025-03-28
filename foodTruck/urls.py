from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('trucks/', views.search_food_trucks, name='search_food_trucks'),
    path('trucks/details/<int:id>', views.details, name='details'),
    path('menu/<int:id>', views.menu, name='menu'),
    path('create_menu/', views.create_menu, name='create_menu'),
    path('create_truck/', views.create_truck, name='create_truck'),
    path('create_user/', views.create_user, name='create_user'),
    path('edit_truck/<int:id>', views.edit_truck, name='edit_truck'),
]