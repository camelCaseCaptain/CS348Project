from django.http import HttpResponse
from django.template import loader
from .models import FoodTruck, Menu, User
from django.shortcuts import render, redirect
from .forms import FoodTruckForm, UserForm, MenuForm
from django.db import connection

def search_food_trucks(request):
    search_name = request.GET.get('name', '')
    search_location = request.GET.get('location', '')
    sort_by = request.GET.get('sort', 'name')  # default sort

    query = """
        SELECT id, name, location, latitude, longitude, openTime, closeTime
        FROM foodTruck_foodtruck
        WHERE name LIKE %s AND location LIKE %s
        ORDER BY {}
    """.format(sort_by if sort_by in ['name', 'location', 'openTime', 'closeTime'] else 'name')  # prevent SQL injection on ORDER BY

    params = [f'%{search_name}%', f'%{search_location}%']

    with connection.cursor() as cursor:
        cursor.execute(query, params)
        results = cursor.fetchall()

    food_trucks = [
        {
            'id': row[0],
            'name': row[1],
            'location': row[2],
            'latitude': row[3],
            'longitude': row[4],
            'openTime': row[5],
            'closeTime': row[6],
        }
        for row in results
    ]

    return render(request, 'trucks.html', {'food_trucks': food_trucks})
def details(request, id):
    my_food_truck = FoodTruck.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'my_food_truck': my_food_truck,
    }
    return HttpResponse(template.render(context, request))

def menu(request, id):
    my_food_truck = FoodTruck.objects.get(id=id)
    menu_items = Menu.objects.all().filter(truck_id=id)
    template = loader.get_template('menu.html')
    context = {
        'menu_items': menu_items,
        'my_food_truck': my_food_truck,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def testing(request):
    mydata = FoodTruck.objects.all().values()
    template = loader.get_template('template.html')
    context = {
        'myTrucks': mydata,
    }
    return HttpResponse(template.render(context, request))

def create_truck(request):
    if request.method == 'POST':
        form = FoodTruckForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = FoodTruckForm()
    return render(request, 'create_truck.html', {'form': form})

def create_menu(request):
    if request.method == 'POST':
        form = MenuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = MenuForm()
    return render(request, 'create_menu.html', {'form': form})

def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UserForm()
    return render(request, 'create_user.html', {'form': form})

def edit_truck(request, id):
    my_food_truck = FoodTruck.objects.get(id=id)
    if request.method == 'POST':
        form = FoodTruckForm(request.POST, instance=my_food_truck)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = FoodTruckForm(instance=my_food_truck)
    return render(request, 'edit_truck.html', {'form': form})