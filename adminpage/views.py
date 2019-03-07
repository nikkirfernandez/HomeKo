# This is a course requirement for CS 192 Software Engineering II under the supervision of Asst. Prof. Ma. Rowena C. Solamo of the Department of Computer Science, College of Engineering, University of the Philippines, Diliman for the AY 2018-2019.

# CODE HISTORY #
# Kasilag

# File creation date: Feb. 19, 2019

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.db.models.functions import Concat
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from .choices import *
from .forms import *
from mainpage.models import *

# Create your views here.

def adminlogin(request):
	incorrect = False
	if request.method == "POST":
		form = AdminLogin(request.POST)
		if form.is_valid():
			uname = request.POST['uname']
			pw = request.POST['pw']
			user = authenticate(request, username=uname, password=pw)
			if user is not None:
				login(request, user)
				return HttpResponseRedirect(reverse('home'))
			else:
				incorrect = True
	form = AdminLogin()

	content = {
		'tableChoices' : TABLES_CHOICES,
		'form' : form,
		'incorrect' : incorrect,
	}

	return render(request, 'adminpage/login.html', content)

def adminlogout(request):
	logout(request)
	
	return HttpResponseRedirect(reverse('adminlogin'))

@login_required(login_url='/adminpage/login/')
def home(request):

	content = {
		'tableChoices' : TABLES_CHOICES,
	}

	return render(request, 'adminpage/adminHome.html', content)

@login_required(login_url='/adminpage/login/')
def tablePage(request, table):

	# recordPK is a list of the primary keys 
	# recordName is a list of names that represent the records
    # records = [{'item1': t[0], 'item2': t[1]} for t in zip(recordPK, recordName)]

	if table == "Area":
		recordPK = Area.objects.values_list('areaid', flat=True).order_by('areaid')
		recordName = Area.objects.values_list('areaname', flat=True).order_by('areaid')
	elif table=="Housing":
		recordPK = Housing.objects.values_list('housingid', flat=True).order_by('housingid')
		recordName = Housing.objects.values_list('housingname', flat=True).order_by('housingid')		
	elif table=="Additionalinfo":
		recordPK = Additionalinfo.objects.values_list('additionalinfoid', flat=True).order_by('additionalinfoid')
		recordName = Additionalinfo.objects.values_list('additionalinfoname', flat=True).order_by('additionalinfoid')
	elif table == "Contact":
		recordPK = Contact.objects.values_list('contactid', flat=True).order_by('contactid')
		recordName = Contact.objects.values_list('contactno', flat=True).order_by('contactid')
	elif table == "Feedback":
		recordPending = Feedback.objects.filter(status=1).order_by('feedbackid')
		recordApproved = Feedback.objects.filter(status=2).order_by('feedbackid')
		recordNotApproved = Feedback.objects.filter(status=3).order_by('feedbackid')
		content = {
			'tableChoices' : TABLES_CHOICES,
			'tableName' : table,     
			'pending' : recordPending,
			'approved' : recordApproved,
			'notapproved' : recordNotApproved,    
		}
		return render(request, 'adminpage/feedbackTabs.html', content)
	elif table == "Housetype":
		recordPK = Housetype.objects.values_list('housetypeid', flat=True).order_by('housetypeid')
		recordName = Housetype.objects.values_list('housetypename', flat=True).order_by('housetypeid')
	elif table == "HousingAdditionalinfo":
		recordPK = HousingAdditionalInfo.objects.values_list('housingadditionalinfoid', flat=True).order_by('housingadditionalinfoid')
		recordName = HousingAdditionalInfo.objects.values_list('housingid__housingname', 'additionalinfoid__additionalinfoname').order_by('housingadditionalinfoid')
	elif table == "Request":
		#TODO ######## EDIT THIS ######## RECORDNAME: REQTYPE AND FIRST 5 WORDS OF REQUEST
		recordPK = Request.objects.values_list('requestid', flat=True).order_by('requestid')
		recordName = Request.objects.values_list('reqtype', flat=True).order_by('requestid')
	
		recordPending = Request.objects.filter(status=1).order_by('requestid')
		recordApproved = Request.objects.filter(status=2).order_by('requestid')
		recordNotApproved = Request.objects.filter(status=3).order_by('requestid')

		content = {
			'tableChoices' : TABLES_CHOICES,
			'tableName' : table,     
			'pending' : recordPending,
			'approved' : recordApproved,
			'notapproved' : recordNotApproved,    
		}
		return render(request, 'adminpage/requestTabs.html', content)
	elif table == "HousingRequest":
		recordPK = HousingRequest.objects.values_list('housingrequestid', flat=True).order_by('housingrequestid')
		recordName = HousingRequest.objects.values_list('housingid__housingname', 'requestid__reqtype').order_by('housingrequestid')
	elif table == "Owner":
		recordPK = Owner.objects.values_list('ownerid', flat=True).order_by('ownerid')
		recordName = Owner.objects.values_list('ownername', flat=True).order_by('ownerid')
	elif table == "HousingOwner":
		recordPK = HousingOwner.objects.values_list('housingownerid', flat=True).order_by('housingownerid')
		recordName = HousingOwner.objects.values_list('ownerid__ownername', 'housingid__housingname').order_by('housingownerid')
	elif table == "Picture": 
		recordPK = Picture.objects.values_list('pictureid', flat=True).order_by('pictureid')
		recordName = Picture.objects.values_list('filename', flat=True).order_by('pictureid')
	elif table == "RoomCost":
		recordPK = RoomCost.objects.values_list('roomid', flat=True).order_by('roomid')
		recordName = RoomCost.objects.values_list('housingid__housingname', 'roomname').order_by('roomid')
	elif table == "Propertytype":
		recordPK = Propertytype.objects.values_list('propertytypeid', flat=True).order_by('propertytypeid')
		recordName = Propertytype.objects.values_list('propertytypename', flat=True).order_by('propertytypeid')

	content = {
		'tableChoices' : TABLES_CHOICES,
		'tableName' : table,
		'records' : records,
	}

	return render(request, 'adminpage/tablePage.html', content)

@login_required(login_url='/adminpage/login/')
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

@login_required(login_url='/adminpage/login/')
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

@login_required(login_url='/adminpage/login/')
def addArea(request):
	form = addAreaForm(request.POST)

	if request.method == 'POST':

		if form.is_valid():
			newArea = form.save()
			if '_addAnother' in request.POST:
				return HttpResponseRedirect(reverse('addArea', args=()))
			elif '_save' in request.POST:
				return HttpResponseRedirect(reverse('tablePage', args=("Area",)))



	content = {
		'tableChoices' : TABLES_CHOICES,
		'recordExist' : False,
		'form' : form,
	}

	return render(request, 'adminpage/recordArea.html', content)

@login_required(login_url='/adminpage/login/')
def editArea(request, id):

	# print(areaEntry)
	areaEntry = Area.objects.get(pk=id)
	form = addAreaForm(request.POST, instance=areaEntry)
	if request.method=="GET":
		if '_delete' in request.GET:
			areaEntry.delete()
			return HttpResponseRedirect(reverse('tablePage', args=("Area",)))
	if request.method == 'POST':
		if form.is_valid():
			newArea = form.save()
			if '_addAnother' in request.POST:
				return HttpResponseRedirect(reverse('addArea', args=()))
			elif '_save' in request.POST:
				return HttpResponseRedirect(reverse('tablePage', args=("Area",)))

	content = {
		'tableChoices' : TABLES_CHOICES,
		'recordExist' : True,
		'form' : form
		# 'record' : record, 				Ito yung record na result ng query sa db
	}

	return render(request, 'adminpage/recordArea.html', content)

@login_required(login_url='/adminpage/login/')
def addContact(request):

	form = addContactForm(request.POST)
	if request.method == 'POST':
		if form.is_valid():
			newArea = form.save()
			if '_addAnother' in request.POST:
				return HttpResponseRedirect(reverse('addContact', args=()))
			elif '_save' in request.POST:
				return HttpResponseRedirect(reverse('tablePage', args=("Contact",)))


	content = {
		'tableChoices' : TABLES_CHOICES,
		#'ownerChoices' :  query of all owners in Owner table
		'recordExist' : False,
		'form' : form,
	}

	return render(request, 'adminpage/recordContact.html', content)

@login_required(login_url='/adminpage/login/')
def editContact(request, id):

	contactEntry = Contact.objects.get(pk=id)
	form = addContactForm(request.POST, instance=contactEntry)
	if request.method == "GET":
		if '_delete' in request.GET:
			contactEntry.delete()
			return HttpResponseRedirect(reverse('tablePage', args=("Contact",)))
	if request.method == 'POST':
		if form.is_valid():
			newContact = form.save()
			if '_addAnother' in request.POST:
				return HttpResponseRedirect(reverse('addContact', args=()))
			elif '_save' in request.POST:
				return HttpResponseRedirect(reverse('tablePage', args=("Contact",)))

	content = {
		'tableChoices' : TABLES_CHOICES,
		#'ownerChoices' :  query of all owners in Owner table
		'recordExist' : True,
		'form' : form
		# 'record' : record, 				Ito yung record na result ng query sa db
	}

	return render(request, 'adminpage/recordContact.html', content)

@login_required(login_url='/adminpage/login/')
def editFeedback(request, id):

	form = addFeedbackForm(request.POST)
	print("ff")
	if request.method == 'POST':
		if form.is_valid():
			print('sfg')
			newFeedback = form.save()
			if '_addAnother' in request.POST:
				return HttpResponseRedirect(reverse('addFeedback', args=()))
			elif '_save' in request.POST:
				return HttpResponseRedirect(reverse('tablePage', args=("Feedback",)))


	content = {
		'tableChoices' : TABLES_CHOICES,
		#'ownerChoices' :  query of all owners in Owner table
		'recordExist' : False,
		'form' : form,
	}

	return render(request, 'adminpage/recordFeedback.html', content)

# @login_required(login_url='/adminpage/login/')
# def addHousetype(request):

def editFeedback(request, id):
	feedbackEntry = Housetype.objects.get(pk=id)
	form = addFeedbackForm(request.POST, instance=feedbackEntry)
	if request.method == "GET":
		print("delete")
		if '_delete' in request.GET:
			feedbackEntry.delete()
			return HttpResponseRedirect(reverse('tablePage', args=("Feedback",)))
	if request.method == 'POST':
		if form.is_valid():
			newFeedback = form.save()
			if '_addAnother' in request.POST:
				return HttpResponseRedirect(reverse('addFeedback', args=()))
			elif '_save' in request.POST:
				return HttpResponseRedirect(reverse('tablePage', args=("Feedback",)))


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

	form = addHousetypeForm(request.POST)
	if request.method == 'POST':
		if form.is_valid():
			newHousetype = form.save()
			if '_addAnother' in request.POST:
				return HttpResponseRedirect(reverse('addHousetype', args=()))
			elif '_save' in request.POST:
				return HttpResponseRedirect(reverse('tablePage', args=("Housetype",)))
	content = {
		'tableChoices' : TABLES_CHOICES,
		'recordExist' : False,
		'form' : form,
	}

	return render(request, 'adminpage/recordHousetype.html', content)

@login_required(login_url='/adminpage/login/')
def editHousetype(request, id):

	HousetypeEntry = Housetype.objects.get(pk=id)
	form = addHousetypeForm(request.POST, instance=HousetypeEntry)
	if request.method == "GET":
		if '_delete' in request.GET:
			HousetypeEntry.delete()
			return HttpResponseRedirect(reverse('tablePage', args=("Housetype",)))
	if request.method == 'POST':
		if form.is_valid():
			newHousetype = form.save()
			if '_addAnother' in request.POST:
				return HttpResponseRedirect(reverse('addHousetype', args=()))
			elif '_save' in request.POST:
				return HttpResponseRedirect(reverse('tablePage', args=("Housetype",)))
	content = {
		'tableChoices' : TABLES_CHOICES,
		'recordExist' : True,
		# 'record' : record, 				Ito yung record na result ng query sa db
		'form' : form
	}

	return render(request, 'adminpage/recordHousetype.html', content)

@login_required(login_url='/adminpage/login/')
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

@login_required(login_url='/adminpage/login/')
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
	#
	# idVal = int(id[1])
	# print(idVal)
	# housing = Housing.objects.get(pk=idVal)
	# # form = addHousingForm(instance=housing)
	# areaChoices = Area.objects.all()
	# propertytypeChoices = Propertytype.objects.all()
	# housetypeChoices = Housetype.objects.all()
	#
	# if request.method == "POST":
	# 	# houseModel = addHousingForm(request.POST, instance=housing)
	# 	houseName = request.POST['name']
	# 	houseArea = request.POST['area']
	# 	areaVal = Area.objects.filter(areaid=houseArea).first()
	# 	houseAddress = request.POST['address']
	# 	housepType = request.POST['propertytype']
	# 	pTypeVal = Propertytype.objects.filter(propertytypeid=housepType).first()
	# 	houseType = request.POST['housetype']
	# 	houseTypeVal = Housetype.objects.filter(housetypeid=houseType).first()
	#
	# 	houseModel = Housing(housingname=houseName, area=areaVal, address=houseAddress, propertytype=pTypeVal,
	# 					 housetype=houseTypeVal, createdby="dummyuser", lastediteddate="dummyuser")
	# 	houseModel.save()

	content = {
		'tableChoices' : TABLES_CHOICES,
		'recordExist' : True,
		'record' : record, 				#Ito yung record na result ng query sa db
		'form' : form,
	}

	return render(request, 'adminpage/recordHousing.html', content)

@login_required(login_url='/adminpage/login/')
def addPropertytype(request):

	form = addPropertytypeForm(request.POST)
	if request.method == 'POST':
		if form.is_valid():
			newProperty = form.save()
			if '_addAnother' in request.POST:
				return HttpResponseRedirect(reverse('addPropertytype', args=()))
			elif '_save' in request.POST:
				return HttpResponseRedirect(reverse('tablePage', args=("Propertytype",)))


	content = {
		'tableChoices' : TABLES_CHOICES,
		'recordExist' : False,
		'form' : form,
	}

	return render(request, 'adminpage/recordPropertytype.html', content)

@login_required(login_url='/adminpage/login/')
def editPropertytype(request, id):

	dbEntry = Propertytype.objects.get(pk=id)
	form = addPropertytypeForm(request.POST, instance=dbEntry)
	if request.method == "GET":
		if '_delete' in request.GET:
			dbEntry.delete()
			return HttpResponseRedirect(reverse('tablePage', args=("Propertytype",)))
	if request.method == 'POST':
		if form.is_valid():
			newForm = form.save()
			if '_addAnother' in request.POST:
				return HttpResponseRedirect(reverse('addPropertytype', args=()))
			elif '_save' in request.POST:
				return HttpResponseRedirect(reverse('tablePage', args=("Propertytype",)))

	content = {
		'tableChoices' : TABLES_CHOICES,
		'recordExist' : True,
		'form' : form
		# 'record' : record, 				Ito yung record na result ng query sa db
	}

	return render(request, 'adminpage/recordPropertytype.html', content)

@login_required(login_url='/adminpage/login/')
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

@login_required(login_url='/adminpage/login/')
def addHousingAdditionalInfo(request):
	form = addHousingAddtionalinfoForm(request.POST)
	if request.method == 'POST':
		if form.is_valid():
			newForm = form.save()
			if '_addAnother' in request.POST:
				return HttpResponseRedirect(reverse('addHousingAddtionalinfo', args=()))
			elif '_save' in request.POST:
				return HttpResponseRedirect(reverse('tablePage', args=("HousingAdditionalinfo",)))


	content = {
		'tableChoices' : TABLES_CHOICES,
		#'infoChoices' :    query of all records in additionalinfo table
		#'housingChoices' :    query of all records in housing table
		'recordExist' : False,
		'form' : form,
	}

	return render(request, 'adminpage/recordHousingAdditionalInfo.html', content)

@login_required(login_url='/adminpage/login/')
def editHousingAdditionalInfo(request, id):
	dbEntry = HousingAdditionalInfo.objects.get(pk=id)
	form = addHousingAddtnlinfoForm(request.POST, instance=dbEntry)
	if request.method == "GET":
		if '_delete' in request.GET:
			dbEntry.delete()
			return HttpResponseRedirect(reverse('tablePage', args=("HousingAdditionalInfo",)))
	if request.method == 'POST':
		if form.is_valid():
			newForm = form.save()
			if '_addAnother' in request.POST:
				return HttpResponseRedirect(reverse('addHousingAddtionalinfo', args=()))
			elif '_save' in request.POST:
				return HttpResponseRedirect(reverse('tablePage', args=("HousingAdditionalInfo",)))


	content = {
		'tableChoices' : TABLES_CHOICES,
		#'infoChoices' :    query of all records in additionalinfo table
		#'housingChoices' :    query of all records in housing table
		'recordExist' : True,
		# 'record' : record, 				Ito yung record na result ng query sa db
		'form' : form
	}

	return render(request, 'adminpage/recordHousingAdditionalInfo.html', content)

@login_required(login_url='/adminpage/login/')
def addHousingOwner(request):
	form = addHousingOwnerForm(request.POST)
	if request.method == 'POST':
		if form.is_valid():
			newForm = form.save()
			if '_addAnother' in request.POST:
				return HttpResponseRedirect(reverse('addHousingOwner', args=()))
			elif '_save' in request.POST:
				return HttpResponseRedirect(reverse('tablePage', args=("HousingOwner",)))

	content = {
		'tableChoices' : TABLES_CHOICES,
		#'ownerChoices' :    query of all records in Owner table
		#'housingChoices' :    query of all records in housing table
		'recordExist' : False,
		'form' : form,
	}

	return render(request, 'adminpage/recordHousingOwner.html', content)

@login_required(login_url='/adminpage/login/')
def editHousingOwner(request, id):
	dbEntry = HousingOwner.objects.get(pk=id)
	form = addHousingOwnerForm(request.POST, instance=dbEntry)
	if request.method == "GET":
		if '_delete' in request.GET:
			dbEntry.delete()
			return HttpResponseRedirect(reverse('tablePage', args=("HousingOwner",)))
	if request.method == 'POST':
		if form.is_valid():
			newForm = form.save()
			if '_addAnother' in request.POST:
				return HttpResponseRedirect(reverse('addHousingOwner', args=()))
			elif '_save' in request.POST:
				return HttpResponseRedirect(reverse('tablePage', args=("HousingOwner",)))


	content = {
		'tableChoices' : TABLES_CHOICES,
		#'ownerChoices' :    query of all records in Owner table
		#'housingChoices' :    query of all records in housing table
		'recordExist' : True,
		# 'record' : record, 				Ito yung record na result ng query sa db
		'form' : form
	}

	return render(request, 'adminpage/recordHousingOwner.html', content)

@login_required(login_url='/adminpage/login/')
def addHousingRequest(request):

	form = addHousingRequestForm(request.POST)
	if request.method == 'POST':
		if form.is_valid():
			newForm = form.save()
			if '_addAnother' in request.POST:
				return HttpResponseRedirect(reverse('addHousingRequest', args=()))
			elif '_save' in request.POST:
				return HttpResponseRedirect(reverse('tablePage', args=("HousingRequest",)))


	content = {
		'tableChoices' : TABLES_CHOICES,
		#'requestChoices' :    query of all records in Request table
		#'housingChoices' :    query of all records in housing table
		'recordExist' : False,
		'form' : form,
	}

	return render(request, 'adminpage/recordHousingRequest.html', content)

@login_required(login_url='/adminpage/login/')
def editHousingRequest(request, id):
	dbEntry = HousingRequest.objects.get(pk=id)
	form = addHousingRequestForm(request.POST, instance=dbEntry)
	if request.method == "GET":
		if '_delete' in request.GET:
			dbEntry.delete()
			return HttpResponseRedirect(reverse('tablePage', args=("HousingRequest",)))
	if request.method == 'POST':
		if form.is_valid():
			newForm = form.save()
			if '_addAnother' in request.POST:
				return HttpResponseRedirect(reverse('addHousingRequest', args=()))
			elif '_save' in request.POST:
				return HttpResponseRedirect(reverse('tablePage', args=("HousingRequest",)))
	content = {
		'tableChoices' : TABLES_CHOICES,
		#'requestChoices' :    query of all records in Request table
		#'housingChoices' :    query of all records in housing table
		'recordExist' : True,
		# 'record' : record, 				Ito yung record na result ng query sa db
		'form' : form
	}

	return render(request, 'adminpage/recordHousingRequest.html', content)

@login_required(login_url='/adminpage/login/')
def addPicture(request):

	form = addPictureForm()

	content = {
		'tableChoices' : TABLES_CHOICES,
		#'housingChoices' :    query of all records in housing table
		'recordExist' : False,
		'form' : form,
	}

	return render(request, 'adminpage/recordPicture.html', content)

@login_required(login_url='/adminpage/login/')
def editPicture(request, id):

	content = {
		'tableChoices' : TABLES_CHOICES,
		#'housingChoices' :    query of all records in housing table
		'recordExist' : True,
		# 'record' : record, 				Ito yung record na result ng query sa db
	}

	return render(request, 'adminpage/recordPicture.html', content)

@login_required(login_url='/adminpage/login/')
def addRoomCost(request):
	form = addRoomCostForm(request.POST)
	if request.method == 'POST':
		if form.is_valid():
			newForm = form.save()
			if '_addAnother' in request.POST:
				return HttpResponseRedirect(reverse('addRoomCost', args=()))
			elif '_save' in request.POST:
				return HttpResponseRedirect(reverse('tablePage', args=("RoomCost",)))

	content = {
		'tableChoices' : TABLES_CHOICES,
		#'housingChoices' :    query of all records in housing table
		'recordExist' : False,
		'form' : form,
	}

	return render(request, 'adminpage/recordRoomCost.html', content)

@login_required(login_url='/adminpage/login/')
def editRoomCost(request, id):
	dbEntry = RoomCost.objects.get(pk=id)
	form = addRoomCostForm(request.POST, instance=dbEntry)
	if request.method == "GET":
		if '_delete' in request.GET:
			dbEntry.delete()
			return HttpResponseRedirect(reverse('tablePage', args=("RoomCost",)))
	if request.method == 'POST':
		if form.is_valid():
			newForm = form.save()
			if '_addAnother' in request.POST:
				return HttpResponseRedirect(reverse('addRoomCost', args=()))
			elif '_save' in request.POST:
				return HttpResponseRedirect(reverse('tablePage', args=("RoomCost",)))
	content = {
		'tableChoices' : TABLES_CHOICES,
		#'housingChoices' :    query of all records in housing table
		'recordExist' : True,
		# 'record' : record, 				Ito yung record na result ng query sa db
		'form' : form
	}

	return render(request, 'adminpage/recordRoomCost.html', content)

@login_required(login_url='/adminpage/login/')
def addOwner(request):
	form = addOwnerForm(request.POST)
	if request.method == 'POST':
		if form.is_valid():
			newForm = form.save()
			if '_addAnother' in request.POST:
				return HttpResponseRedirect(reverse('addOwner', args=()))
			elif '_save' in request.POST:
				return HttpResponseRedirect(reverse('tablePage', args=("Owner",)))

	content = {
		'tableChoices' : TABLES_CHOICES,
		'recordExist' : False,
		'form' : form,
	}

	return render(request, 'adminpage/recordOwner.html', content)

@login_required(login_url='/adminpage/login/')
def editOwner(request, id):
	dbEntry = Owner.objects.get(pk=id)
	form = addOwnerForm(request.POST, instance=dbEntry)
	if request.method == "GET":
		if '_delete' in request.GET:
			dbEntry.delete()
			return HttpResponseRedirect(reverse('tablePage', args=("Owner",)))
	if request.method == 'POST':
		if form.is_valid():
			newForm = form.save()
			if '_addAnother' in request.POST:
				return HttpResponseRedirect(reverse('addOwner', args=()))
			elif '_save' in request.POST:
				return HttpResponseRedirect(reverse('tablePage', args=("Owner",)))
	content = {
		'tableChoices' : TABLES_CHOICES,
		'recordExist' : True,
		# 'record' : record, 				Ito yung record na result ng query sa db
		'form' : form
	}

	return render(request, 'adminpage/recordOwner.html', content)
