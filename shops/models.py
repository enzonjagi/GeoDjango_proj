from django.contrib.gis.db import models

class Shop(models.Model):
    """Represents a Shop on the App"""

    name = models.CharField(max_length=100)
    location = models.PointField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)