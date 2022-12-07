from django.http import HttpResponse
from django.shortcuts import render
from scripts.select_drivers import select_driver

def index(request):
    driver = select_driver(request.GET['driver_id'])

    new_status = driver[6]
    new_active_order = driver[7]
    if driver[6] and not driver[7]:
        change_status_button = 'Уйти с линии'
        new_status = False
        new_active_order = False
    elif driver[7]:
        change_status_button = 'Завершить заказ'
        new_status = True
        new_active_order = False
    else:
        change_status_button = 'Выйти на линию'
        new_status = True
        new_active_order = False

    return render(request, "driver_profile.html", {
        'name': driver[1],
        'car_brand': driver[4],
        'car_model': driver[5],
        'car_number': driver[3],
        'is_active': driver[6],
        'change_status_button': change_status_button,
        'driver_id': driver[0],
        'new_status': new_status,
        'new_active_order': new_active_order,
        'has_active_order': driver[7]
    })
