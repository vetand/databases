import json

from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render

from scripts.select_car_models import select_car_model
from scripts.insert_driver import insert_new_driver

class RegistrationForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=100)
    car_number = forms.CharField(label='Номер автомобиля', max_length=100)
    car_brand = forms.CharField(label='Бренд автомобиля', max_length=100)
    car_model = forms.CharField(label='Модель автомобиля', max_length=100)

    def clean(self):
        super(RegistrationForm, self).clean()

        name = self.cleaned_data.get('name')
        car_number = self.cleaned_data.get('car_number')
        car_brand = self.cleaned_data.get('car_brand')
        car_model = self.cleaned_data.get('car_model')

        car_model_id = select_car_model(car_brand, car_model)
        if car_model_id is None:
            self._errors['car_brand'] = self.error_class([
                'Неправильная марка или модель автомобиля'
            ])
        return self.cleaned_data

def register_driver(form):
    name = form.cleaned_data.get('name')
    car_number = form.cleaned_data.get('car_number')
    car_brand = form.cleaned_data.get('car_brand')
    car_model = form.cleaned_data.get('car_model')

    car_model_id = select_car_model(car_brand, car_model)
    return insert_new_driver(car_model_id, name, car_number)

def get_driver(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            driver_id = register_driver(form)
            return HttpResponseRedirect('/driver-profile?driver_id={}'.format(driver_id))
    else:
        form = RegistrationForm()

    return render(request, 'driver_registration.html', {'form': form})
