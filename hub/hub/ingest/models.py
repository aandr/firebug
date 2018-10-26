from django.db import models


class DataPoint(models.Model):
    device = models.ForeignKey('devices.Device', on_delete=models.DO_NOTHING)
    temperature = models.FloatField()
    pm25 = models.FloatField()
    pm1 = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = [('device', 'timestamp')]
