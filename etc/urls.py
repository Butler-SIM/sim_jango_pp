
from django.contrib import admin
from django.urls import path

import mainapp
from etc.views import etcList
from mainapp.views import *

app_name = 'etc'

urlpatterns = [
    path('', etcList, name='etcList'),

]
