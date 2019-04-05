from django.shortcuts import render, redirect
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
	ownerid = request.session.get('ownerid')
	records = HousingOwner.objects.filter(ownerid=ownerid)

	content = {
		'records' : records,
	}

	return render(request, 'ownerpage/home.html', content)

def ownerlogout(request):
	logout(request)
	
	return HttpResponseRedirect('/ownerlogin')
	
def account(request):
	ownerid = request.session.get('ownerid')
	record = Owner.objects.get(ownerid=ownerid)

	if request.method == "POST":
		form = editOwnerForm(request.POST, instance=record)
		if form.is_valid():
			if '_save' in request.POST:
				# if next button is pressed, save the form then go the rooms form
				print("save")
				post = form.save()
				return HttpResponseRedirect(reverse('editContactRecord', args=()))

	form = editOwnerForm(instance=record)
	
	content = {
		'recordExist' : True,
		'record' : record, 	
		'form' : form,
	}

	return render(request, 'ownerpage/account.html', content)

def editContactRecord(request):
	ownerid = request.session.get('ownerid')
	contacts = Contact.objects.filter(ownerid=ownerid)

	if request.method=="GET":
		if '_delete' in request.GET:
			# if delete button is clicked
			recordid = request.GET.get('_delete', '')	#id of the record to be deleted
			print(recordid)
			record = Contact.objects.get(contactid=recordid)
			record.delete()
			return HttpResponseRedirect(reverse('editContactRecord', args=()))
		if '_save' in request.GET:
			# add new record or edit an existing room record
			recordid = request.GET.get('_save', '') #id of the record to be edited or if this is 0, then add a new record
			contactno = request.GET.get('contactno', '') #contactno
			if recordid=='0':
				print("add")
				newRecord = Contact.objects.create(contactno=contactno, ownerid=Owner.objects.get(ownerid=ownerid))
			else:
				record = Contact.objects.get(contactid=recordid)
				record.contactno = contactno
				record.save()
				print("edit")
			
			print(recordid)
			print(contactno)
			return HttpResponseRedirect(reverse('editContactRecord', args=()))

	contactform = editContactForm()

	content = {
		'recordExist' : True,
		'contacts' : contacts,
		'contactform' : contactform,
	}

	return render(request, 'ownerpage/contactrecord.html', content)

def editHousingRecord(request, housingid):
	record = Housing.objects.get(housingid=housingid)
	form = housingForm(instance=record)
	
	if request.method=="GET":
		if '_delete' in request.GET:
			record.delete()
			return HttpResponseRedirect(reverse('home', args=()))

	if request.method == "POST":
		form = housingForm(request.POST, instance=record)
		if form.is_valid():
			if '_save' in request.POST:
				# if next button is pressed, save the form then go the rooms form
				print("save")
				post = form.save()
				return HttpResponseRedirect(reverse('editRoomRecord', args=(housingid,)))

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
			record = RoomCost.objects.get(roomid=recordid)
			record.delete()
			return HttpResponseRedirect(reverse('editRoomRecord', args=(housingid,)))
		if '_save' in request.GET:
			# add new record or edit an existing room record
			recordid = request.GET.get('_save', '') #id of the record to be edited or if this is 0, then add a new record
			roomname = request.GET.get('roomname', '') #roomname
			cost = request.GET.get('cost', '') #cost
			if recordid=='0':
				print("add")
				newRecord = RoomCost.objects.create(roomname=roomname, cost=cost, housingid=Housing.objects.get(housingid=housingid))
			else:
				record = RoomCost.objects.get(roomid=recordid)
				record.roomname = roomname
				record.cost = cost
				record.save()
				print("edit")
			
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
			record = HousingAdditionalInfo.objects.get(housingadditionalinfoid=recordid)
			record.delete()
			return HttpResponseRedirect(reverse('editAmenityRecord', args=(housingid,)))
		if '_save' in request.GET:
			# add new record or edit an existing room record
			# NOTE: if None yung value ng description, it means walang laman yung field na yun sa db
			recordid = request.GET.get('_save', '') #id of the record to be edited or if this is 0, then add a new record
			additionalinfoid = request.GET.get('additionalinfoid', '') #additionalinfoid
			description = request.GET.get('description', '') #description
			if recordid=='0':
				print("add")
				newRecord = HousingAdditionalInfo.objects.create(additionalinfoid=Additionalinfo.objects.get(additionalinfoid=additionalinfoid), description=description, housingid=Housing.objects.get(housingid=housingid))
			else:
				record = HousingAdditionalInfo.objects.get(housingadditionalinfoid=recordid)
				record.additionalinfoid = Additionalinfo.objects.get(additionalinfoid=additionalinfoid)
				record.description = description
				record.save()
				print("edit")
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
			record = HousingAdditionalInfo.objects.get(housingadditionalinfoid=recordid)
			record.delete()
			return HttpResponseRedirect(reverse('editFacilityRecord', args=(housingid,)))
		if '_save' in request.GET:
			# add new record or edit an existing room record
			# NOTE: if None yung value ng description, it means walang laman yung field na yun sa db
			recordid = request.GET.get('_save', '') #id of the record to be edited or if this is 0, then add a new record
			additionalinfoid = request.GET.get('additionalinfoid', '') #additionalinfoid
			description = request.GET.get('description', '') #description
			if recordid=='0':
				print("add")
				newRecord = HousingAdditionalInfo.objects.create(additionalinfoid=Additionalinfo.objects.get(additionalinfoid=additionalinfoid), description=description, housingid=Housing.objects.get(housingid=housingid))
			else:
				record = HousingAdditionalInfo.objects.get(housingadditionalinfoid=recordid)
				record.additionalinfoid = Additionalinfo.objects.get(additionalinfoid=additionalinfoid)
				record.description = description
				record.save()
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
			record = HousingAdditionalInfo.objects.get(housingadditionalinfoid=recordid)
			record.delete()
			return HttpResponseRedirect(reverse('editRuleRecord', args=(housingid,)))
		if '_save' in request.GET:
			# add new record or edit an existing room record
			# NOTE: if None yung value ng description, it means walang laman yung field na yun sa db
			recordid = request.GET.get('_save', '') #id of the record to be edited or if this is 0, then add a new record
			additionalinfoid = request.GET.get('additionalinfoid', '') #additionalinfoid
			description = request.GET.get('description', '') #description
			if recordid=='0':
				print("add")
				newRecord = HousingAdditionalInfo.objects.create(additionalinfoid=Additionalinfo.objects.get(additionalinfoid=additionalinfoid), description=description, housingid=Housing.objects.get(housingid=housingid))
			else:
				record = HousingAdditionalInfo.objects.get(housingadditionalinfoid=recordid)
				record.additionalinfoid = Additionalinfo.objects.get(additionalinfoid=additionalinfoid)
				record.description = description
				record.save()
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

