from django.contrib import admin
from CandDmotors.models import Galareya
# Register your models here.

class GalareyaAdmin(admin.ModelAdmin):
    list_display = ['name', 'model', 'gibrid', 'max_speed', 'passangers', 'battery_capacity', 'max_cruising_range']
    prepopulated_fields = {'slug': ('model',)}
admin.site.register(Galareya, GalareyaAdmin)