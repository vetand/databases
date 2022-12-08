import json

from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render

from scripts.select_car_models import select_car_model
from scripts.insert_driver import insert_new_driver
from scripts.insert_new_car_model import insert_car_model

class RegistrationForm(forms.Form):
    brand = forms.CharField(label='Бренд', max_length=100)
    model_name = forms.CharField(label='Модель автомобиля', max_length=100)
    description = forms.CharField(label='Описание автомобиля', max_length=100)

    def clean(self):
        super(RegistrationForm, self).clean()
        return self.cleaned_data

def create_car_model(form):
    brand = form.cleaned_data.get('brand')
    model_name = form.cleaned_data.get('model_name')
    description = form.cleaned_data.get('description')

    model_id = insert_car_model(brand, model_name, description)
    if len(model_id) == 0:
      return None
    else:
      return model_id[0]

def index(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            model_id = create_car_model(form)
            if model_id is not None:
                return HttpResponseRedirect('/car-models')
    else:
        form = RegistrationForm()

    return render(request, 'car_model_creation.html', {'form': form})
