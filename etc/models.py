from django.db import models
from django.utils.timezone import now
# Create your models here.


class LottoNumber(models.Model):
    number_01 = models.IntegerField(null=True)
    number_02 = models.IntegerField(null=True)
    number_03 = models.IntegerField(null=True)
    number_04 = models.IntegerField(null=True)
    number_05 = models.IntegerField(null=True)
    number_06 = models.IntegerField(null=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name='생성일')

    class Meta:
        db_table = 'lotto_number'
        verbose_name        = "lotto"
