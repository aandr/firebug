from django.db import models


class Device(models.Model):
    serial = models.CharField(max_length=512)
    lat = models.DecimalField(max_digits=6, decimal_places=4)
    lon = models.DecimalField(max_digits=6, decimal_places=4)
    hw_version = models.IntegerField(default=0)
    fw_version = models.IntegerField(default=0)

    def as_json(self):
        return {
            'serial': self.serial,
            'lat': self.lat,
            'lon': self.lon
        }
