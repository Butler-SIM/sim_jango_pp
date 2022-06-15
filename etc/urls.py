
from django.contrib import admin
from django.urls import path

import mainapp
from etc.views import etcList, LottoViewSet, get_week_lotto_check
from mainapp.views import *

app_name = 'etc'

urlpatterns = [
    path('', etcList, name='etcList'),
    path('/lotto', LottoViewSet.as_view({"get": "get_lotto_numer"}), name='lotto'),
    path('/week_lotto_check', get_week_lotto_check, name='week_lotto_check'),

]
