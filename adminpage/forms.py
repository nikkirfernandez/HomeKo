# CODE HISTORY #
# Sontillano     # Feb 11, 2019     # added AdminLogin, addAdditionalinfo, addArea, addContact, addFeedback, addHousetype, addHousingAddtnlinfo, addHousingOwner, addHousingRequest, addHousing, addOwner, addPicture, addPropertytype, addRequest, addRoomCost

# File creation date: Feb. 11, 2019

from django import forms
from .choices import *

class AdminLogin(forms.Form):
	uname = forms.CharField(max_length=50, required=True)
	pw = forms.CharField(max_length=50, required=True)

class addAdditionalinfo(forms.Form):
	name = forms.CharField(max_length=70, required=True)
	infotype = forms.ChoiceField(choices = INFOTYPE_CHOICES, widget=forms.Select(), required=True)

class addArea(forms.Form):
     name = forms.CharField(max_length=30, required=True)
		
class addContact(forms.Form):
     contactno = forms.CharField(max_length=1, required=True)
     ownerid = forms.ChoiceField(widget=forms.Select(), required=True)

class addFeedback(forms.Form):
	status = forms.ChoiceField(choices = FEEDBACK_STATUS_CHOICES, widget=forms.Select(), required=True)

class addHousetype(forms.Form):
	name = forms.CharField(max_length=20, required=True)

class addHousingAddtnlinfo(forms.Form):
     addtnlinfoid = forms.ChoiceField(widget=forms.Select(), required=True)
     description = forms.CharField(max_length=300, required=False)
     housingid = forms.ChoiceField(widget=forms.Select(), required=True)

class addHousingOwner(forms.Form):
	housingid = forms.ChoiceField(widget=forms.Select(), required=True)
	ownerid = forms.ChoiceField(widget=forms.Select(), required=True)

class addHousingRequest(forms.Form):
	housingid = forms.ChoiceField(widget=forms.Select(), required=True)
	requestid = forms.ChoiceField(widget=forms.Select(), required=True)

class addHousing(forms.Form):
	name = forms.CharField(max_length=50, required=True)
	area = forms.ChoiceField(widget=forms.Select(), required=True)
    address = forms.CharField(max_length=80, required=True)
    propertytype = forms.ChoiceField(widget=forms.Select(), required=True)
	housetype = forms.ChoiceField(widget=forms.Select(), required=True)
	maphtml = forms.CharField(max_length=500, required=False)

class addOwner(forms.Form):
     uname = forms.CharField(max_length=70, required=True)
     fName = forms.CharField(max_length=40, required=True)
     lName = forms.CharField(max_length=40, required=True)
     email = forms.CharField(max_length=60, required=False)

class addPicture(forms.Form):
	file = forms.CharField(max_length=30, required=True)
	housingid = forms.ChoiceField(widget=forms.Select(), required=True)

class addPropertytype(forms.Form):
	name = forms.CharField(max_length=20, required=True)

class addRequest(forms.Form):
	 reqtype = forms.ChoiceField(choices = REQUEST_TYPE_CHOICES, widget=forms.Select(), required=True)
     status = forms.ChoiceField(choices = REQUEST_STATUS_CHOICES, widget=forms.Select(), required=True)

class addRoomCost(forms.Form):
	name = forms.CharField(max_length=100, required=True)
	cost = forms.FloatField(required=True)
	housingid = forms.ChoiceField(widget=forms.Select(), required=True)
		