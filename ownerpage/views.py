from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.db.models.functions import Concat
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import *
from mainpage.models import *

def home(request):
	ownerid = 1
	records = HousingOwner.objects.filter(ownerid=ownerid)
	
	request.session['ownerid'] = ownerid
	content = {
		'records' : records,
	}

	return render(request, 'ownerpage/home.html', content)

def account(request):
	ownerid = request.session.get('ownerid')
	record = Owner.objects.get(ownerid=ownerid)
	contacts = Contact.objects.filter(ownerid=ownerid)
	form = editOwnerForm(instance=record)
	contactform = editContactForm()
	content = {
		'recordExist' : True,
		'record' : record, 	
		'form' : form,
		'contactform' : contactform,
	}

	return render(request, 'ownerpage/account.html', content)

def editHousingRecord(request, housingid):
	record = Housing.objects.get(housingid=housingid)
	form = housingForm(instance=record)
	roomform = roomCostForm()
	amenityform = housingAddtnlinfoForm()
	amenityform.fields["additionalinfoid"].queryset = Additionalinfo.objects.filter(additionalinfotype=1)
	facilityform = housingAddtnlinfoForm()
	facilityform.fields["additionalinfoid"].queryset = Additionalinfo.objects.filter(additionalinfotype=2)
	ruleform = housingAddtnlinfoForm()
	ruleform.fields["additionalinfoid"].queryset = Additionalinfo.objects.filter(additionalinfotype=3)

	housingRooms = RoomCost.objects.filter(housingid=housingid)
	amenities = HousingAdditionalInfo.objects.filter(housingid=housingid, additionalinfoid__additionalinfotype=1)
	facilities = HousingAdditionalInfo.objects.filter(housingid=housingid, additionalinfoid__additionalinfotype=2)
	rules = HousingAdditionalInfo.objects.filter(housingid=housingid, additionalinfoid__additionalinfotype=3)

	content = {
		'recordExist' : True,
		'record' : record, 	
		'form' : form,
		'roomform' : roomform,
		'amenityform' : amenityform,
		'facilityform' : facilityform,
		'ruleform' : ruleform,
		'rooms' : housingRooms,
		'amenities' : amenities,
		'facilities' : facilities,
		'rules' : rules,
	}

	return render(request, 'ownerpage/housingrecord.html', content)

def addHousingRecord(request):
	form = housingForm()
	roomform = roomCostForm()
	amenityform = housingAddtnlinfoForm()
	amenityform.fields["additionalinfoid"].queryset = Additionalinfo.objects.filter(additionalinfotype=1)
	facilityform = housingAddtnlinfoForm()
	facilityform.fields["additionalinfoid"].queryset = Additionalinfo.objects.filter(additionalinfotype=2)
	ruleform = housingAddtnlinfoForm()
	ruleform.fields["additionalinfoid"].queryset = Additionalinfo.objects.filter(additionalinfotype=3)

	content = {
		'recordExist' : False,	
		'form' : form,
		'roomform' : roomform,
		'amenityform' : amenityform,
		'facilityform' : facilityform,
		'ruleform' : ruleform,
	}

	return render(request, 'ownerpage/housingrecord.html', content)
# Create your views here.
