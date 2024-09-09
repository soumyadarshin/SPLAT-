from django.db import models

class ViewReport(models.Model):
    path_analysis = models.FileField(upload_to='docs/',blank=True)
    report_analysis = models.FileField(upload_to='report_docs/',blank=True)
    
    
class transmitter(models.Model):
    transmitter_name = models.CharField(max_length=50)
    lattitude = models.BigIntegerField()
    longitude = models.BigIntegerField()
    antenna_height = models.IntegerField()
    
    

    
class receiver(models.Model):
    receiver_name = models.CharField(max_length=50)
    receiver_lattitude = models.BigIntegerField()
    receiver_longitude = models.BigIntegerField()
    receiver_antenna_height = models.IntegerField()
    
    
    
