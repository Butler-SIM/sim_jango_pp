import json
from rest_framework import serializers
from django.db.models import Count

from etc.models import LottoNumber


class LottoNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = LottoNumber
        fields = '__all__'



