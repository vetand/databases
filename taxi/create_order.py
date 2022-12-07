import json
import random
import re

from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render

from scripts.select_drivers import select_active_drivers
from scripts.insert_driver import insert_new_driver
from scripts.create_order import create_taxi_order

default_data = {
    'pointA_lat': '55.7',
    'pointA_lon': '37.8',
    'pointB_lat': '55.8',
    'pointB_lon': '37.6',
}

class OrderCreationForm(forms.Form):
    pointA_lat = forms.CharField(label='Точка А, широта', max_length=100, empty_value='55.5')
    pointA_lon = forms.CharField(label='Точка А, долгота', max_length=100)
    pointB_lat = forms.CharField(label='Точка B, широта', max_length=100)
    pointB_lon = forms.CharField(label='Точка B, долгота', max_length=100)

    def clean(self):
        super(OrderCreationForm, self).clean()

        if re.match(r'^-?\d+(?:\.\d+)$', self.cleaned_data.get('pointA_lat')) is None:
            self._errors['pointA_lat'] = self.error_class([
                'Неправильная широта точки А'
            ])
            return

        if re.match(r'^-?\d+(?:\.\d+)$', self.cleaned_data.get('pointA_lon')) is None:
            self._errors['pointA_lon'] = self.error_class([
                'Неправильная долгота точки А'
            ])
            return

        if re.match(r'^-?\d+(?:\.\d+)$', self.cleaned_data.get('pointB_lat')) is None:
            self._errors['pointB_lat'] = self.error_class([
                'Неправильная широта точки B'
            ])
            return

        if re.match(r'^-?\d+(?:\.\d+)$', self.cleaned_data.get('pointB_lon')) is None:
            self._errors['pointB_lon'] = self.error_class([
                'Неправильная долгота точки B'
            ])
            return

        return self.cleaned_data

def create_order(form):
    active_drivers = select_active_drivers(1)
    order_id = None
    if len(active_drivers) > 0:
        driver = active_drivers[0]
        order_id = create_taxi_order( \
            form.cleaned_data.get('pointA_lat'), \
            form.cleaned_data.get('pointA_lon'), \
            form.cleaned_data.get('pointB_lat'), \
            form.cleaned_data.get('pointB_lon'), \
            round(random.uniform(100, 500), 1), \
            driver[0],
    ) 
    return order_id

def create_order_handle(request):
    if request.method == 'POST':
        form = OrderCreationForm(request.POST)
        if form.is_valid():
            order_id = create_order(form)
            if order_id is not None:
                return HttpResponseRedirect('/park')

    form = OrderCreationForm(default_data)
    return render(request, 'order_creation.html', {'form': form})
