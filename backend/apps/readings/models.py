from django.db import models

# Create your models here.
class Device(models.Model):
    type_choices = [("smart_meter","smart_meter"),("smart_thermo","smart_thermo"),("sensor","sensor")]
    device_id = models.CharField(max_length=300,blank=False,null=False, unique=True)
    name = models.CharField(max_length=300,blank=False,null=True)
    type = models.CharField(choices=type_choices)
    location = models.CharField(max_length=200,blank=True,null=True)
    is_active = models.BooleanField(default= True,blank=False, null= True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "devices"

    def __str__(self):
        return self.name + " : " + self.type

class NetworkReading(models.Model):
    device = models.ForeignKey(Device,related_name="reading", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(blank=False)
    metric_name = models.CharField(max_length=500,blank=True)
    metric_value = models.FloatField(default=0)
    raw_payload = models.JSONField(blank=True,null = True)

    def __str__(self):
        return self.device.device_id +" "+ self.metric_name
    
    class Meta:
        ordering = ["-timestamp"]
        db_table = "device_readings"