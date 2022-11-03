from django.contrib import admin
from django.urls import path
from.views import *

urlpatterns = [
    path('faker/',faker_view,name='fake'),
    path('data/',display_data,name='data'),
]