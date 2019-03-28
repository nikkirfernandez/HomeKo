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
	
	if request.method=="GET":
		if '_delete' in request.GET:
			# if delete button is clicked
			print("delete")

	if request.method == "POST":
		form = addAdditionalinfoForm(request.POST, instance=record)
		if form.is_valid():
			if '_save' in request.POST:
				# if next button is pressed, save the form then go the rooms form
				print("save")

	content = {
		'recordExist' : True,
		'record' : record, 	
		'form' : form,
	}

	return render(request, 'ownerpage/housingrecord.html', content)

def editRoomRecord(request, housingid):
	roomform = roomCostForm()
	housingRooms = RoomCost.objects.filter(housingid=housingid)

	if request.method=="GET":
		if '_delete' in request.GET:
			# if delete button is clicked
			recordid = request.GET.get('_delete', '')	#id of the record to be deleted
			print(recordid)
			return HttpResponseRedirect(reverse('editRoomRecord', args=(housingid,)))
		if '_save' in request.GET:
			# add new record or edit an existing room record
			recordid = request.GET.get('_save', '') #id of the record to be edited or if this is 0, then add a new record
			roomname = request.GET.get('roomname', '') #roomname
			cost = request.GET.get('cost', '') #cost
			print(recordid)
			print(roomname)
			print(cost)
			return HttpResponseRedirect(reverse('editRoomRecord', args=(housingid,)))

	content = {
		'recordExist' : True,
		'roomform' : roomform,
		'rooms' : housingRooms,
		'housingid': housingid,
	}

	return render(request, 'ownerpage/roomrecord.html', content)

def editAmenityRecord(request, housingid):
	amenityform = housingAddtnlinfoForm()
	amenityform.fields["additionalinfoid"].queryset = Additionalinfo.objects.filter(additionalinfotype=1)
	amenities = HousingAdditionalInfo.objects.filter(housingid=housingid, additionalinfoid__additionalinfotype=1)


	if request.method=="GET":
		if '_delete' in request.GET:
			# if delete button is clicked
			recordid = request.GET.get('_delete', '')	#id of the record to be deleted
			print(recordid)
			return HttpResponseRedirect(reverse('editAmenityRecord', args=(housingid,)))
		if '_save' in request.GET:
			# add new record or edit an existing room record
			# NOTE: if None yung value ng description, it means walang laman yung field na yun sa db
			recordid = request.GET.get('_save', '') #id of the record to be edited or if this is 0, then add a new record
			additionalinfoid = request.GET.get('additionalinfoid', '') #additionalinfoid
			description = request.GET.get('description', '') #description
			print(recordid)
			print(additionalinfoid)
			print(description)
			return HttpResponseRedirect(reverse('editAmenityRecord', args=(housingid,)))


	content = {
		'recordExist' : True,
		'amenityform' : amenityform,
		'amenities' : amenities,
		'housingid': housingid,
	}

	return render(request, 'ownerpage/amenityrecord.html', content)

def editFacilityRecord(request, housingid):
	facilityform = housingAddtnlinfoForm()
	facilityform.fields["additionalinfoid"].queryset = Additionalinfo.objects.filter(additionalinfotype=2)
	facilities = HousingAdditionalInfo.objects.filter(housingid=housingid, additionalinfoid__additionalinfotype=2)

	if request.method=="GET":
		if '_delete' in request.GET:
			# if delete button is clicked
			recordid = request.GET.get('_delete', '')	#id of the record to be deleted
			print(recordid)
			return HttpResponseRedirect(reverse('editFacilityRecord', args=(housingid,)))
		if '_save' in request.GET:
			# add new record or edit an existing room record
			# NOTE: if None yung value ng description, it means walang laman yung field na yun sa db
			recordid = request.GET.get('_save', '') #id of the record to be edited or if this is 0, then add a new record
			additionalinfoid = request.GET.get('additionalinfoid', '') #additionalinfoid
			description = request.GET.get('description', '') #description
			print(recordid)
			print(additionalinfoid)
			print(description)
			return HttpResponseRedirect(reverse('editFacilityRecord', args=(housingid,)))
			
	content = {
		'recordExist' : True,
		'facilityform' : facilityform,
		'facilities' : facilities,
		'housingid': housingid,
	}

	return render(request, 'ownerpage/facilityrecord.html', content)

def editRuleRecord(request, housingid):
	ruleform = housingAddtnlinfoForm()
	ruleform.fields["additionalinfoid"].queryset = Additionalinfo.objects.filter(additionalinfotype=3)
	rules = HousingAdditionalInfo.objects.filter(housingid=housingid, additionalinfoid__additionalinfotype=3)

	if request.method=="GET":
		if '_delete' in request.GET:
			# if delete button is clicked
			recordid = request.GET.get('_delete', '')	#id of the record to be deleted
			print(recordid)
			return HttpResponseRedirect(reverse('editRuleRecord', args=(housingid,)))
		if '_save' in request.GET:
			# add new record or edit an existing room record
			# NOTE: if None yung value ng description, it means walang laman yung field na yun sa db
			recordid = request.GET.get('_save', '') #id of the record to be edited or if this is 0, then add a new record
			additionalinfoid = request.GET.get('additionalinfoid', '') #additionalinfoid
			description = request.GET.get('description', '') #description
			print(recordid)
			print(additionalinfoid)
			print(description)
			return HttpResponseRedirect(reverse('editRuleRecord', args=(housingid,)))

	content = {
		'recordExist' : True,
		'ruleform' : ruleform,
		'rules' : rules,
		'housingid': housingid,
	}

	return render(request, 'ownerpage/rulerecord.html', content)

