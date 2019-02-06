
# CODE HISTORY #
# Sontillano     # Feb 5, 2019     # added SearchHousing, AddRequest, SignUp

# File creation date: Feb. 5, 2019

from django import forms
from .choices import *

class SearchHousing(forms.Form):
     area=forms.ChoiceField(choices = AREA_CHOICES, widget=forms.Select(), required=False)
     propertyType = forms.ChoiceField(choices = PROPERTY_CHOICES, widget=forms.Select(), required=False)
     homeType = forms.ChoiceField(choices = HOME_CHOICES, widget=forms.Select(), required=False)
     priceMin = forms.FloatField(required=False)
     priceMax = forms.FloatField(required=False)
     kitchen = forms.BooleanField(initial=False, required=False)
     aircon = forms.BooleanField(initial=False, required=False)
     washer = forms.BooleanField(initial=False, required=False)
     dryer = forms.BooleanField(initial=False, required=False)
     wifi = forms.BooleanField(initial=False, required=False)
     iron = forms.BooleanField(initial=False, required=False)
     tv = forms.BooleanField(initial=False, required=False)
     parking = forms.BooleanField(initial=False, required=False)
     pet = forms.BooleanField(initial=False, required=False)
     smoking = forms.BooleanField(initial=False, required=False)
     curfew = forms.BooleanField(initial=False, required=False)
    
class AddRequest(forms.Form):
	 email = forms.CharField(max_length=50, required=True)
 	 requestType = forms.ChoiceField(choices = REQUEST_CHOICES, widget=forms.Select(), required=True)
 	 content = forms.CharField(required=True, widget=forms.Textarea)

class SignUp(forms.Form):
	 lname = forms.CharField(max_length=40, required=True)
 	 fname = forms.CharField(max_length=40, required=True)
  	 contact = forms.CharField(max_length=70, required=True)  
