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
	content = {}

	return render(request, 'ownerpage/home.html', content)

def account(request):
	record = Owner.objects.get(ownerid=1)
	form = editOwnerForm(instance=record)
	content = {
		'recordExist' : True,
		'record' : record, 	
		'form' : form,
	}

	return render(request, 'ownerpage/account.html', content)

def housingRecord(request):
	housingid = 1
	record = Housing.objects.get(housingid=housingid)
	form = editHousingForm(instance=record)
	roomform = editRoomCostForm()
	amenityform = editHousingAddtnlinfoForm()
	amenityform.fields["additionalinfoid"].queryset = Additionalinfo.objects.filter(additionalinfotype=1)
	facilityform = editHousingAddtnlinfoForm()
	facilityform.fields["additionalinfoid"].queryset = Additionalinfo.objects.filter(additionalinfotype=2)
	ruleform = editHousingAddtnlinfoForm()
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
# Create your views here.
