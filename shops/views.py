from django.shortcuts import render
from django.views import generic
from django.contrib.gis.geos import fromstr, Point
from django.contrib.gis.db.models.functions import Distance
from .models import Shop
from pathlib import Path
import json

# we're hard coding the coordinates of Nairobi 
# This is to simulate a user's location. 
# Ideally the user should supply this info, 
# but we're doign this as a demo.

# for miami data
longitude = -80.191_788
latitude = 25.761_681

user_location = Point(longitude, latitude, srid=4326)

# for Nairobi data
longitude2 = -36.8219
latitude2 = 1.2921

user_location2 = Point(longitude2, latitude2, srid=4326)
# user_location = fromstr(f'POINT({longitude} {latitude})', srid=4326)

# Let's try to display shops in miami here
DATA_FILENAME = 'data.json'

class Home(generic.ListView):
    """A view of shops around the user's location"""

    model = Shop
    content_object_name = 'shops'
    queryset = Shop.objects.annotate(
        distance=Distance('location', user_location2)
    ).order_by("distance")[0:6]
    template_name = 'shops/index.html'

home = Home.as_view()
