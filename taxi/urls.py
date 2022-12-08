"""taxi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import parks
from . import driver_registration
from . import driver_profile
from . import change_driver_status
from . import create_order
from . import car_models
from . import create_car_model

urlpatterns = [
    path("admin/", admin.site.urls),
    path('park/', parks.index, name='park_admin'),
    path('driver-registration/', driver_registration.get_driver, name='driver_registration'),
    path('driver-profile/', driver_profile.index, name='driver_profile'),
    path('change-driver-status/', change_driver_status.chage_status, name='change_driver_status'),
    path('create-taxi-order/', create_order.create_order_handle, name='create_taxi_order'),
    path('car-models/', car_models.index, name='car_models'),
    path('create-car-model/', create_car_model.index, name='create_car_model'),
]
