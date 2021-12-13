from django.db import models

# Create your models here.

class MainappModel(models.Model):
    main_intro = models.CharField(max_length=255, null=True, blank=True, verbose_name="메인 소개글")

