from django.urls import path
from .views import *

urlpatterns = [
    path('index', index, name="index"),
    path('simple', simple, name="simple"),

    path('', searchPlace, name="seachPlace"),
    path('placeInfo', placeInfo, name="placeInfo"),
]