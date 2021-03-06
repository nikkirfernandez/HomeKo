# License: MIT License

# CODE HISTORY #
# Sontillano     # Mar 30, 2019     # added home, account, editHousingRecord, editRoomRecord, editAmenityRecord, editFacilityRecord, editRuleRecord
# Sontillano     # Apr 3, 2019     # added ownerlogout

# File creation date: Mar. 30, 2019

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

# Method name: home 
# Creation date: Mar 30, 2019 
# Purpose: View for the owner home page. Contains the list of housings the owner own.
# Calling arguments: No arguments for calling this function.
# Required files: home.html
@login_required(login_url='/ownerlogin') 
def home(request):
	if not request.user.is_superuser:
		ownerid = request.session.get('ownerid')
		records = HousingOwner.objects.filter(ownerid=ownerid)

		content = {
			'records' : records,
		}

		return render(request, 'ownerpage/home.html', content)
	else:
		return HttpResponseRedirect('/ownerlogin')

# Method name: ownerlogout
# Creation date: Apr 3, 2019 
# Purpose: Logs out the owner
# Calling arguments: No arguments for calling this function.
# Required files: None
@login_required(login_url='/ownerlogin') 
def ownerlogout(request):
	if not request.user.is_superuser:
		logout(request)
	
	return HttpResponseRedirect('/ownerlogin')

# Method name: account
# Creation date: Mar 30, 2019 
# Purpose: Owner can edit his/her personal information
# Calling arguments: No arguments for calling this function.
# Required files: account.html
@login_required(login_url='/ownerlogin') 
def account(request):
	if not request.user.is_superuser:
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
	else:
		return HttpResponseRedirect('/ownerlogin')

# Method name: editContactRecord
# Creation date: Mar 30, 2019 
# Purpose: Owner can edit his/her contact information
# Calling arguments: No arguments for calling this function.
# Required files: contactrecord.html
@login_required(login_url='/ownerlogin') 
def editContactRecord(request):
	if not request.user.is_superuser:
		ownerid = request.session.get('ownerid')
		contacts = Contact.objects.filter(ownerid=ownerid)

		if request.method=="GET":
			if '_delete' in request.GET:
				# if delete button is clicked
				recordid = request.GET.get('_delete', '')	#id of the record to be deleted
				record = Contact.objects.get(contactid=recordid)
				record.delete()
				return HttpResponseRedirect(reverse('editContactRecord', args=()))
			if '_save' in request.GET:
				# add new record or edit an existing room record
				recordid = request.GET.get('_save', '') #id of the record to be edited or if this is 0, then add a new record
				contactno = request.GET.get('contactno', '') #contactno
				if recordid=='0':
					newRecord = Contact.objects.create(contactno=contactno, ownerid=Owner.objects.get(ownerid=ownerid))
				else:
					record = Contact.objects.get(contactid=recordid)
					record.contactno = contactno
					record.save()
				return HttpResponseRedirect(reverse('editContactRecord', args=()))

		contactform = editContactForm()

		content = {
			'recordExist' : True,
			'contacts' : contacts,
			'contactform' : contactform,
		}

		return render(request, 'ownerpage/contactrecord.html', content)
	else:
		return HttpResponseRedirect('/ownerlogin')

# Method name: editHousingRecord
# Creation date: Mar 30, 2019 
# Purpose: Owner can edit the fields of a Housing record
# Calling arguments: No arguments for calling this function.
# Required files: housingrecord.html
@login_required(login_url='/ownerlogin') 
def editHousingRecord(request, housingid):
	if not request.user.is_superuser:
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
	else:
		return HttpResponseRedirect('/ownerlogin')

# Method name: editRoomRecord
# Creation date: Mar 30, 2019 
# Purpose: Owner can edit the fields of a Room record
# Calling arguments: No arguments for calling this function.
# Required files: roomrecord.html
@login_required(login_url='/ownerlogin') 
def editRoomRecord(request, housingid):
	if not request.user.is_superuser:
		roomform = roomCostForm()
		housingRooms = RoomCost.objects.filter(housingid=housingid)

		if request.method=="GET":
			if '_delete' in request.GET:
				# if delete button is clicked
				recordid = request.GET.get('_delete', '')	#id of the record to be deleted
				record = RoomCost.objects.get(roomid=recordid)
				record.delete()
				return HttpResponseRedirect(reverse('editRoomRecord', args=(housingid,)))
			if '_save' in request.GET:
				# add new record or edit an existing room record
				recordid = request.GET.get('_save', '') #id of the record to be edited or if this is 0, then add a new record
				roomname = request.GET.get('roomname', '') #roomname
				cost = request.GET.get('cost', '') #cost
				if recordid=='0':
					newRecord = RoomCost.objects.create(roomname=roomname, cost=cost, housingid=Housing.objects.get(housingid=housingid))
				else:
					record = RoomCost.objects.get(roomid=recordid)
					record.roomname = roomname
					record.cost = cost
					record.save()
				return HttpResponseRedirect(reverse('editRoomRecord', args=(housingid,)))

		content = {
			'recordExist' : True,
			'roomform' : roomform,
			'rooms' : housingRooms,
			'housingid': housingid,
		}

		return render(request, 'ownerpage/roomrecord.html', content)
	else:
		return HttpResponseRedirect('/ownerlogin')

# Method name: editAmenityRecord
# Creation date: Mar 30, 2019 
# Purpose: Owner can edit the fields of a Amenity record
# Calling arguments: No arguments for calling this function.
# Required files: amenityrecord.html
@login_required(login_url='/ownerlogin') 
def editAmenityRecord(request, housingid):
	if not request.user.is_superuser:
		amenityform = housingAddtnlinfoForm()
		amenityform.fields["additionalinfoid"].queryset = Additionalinfo.objects.filter(additionalinfotype=1)
		amenities = HousingAdditionalInfo.objects.filter(housingid=housingid, additionalinfoid__additionalinfotype=1)

		if request.method=="GET":
			if '_delete' in request.GET:
				# if delete button is clicked
				recordid = request.GET.get('_delete', '')	#id of the record to be deleted
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
					newRecord = HousingAdditionalInfo.objects.create(additionalinfoid=Additionalinfo.objects.get(additionalinfoid=additionalinfoid), description=description, housingid=Housing.objects.get(housingid=housingid))
				else:
					record = HousingAdditionalInfo.objects.get(housingadditionalinfoid=recordid)
					record.additionalinfoid = Additionalinfo.objects.get(additionalinfoid=additionalinfoid)
					record.description = description
					record.save()
				return HttpResponseRedirect(reverse('editAmenityRecord', args=(housingid,)))

		content = {
			'recordExist' : True,
			'amenityform' : amenityform,
			'amenities' : amenities,
			'housingid': housingid,
		}

		return render(request, 'ownerpage/amenityrecord.html', content)
	else:
		return HttpResponseRedirect('/ownerlogin')

# Method name: editFacilityRecord
# Creation date: Mar 30, 2019 
# Purpose: Owner can edit the fields of a Facility record
# Calling arguments: No arguments for calling this function.
# Required files: facilityrecord.html
@login_required(login_url='/ownerlogin') 
def editFacilityRecord(request, housingid):
	if not request.user.is_superuser:
		facilityform = housingAddtnlinfoForm()
		facilityform.fields["additionalinfoid"].queryset = Additionalinfo.objects.filter(additionalinfotype=2)
		facilities = HousingAdditionalInfo.objects.filter(housingid=housingid, additionalinfoid__additionalinfotype=2)

		if request.method=="GET":
			if '_delete' in request.GET:
				# if delete button is clicked
				recordid = request.GET.get('_delete', '')	#id of the record to be deleted
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
					newRecord = HousingAdditionalInfo.objects.create(additionalinfoid=Additionalinfo.objects.get(additionalinfoid=additionalinfoid), description=description, housingid=Housing.objects.get(housingid=housingid))
				else:
					record = HousingAdditionalInfo.objects.get(housingadditionalinfoid=recordid)
					record.additionalinfoid = Additionalinfo.objects.get(additionalinfoid=additionalinfoid)
					record.description = description
					record.save()
				return HttpResponseRedirect(reverse('editFacilityRecord', args=(housingid,)))
			
		content = {
			'recordExist' : True,
			'facilityform' : facilityform,
			'facilities' : facilities,
			'housingid': housingid,
		}

		return render(request, 'ownerpage/facilityrecord.html', content)
	else:
		return HttpResponseRedirect('/ownerlogin')

# Method name: editRuleRecord
# Creation date: Mar 30, 2019 
# Purpose: Owner can edit the fields of a Rule record
# Calling arguments: No arguments for calling this function.
# Required files: rulerecord.html
@login_required(login_url='/ownerlogin') 
def editRuleRecord(request, housingid):
	if not request.user.is_superuser:
		ruleform = housingAddtnlinfoForm()
		ruleform.fields["additionalinfoid"].queryset = Additionalinfo.objects.filter(additionalinfotype=3)
		rules = HousingAdditionalInfo.objects.filter(housingid=housingid, additionalinfoid__additionalinfotype=3)

		if request.method=="GET":
			if '_delete' in request.GET:
				# if delete button is clicked
				recordid = request.GET.get('_delete', '')	#id of the record to be deleted
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
					newRecord = HousingAdditionalInfo.objects.create(additionalinfoid=Additionalinfo.objects.get(additionalinfoid=additionalinfoid), description=description, housingid=Housing.objects.get(housingid=housingid))
				else:
					record = HousingAdditionalInfo.objects.get(housingadditionalinfoid=recordid)
					record.additionalinfoid = Additionalinfo.objects.get(additionalinfoid=additionalinfoid)
					record.description = description
					record.save()
				return HttpResponseRedirect(reverse('editRuleRecord', args=(housingid,)))

		content = {
			'recordExist' : True,
			'ruleform' : ruleform,
			'rules' : rules,
			'housingid': housingid,
		}

		return render(request, 'ownerpage/rulerecord.html', content)
	else:
		return HttpResponseRedirect('/ownerlogin')

