# This is a course requirement for CS 192 Software Engineering II under the supervision of Asst. Prof. Ma. Rowena C. Solamo of the Department of Computer Science, College of Engineering, University of the Philippines, Diliman for the AY 2018-2019.

# CODE HISTORY #
# Kasilag     

# File creation date: Feb. 19, 2019

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .choices import *
from .forms import *
from mainpage.models import *

# Create your views here.

def login(request):

	content = {
		'tableChoices' : TABLES_CHOICES,
	}

	return render(request, 'adminpage/login.html', content)

def home(request):

	content = {
		'tableChoices' : TABLES_CHOICES,
	}

	return render(request, 'adminpage/adminHome.html', content)

def tablePage(request, table):

	# TODO hindi nakasort kasi hindi integer yung ids
	if table == "Area":
		recordPK = Area.objects.values_list('areaid', flat=True).order_by('areaid')
		recordName = Area.objects.values_list('areaname')
		records = [{'item1': t[0], 'item2': t[1]} for t in zip(recordPK, recordName)]
	elif table == "Housing":
		recordPK = Housing.objects.values_list('housingid')
		recordName = Housing.objects.values_list('housingname', flat=True).order_by('housingid')
		records = [{'item1': t[0], 'item2': t[1]} for t in zip(recordPK, recordName)]
	elif table == "Additionalinfo":
		recordPK = Additionalinfo.objects.values_list('additionalinfoid')
		recordName = Additionalinfo.objects.values_list('additionalinfoname', flat=True).order_by('additionalinfoid')
		records = [{'item1': t[0], 'item2': t[1]} for t in zip(recordPK, recordName)]
		# TODO add owner table on Contact UI
	elif table == "Contact":
		recordPK = Contact.objects.values_list('contactid')
		recordName = Contact.objects.values_list('contactno', flat=True).order_by('contactid')
		records = [{'item1': t[0], 'item2': t[1]} for t in zip(recordPK, recordName)]
		# TODO the one being outputted is the integer value of the status field in Feedback
	elif table == "Feedback":
		recordPK = Feedback.objects.values_list('feedbackid')
		recordName = Feedback.objects.values_list('status', flat=True).order_by('feedbackid')
		records = [{'item1': t[0], 'item2': t[1]} for t in zip(recordPK, recordName)]
	elif table == "Housetype":
		recordPK = Housetype.objects.values_list('housetypeid')
		recordName = Housetype.objects.values_list('housetypename', flat=True).order_by('housetypeid')
		records = [{'item1': t[0], 'item2': t[1]} for t in zip(recordPK, recordName)]
	elif table == "HousingAdditionalinfo":
		recordPK = HousingAdditionalInfo.objects.values_list('housingadditionalinfoid')
		recordName = HousingAdditionalInfo.objects.values_list('description', flat=True).order_by('housingadditionalinfoid')
		records = [{'item1': t[0], 'item2': t[1]} for t in zip(recordPK, recordName)]

	# TODO The ones being outputted is the names of the housing certain Housing request is paired to.
	elif table == "HousingRequest":
		recordPK = HousingRequest.objects.values_list('housingrequestid')
		recordName = HousingRequest.objects.values_list('housingid', flat=True).order_by('housingrequestid')
		records = [{'item1': t[0], 'item2': t[1]} for t in zip(recordPK, recordName)]
	elif table == "HousingRequest":
		recordPK = HousingRequest.objects.values_list('housingrequestid')
		recordName = HousingRequest.objects.values_list('housingid', flat=True).order_by('housingrequestid')
		records = [{'item1': t[0], 'item2': t[1]} for t in zip(recordPK, recordName)]
	elif table == "Owner":
		recordPK = Owner.objects.values_list('ownerid')
		recordName = Owner.objects.values_list('ownername', flat=True).order_by('ownerid')
		records = [{'item1': t[0], 'item2': t[1]} for t in zip(recordPK, recordName)]
	elif table == "Picture":
		recordPK = Picture.objects.values_list('pictureid')
		recordName = Picture.objects.values_list('filename', flat=True).order_by('pictureid')
		records = [{'item1': t[0], 'item2': t[1]} for t in zip(recordPK, recordName)]
	elif table == "RoomCost":
		recordPK = RoomCost.objects.values_list('roomid')
		recordName = RoomCost.objects.values_list('roomname', flat=True).order_by('roomid')
		records = [{'item1': t[0], 'item2': t[1]} for t in zip(recordPK, recordName)]
	elif table == "Propertytype":
		recordPK = Propertytype.objects.values_list('propertytypeid')
		recordName = Propertytype.objects.values_list('propertytypename', flat=True).order_by('propertytypeid')
		records = [{'item1': t[0], 'item2': t[1]} for t in zip(recordPK, recordName)]

	print(recordPK)
	print(recordName)

	# records = zip(recordPK, recordName)

	content = {
		'tableChoices' : TABLES_CHOICES,
		'tableName' : table,
		'records' : records,
	}

	return render(request, 'adminpage/tablePage.html', content)

def addAdditionalInfo(request):

	if request.method == "POST":
		form = addAdditionalinfoForm(request.POST)

		if form.is_valid():
			post = form.save()
			if '_addAnother' in request.POST:
				return HttpResponseRedirect(reverse('addAdditionalInfo', args=()))
			elif '_save' in request.POST:
				return HttpResponseRedirect(reverse('tablePage', args=("Additionalinfo",)))
			
	form = addAdditionalinfoForm()
	#print(form)

	content = {
		'tableChoices' : TABLES_CHOICES,
		'infoChoices' : INFOTYPE_CHOICES,
		'recordExist' : False,
		'form' : form,
	}

	return render(request, 'adminpage/recordAdditionalInfo.html', content)

def editAdditionalInfo(request, id):

	record = Additionalinfo.objects.get(additionalinfoid=id)
	if request.method=="GET":
		if '_delete' in request.GET:
			record.delete()
			return HttpResponseRedirect(reverse('tablePage', args=("Additionalinfo",)))
	if request.method == "POST":
		form = addAdditionalinfoForm(request.POST, instance=record)
		if form.is_valid():
			post = form.save()
			if '_addAnother' in request.POST:
				return HttpResponseRedirect(reverse('addAdditionalInfo', args=()))
			elif '_save' in request.POST:
				return HttpResponseRedirect(reverse('tablePage', args=("Additionalinfo",)))
			
	form = addAdditionalinfoForm(instance=record)

	content = {
		'tableChoices' : TABLES_CHOICES,
		'infoChoices' : INFOTYPE_CHOICES,
		'recordExist' : True,
		# 'additionalinfotype' : amenity, facility or rule
		'record' : record, 				#Ito yung record na result ng query sa db
		'form' : form,
	}

	return render(request, 'adminpage/recordAdditionalInfo.html', content)

def addArea(request):

	form = addAreaForm()

	content = {
		'tableChoices' : TABLES_CHOICES,
		'recordExist' : False,
		'form' : form,
	}

	return render(request, 'adminpage/recordArea.html', content)

def editArea(request, id):

	content = {
		'tableChoices' : TABLES_CHOICES,
		'recordExist' : True,
		# 'record' : record, 				Ito yung record na result ng query sa db
	}

	return render(request, 'adminpage/recordArea.html', content)

def addContact(request):

	form = addContactForm()

	content = {
		'tableChoices' : TABLES_CHOICES,
		#'ownerChoices' :  query of all owners in Owner table
		'recordExist' : False,
		'form' : form,
	}

	return render(request, 'adminpage/recordContact.html', content)

def editContact(request, id):

	content = {
		'tableChoices' : TABLES_CHOICES,
		#'ownerChoices' :  query of all owners in Owner table 
		'recordExist' : True,
		# 'record' : record, 				Ito yung record na result ng query sa db
	}

	return render(request, 'adminpage/recordContact.html', content)

def editFeedback(request, id):

	form = addFeedbackForm()

	content = {
		'tableChoices' : TABLES_CHOICES,
		'statusChoices' :  FEEDBACK_STATUS_CHOICES,
		# 'status' : pending, approved or not approved
		'recordExist' : True,
		# 'record' : record, 				Ito yung record na result ng query sa db
		'form' : form,
	}

	return render(request, 'adminpage/recordFeedback.html', content)

def addHousetype(request):

	form = addHousetypeForm()

	content = {
		'tableChoices' : TABLES_CHOICES,
		'recordExist' : False,
		'form' : form,
	}

	return render(request, 'adminpage/recordHousetype.html', content)

def editHousetype(request, id):

	content = {
		'tableChoices' : TABLES_CHOICES,
		'recordExist' : True,
		# 'record' : record, 				Ito yung record na result ng query sa db
	}

	return render(request, 'adminpage/recordHousetype.html', content)

def addHousing(request):
	
	if request.method == "POST":
		form = addHousingForm(request.POST)

		if form.is_valid():
			post = form.save()
			if '_addAnother' in request.POST:
				return HttpResponseRedirect(reverse('addHousing', args=()))
			elif '_save' in request.POST:
				return HttpResponseRedirect(reverse('tablePage', args=("Housing",)))
			
	form = addHousingForm()
	#print(form)

	content = {
		'tableChoices' : TABLES_CHOICES,
		'recordExist' : False,
		'form' : form,
	}

	return render(request, 'adminpage/recordHousing.html', content)

def editHousing(request, id):
	record = Housing.objects.get(housingid=id)
	if request.method=="GET":
		if '_delete' in request.GET:
			record.delete()
			return HttpResponseRedirect(reverse('tablePage', args=("Housing",)))
	if request.method == "POST":
		form = addHousingForm(request.POST, instance=record)
		if form.is_valid():
			post = form.save()
			if '_addAnother' in request.POST:
				return HttpResponseRedirect(reverse('addHousing', args=()))
			elif '_save' in request.POST:
				return HttpResponseRedirect(reverse('tablePage', args=("Housing",)))
			
	form = addHousingForm(instance=record)

	idVal = int(id[1])
	print(idVal)
	housing = Housing.objects.get(pk=idVal)
	# form = addHousingForm(instance=housing)
	areaChoices = Area.objects.all()
	propertytypeChoices = Propertytype.objects.all()
	housetypeChoices = Housetype.objects.all()

	if request.method == "POST":
		# houseModel = addHousingForm(request.POST, instance=housing)
		houseName = request.POST['name']
		houseArea = request.POST['area']
		areaVal = Area.objects.filter(areaid=houseArea).first()
		houseAddress = request.POST['address']
		housepType = request.POST['propertytype']
		pTypeVal = Propertytype.objects.filter(propertytypeid=housepType).first()
		houseType = request.POST['housetype']
		houseTypeVal = Housetype.objects.filter(housetypeid=houseType).first()

		houseModel = Housing(housingname=houseName, area=areaVal, address=houseAddress, propertytype=pTypeVal,
						 housetype=houseTypeVal, createdby="dummyuser", lastediteddate="dummyuser")
		houseModel.save()

	content = {
		'tableChoices' : TABLES_CHOICES,
		'recordExist' : True,
		'record' : record, 				#Ito yung record na result ng query sa db
		'form' : form,
	}

	return render(request, 'adminpage/recordHousing.html', content)

def addPropertytype(request):

	form = addPropertytypeForm()

	content = {
		'tableChoices' : TABLES_CHOICES,
		'recordExist' : False,
		'form' : form,
	}

	return render(request, 'adminpage/recordPropertytype.html', content)

def editPropertytype(request, id):

	content = {
		'tableChoices' : TABLES_CHOICES,
		'recordExist' : True,
		# 'record' : record, 				Ito yung record na result ng query sa db
	}

	return render(request, 'adminpage/recordPropertytype.html', content)

def editRequest(request, id):

	form = addRequestForm()

	content = {
		'tableChoices' : TABLES_CHOICES,
		'typeChoices' : REQUEST_TYPE_CHOICES,
		'statusChoices' : REQUEST_STATUS_CHOICES,
		'recordExist' : True,
		# 'reqtype' : add, update or delete
		# 'status' : NOT YET EVALUATED, CONTENT COMPLETE, CONTENT CORRECT or REQUEST DONE
		# 'record' : record, 				Ito yung record na result ng query sa db
		'form' : form,
	}

	return render(request, 'adminpage/recordRequest.html', content)

def addHousingAdditionalInfo(request):

	form = addHousingAddtnlinfoForm()

	content = {
		'tableChoices' : TABLES_CHOICES,
		#'infoChoices' :    query of all records in additionalinfo table 
		#'housingChoices' :    query of all records in housing table 
		'recordExist' : False,
		'form' : form,
	}

	return render(request, 'adminpage/recordHousingAdditionalInfo.html', content)

def editHousingAdditionalInfo(request, id):

	content = {
		'tableChoices' : TABLES_CHOICES,
		#'infoChoices' :    query of all records in additionalinfo table 
		#'housingChoices' :    query of all records in housing table 
		'recordExist' : True,
		# 'record' : record, 				Ito yung record na result ng query sa db
	}

	return render(request, 'adminpage/recordHousingAdditionalInfo.html', content)

def addHousingOwner(request):

	form = addHousingOwnerForm()

	content = {
		'tableChoices' : TABLES_CHOICES,
		#'ownerChoices' :    query of all records in Owner table 
		#'housingChoices' :    query of all records in housing table 
		'recordExist' : False,
		'form' : form,
	}

	return render(request, 'adminpage/recordHousingOwner.html', content)

def editHousingOwner(request, id):

	content = {
		'tableChoices' : TABLES_CHOICES,
		#'ownerChoices' :    query of all records in Owner table 
		#'housingChoices' :    query of all records in housing table 
		'recordExist' : True,
		# 'record' : record, 				Ito yung record na result ng query sa db
	}

	return render(request, 'adminpage/recordHousingOwner.html', content)

def addHousingRequest(request):

	form = addHousingRequestForm()

	content = {
		'tableChoices' : TABLES_CHOICES,
		#'requestChoices' :    query of all records in Request table 
		#'housingChoices' :    query of all records in housing table 
		'recordExist' : False,
		'form' : form,
	}

	return render(request, 'adminpage/recordHousingRequest.html', content)

def editHousingRequest(request, id):

	content = {
		'tableChoices' : TABLES_CHOICES,
		#'requestChoices' :    query of all records in Request table 
		#'housingChoices' :    query of all records in housing table 
		'recordExist' : True,
		# 'record' : record, 				Ito yung record na result ng query sa db
	}

	return render(request, 'adminpage/recordHousingRequest.html', content)

def addPicture(request):

	form = addPictureForm()

	content = {
		'tableChoices' : TABLES_CHOICES, 
		#'housingChoices' :    query of all records in housing table 
		'recordExist' : False,
		'form' : form,
	}

	return render(request, 'adminpage/recordPicture.html', content)

def editPicture(request, id):

	content = {
		'tableChoices' : TABLES_CHOICES,
		#'housingChoices' :    query of all records in housing table 
		'recordExist' : True,
		# 'record' : record, 				Ito yung record na result ng query sa db
	}

	return render(request, 'adminpage/recordPicture.html', content)

def addRoomCost(request):

	form = addRoomCostForm()

	content = {
		'tableChoices' : TABLES_CHOICES, 
		#'housingChoices' :    query of all records in housing table 
		'recordExist' : False,
		'form' : form,
	}

	return render(request, 'adminpage/recordRoomCost.html', content)

def editRoomCost(request, id):

	content = {
		'tableChoices' : TABLES_CHOICES,
		#'housingChoices' :    query of all records in housing table 
		'recordExist' : True,
		# 'record' : record, 				Ito yung record na result ng query sa db
	}

	return render(request, 'adminpage/recordRoomCost.html', content)

def addOwner(request):

	form = addOwnerForm()

	content = {
		'tableChoices' : TABLES_CHOICES, 
		'recordExist' : False,
		'form' : form,
	}

	return render(request, 'adminpage/recordOwner.html', content)

def editOwner(request, id):

	content = {
		'tableChoices' : TABLES_CHOICES,
		'recordExist' : True,
		# 'record' : record, 				Ito yung record na result ng query sa db
	}

	return render(request, 'adminpage/recordOwner.html', content)
