from django.contrib import admin

# Register your models here.
from mainapp.models import MainappModel


@admin.register(MainappModel)
class MainappAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'main_intro',
    )

    list_display_links = (
        'id',
        'main_intro',
    )

    search_fields = [
        'id',
        'main_intro',
    ]