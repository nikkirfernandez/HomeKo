from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .choices import *
from .forms import *
from .models import *

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
	# recordPK is a list of the primary keys 
	# recordName is a list of names that represent the records
    # records = [{'item1': t[0], 'item2': t[1]} for t in zip(recordPK, recordName)]

	records = Area.objects.all()
	print(records)

	content = {
		'tableChoices' : TABLES_CHOICES,
		'tableName' : table,
		'records' : records,
	}

	return render(request, 'adminpage/tablePage.html', content)

def addAdditionalInfo(request):

	if request.method == "POST":
		additionalinfoName = request.POST['name']
		additionalinfoType = request.POST['infotype']
		additionalinfoModel = Additionalinfo(additionalinfoname=additionalinfoName, additionalinfotype=additionalinfoType)
		additionalinfoModel.save()

	content = {
		'tableChoices' : TABLES_CHOICES,
		'infoChoices' : INFOTYPE_CHOICES,
		'recordExist' : False,
	}

	return render(request, 'adminpage/recordAdditionalInfo.html', content)

def editAdditionalInfo(request, id):

	content = {
		'tableChoices' : TABLES_CHOICES,
		'infoChoices' : INFOTYPE_CHOICES,
		'recordExist' : True,
		# 'additionalinfotype' : amenity, facility or rule
		# 'record' : record, 				Ito yung record na result ng query sa db
	}

	return render(request, 'adminpage/recordAdditionalInfo.html', content)

def addArea(request):
	# if request.method == "POST" :
	# 	addAreaForm1 = addAreaForm(request.POST)
	# 	print(addAreaForm1.errors)
	# 	if addAreaForm1.is_valid():
	# 		print("valid")
	# 		text = addAreaForm1.cleaned_data['name']
	# 		addAreaForm.save()
	#
	# addAreaForm1 = addAreaForm()

	if request.method == "POST":
		areaName = request.POST['name']
		areaModel = Area(areaname=areaName)
		areaModel.save()

	content = {
		'tableChoices' : TABLES_CHOICES,
		'recordExist' : False,
		# 'text' : areaName
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

	content = {
		'tableChoices' : TABLES_CHOICES,
		#'ownerChoices' :  query of all owners in Owner table
		'recordExist' : False,
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

	content = {
		'tableChoices' : TABLES_CHOICES,
		'statusChoices' :  FEEDBACK_STATUS_CHOICES,
		# 'status' : pending, approved or not approved
		'recordExist' : True,
		# 'record' : record, 				Ito yung record na result ng query sa db
	}

	return render(request, 'adminpage/recordFeedback.html', content)

def addHousetype(request):

	content = {
		'tableChoices' : TABLES_CHOICES,
		'recordExist' : False,
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
	areaChoices = Area.objects.all()
	propertytypeChoices = Propertytype.objects.all()
	housetypeChoices = Housetype.objects.all()


	if request.method == "POST":
		houseName = request.POST['name']
		houseArea = request.POST['area']
		areaVal = Area.objects.filter(areaid=houseArea).first()
		houseAddress = request.POST['address']
		housepType = request.POST['propertytype']
		pTypeVal = Propertytype.objects.filter(propertytypeid=housepType).first()
		houseType = request.POST['housetype']
		houseTypeVal = Housetype.objects.filter(housetypeid=houseType).first()

		houseModel = Housing(housingname=houseName, area=areaVal, address=houseAddress, propertytype=pTypeVal, housetype=houseTypeVal, createdby="dummyuser", lastediteddate="dummyuser")
		houseModel.save()

	content = {
		'tableChoices' : TABLES_CHOICES,
		'areaChoices' :  areaChoices,
		'propertytypeChoices' :  propertytypeChoices,
		'housetypeChoices' :  housetypeChoices,
		'recordExist' : False,
	}

	return render(request, 'adminpage/recordHousing.html', content)

def editHousing(request, id):

	content = {
		'tableChoices' : TABLES_CHOICES,
		#'areaChoices' :  query of all records in Area table 
		#'propertytypeChoices' :  query of all records in propertytype table 
		#'housetypeChoices' :  query of all records in housetype table 
		'recordExist' : True,
		# 'record' : record, 				Ito yung record na result ng query sa db
	}

	return render(request, 'adminpage/recordHousing.html', content)

def addPropertytype(request):

	content = {
		'tableChoices' : TABLES_CHOICES,
		'recordExist' : False,
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

	content = {
		'tableChoices' : TABLES_CHOICES,
		'typeChoices' : REQUEST_TYPE_CHOICES,
		'statusChoices' : REQUEST_STATUS_CHOICES,
		'recordExist' : True,
		# 'reqtype' : add, update or delete
		# 'status' : NOT YET EVALUATED, CONTENT COMPLETE, CONTENT CORRECT or REQUEST DONE
		# 'record' : record, 				Ito yung record na result ng query sa db
	}

	return render(request, 'adminpage/recordRequest.html', content)

def addHousingAdditionalInfo(request):

	content = {
		'tableChoices' : TABLES_CHOICES,
		#'infoChoices' :    query of all records in additionalinfo table 
		#'housingChoices' :    query of all records in housing table 
		'recordExist' : False,
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

	content = {
		'tableChoices' : TABLES_CHOICES,
		#'ownerChoices' :    query of all records in Owner table 
		#'housingChoices' :    query of all records in housing table 
		'recordExist' : False,
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

	content = {
		'tableChoices' : TABLES_CHOICES,
		#'requestChoices' :    query of all records in Request table 
		#'housingChoices' :    query of all records in housing table 
		'recordExist' : False,
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

	content = {
		'tableChoices' : TABLES_CHOICES, 
		#'housingChoices' :    query of all records in housing table 
		'recordExist' : False,
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

	content = {
		'tableChoices' : TABLES_CHOICES, 
		#'housingChoices' :    query of all records in housing table 
		'recordExist' : False,
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

	content = {
		'tableChoices' : TABLES_CHOICES, 
		'recordExist' : False,
	}

	return render(request, 'adminpage/recordOwner.html', content)

def editOwner(request, id):

	content = {
		'tableChoices' : TABLES_CHOICES,
		'recordExist' : True,
		# 'record' : record, 				Ito yung record na result ng query sa db
	}

	return render(request, 'adminpage/recordOwner.html', content)