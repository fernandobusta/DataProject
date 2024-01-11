from django.db import models


# Instances of places get deleted after a user has ended their session
# or after a specific time has passed

# Create your models here.
class Place(models.Model):

    # Info about the search
    id = models.AutoField(primary_key=True)
    mydate = models.DateTimeField(auto_now_add=True)

    # Data about the place
    # 'name', 'formatted_address', 'type', 'icon', 'opening_hours', 'website', 'rating', 'review'
    place_id = models.CharField(max_length=300)
    business_status = models.CharField(max_length=100)
    formatted_address = models.CharField(max_length=300)
    name = models.CharField(max_length=100)
    opening_hours = models.CharField(max_length=100)
    plus_code = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    reviews = models.TextField(default='')
    types = models.CharField(max_length=200)
    url = models.URLField()
    user_ratings_total = models.IntegerField()
    vicinity = models.CharField(max_length=100)
    website = models.URLField()

class PlaceHistory(models.Model):
    id = models.AutoField(primary_key=True)
    mydate = models.DateTimeField(auto_now_add=True)
    place_id = models.CharField(max_length=500)