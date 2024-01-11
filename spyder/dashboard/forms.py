from django import forms
from .models import *
from datetime import datetime



class PlaceSearch(forms.ModelForm):
    # Form saves every search into PlaceHistory table
    class Meta:
        model = PlaceHistory
        fields = ['place_id']

    widgets = {
            'place_id': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Place id'
                })
    }