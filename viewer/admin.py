from django.contrib import admin
from .models import *

@admin.register(ViewReport)
class ViewReport(admin.ModelAdmin):
    list_display = ['path_analysis','report_analysis']

@admin.register(transmitter)
class transmitter(admin.ModelAdmin):
    list_display = ['transmitter_name','lattitude','longitude','antenna_height']

@admin.register(receiver)
class receiver(admin.ModelAdmin):
    list_display = ['receiver_name','receiver_lattitude','receiver_longitude','receiver_antenna_height']
    
    
