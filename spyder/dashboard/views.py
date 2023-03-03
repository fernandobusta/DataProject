from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import *

# Create your views here.
def index(request):
    return render(request, 'dashboard/index.html')

def simple(request):
    return render(request, 'dashboard/simple.html')


# View for the Search place form
def searchPlace(request):
    if request.method == 'POST':
        # Create a new instance of the form with the data entered
        form = PlaceSearch(request.POST)

        if form.is_valid():
            place = form.save()
            return redirect('placeInfo')
        else:
            return render(request, 'dashboard/search_place.html',{form:'form'})
    else:
        # Normal get request, user wants to see the form
        form = PlaceSearch()
        return render(request, 'dashboard/search_place.html', {'form':form})

# View for every place -> display the info
def placeInfo(request):
    place = PlaceHistory.objects.last()
    return render(request, 'dashboard/place_info.html', {'place':place})
