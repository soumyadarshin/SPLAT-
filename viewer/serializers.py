from rest_framework import serializers
from .models import *


class ViewReportSerializer(serializers.ModelSerializer):
    class Meta:
        model=ViewReport
        fields=['path_analysis', 'report_analysis']
        
        
class transmitterserializer(serializers.ModelSerializer):
    class Meta:
        model = transmitter
        fields = ['transmitter_name','lattitude','longitude','antenna_height']
        
        
class receiverserializer(serializers.ModelSerializer):
    class Meta:
        model = receiver
        fields = ['receiver_name','receiver_lattitude','receiver_longitude','receiver_antenna_height']