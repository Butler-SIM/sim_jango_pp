
from django.contrib import admin
from django.urls import path

import mainapp
from mainapp.views import main

app_name = 'mainapp'

urlpatterns = [
    path('', main, name='main'),
]
