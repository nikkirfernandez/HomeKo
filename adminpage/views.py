# This is a course requirement for CS 192 Software Engineering II under the supervision of Asst. Prof. Ma. Rowena C. Solamo of the Department of Computer Science, College of Engineering, University of the Philippines, Diliman for the AY 2018-2019.

# CODE HISTORY #
# Sontillano		# Feb 13, 2019		# created initial functions
# Kasilag     		# Feb 19, 2019		# addHousing, editHousing function definitions
# Sontillano		# Mar 3, 2019		# changed the code for addHousing and editHousing
# Fernandez		# Mar 6, 2019		# added log in for admin
# Sontillano		# Mar 7, 2019		# modified log in
# Kasilag			# Mar 7, 2019		# added definition for other functions
# Sontillano		# Mar 21, 2019		# fixed request processing
# File creation date: Feb. 13, 2019

import time

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.db.models.functions import Concat
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .choices import *
from .forms import *
from mainpage.models import *


# Method name: adminlogin
# Creation date: Feb 13, 2019 
# Purpose: View for the admin log in. Contains the authentication of username and password.
# Calling arguments: No arguments for calling this function.
# Required files: login.html
def adminlogin(request):
	if request.user.is_authenticated:
		if request.user.is_superuser:
			return HttpResponseRedirect(reverse('home'))
		else:
			return HttpResponseRedirect('/ownerpage/home')
	else:
		incorrect = False
		if request.method == "POST":
			form = AdminLogin(request.POST)
			if form.is_valid():
				uname = request.POST['uname']
				pw = request.POST['pw']
				user = authenticate(request, username=uname, password=pw)
				if user is not None:
					if user.is_superuser==1:    
						login(request, user)
						return HttpResponseRedirect(reverse('home'))
					else:
						incorrect = True
				else:
					incorrect = True
		form = AdminLogin()

		content = {
			'form' : form,
			'incorrect' : incorrect,
		}

		return render(request, 'adminpage/login.html', content)

# Method name: adminlogout
# Creation date: Feb 13, 2019 
# Purpose: Contains the admin log out functionality.
# Calling arguments: No arguments for calling this function.
# Required files:
@login_required(login_url='/adminpage/login/') 
def adminlogout(request):
	if request.user.is_superuser:
		logout(request)
	
	return HttpResponseRedirect(reverse('adminlogin'))

# Method name: home
# Creation date: Feb 13, 2019 
# Purpose: View for the admin home page. Contains the tables in the db.
# Calling arguments: No arguments for calling this function.
# Required files: adminHome.html
@login_required(login_url='/adminpage/login/')
def home(request):
	if request.user.is_superuser:
		content = {
			'tableChoices' : TABLES_CHOICES,
		}

		return render(request, 'adminpage/adminHome.html', content)
	else:
		return HttpResponseRedirect(reverse('adminlogin'))

# Method name: tablePage
# Creation date: Feb 13, 2019 
# Purpose: View for the records of a table. Contains the primary key and description of the record.
# Calling arguments: tablename
# Required files: tablePage.html
@login_required(login_url='/adminpage/login/')
def tablePage(request, table):
	if request.user.is_superuser:

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
			recordPending = Request.objects.filter(status=1).order_by('requestid')
			recordProgress = Request.objects.filter(status=2).order_by('requestid')
			recordDone = Request.objects.filter(status=3).order_by('requestid')
			recordNotApproved = Request.objects.filter(status=4).order_by('requestid')
			content = {
				'tableChoices' : TABLES_CHOICES,
				'tableName' : table,     
				'pending' : recordPending,
				'progress' : recordProgress,
				'done' : recordDone,    
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

		records = [{'item1': t[0], 'item2': t[1]} for t in zip(recordPK, recordName)]

		content = {
			'tableChoices' : TABLES_CHOICES,
			'tableName' : table,
			'records' : records,
		}

		return render(request, 'adminpage/tablePage.html', content)
	else:
		return HttpResponseRedirect(reverse('adminlogin'))

# Method name: addAdditionalInfo
# Creation date: Feb 13, 2019 
# Purpose: View for adding a record in AdditionalInfo table. Contains the form processing and record adding.
# Calling arguments: 
# Required files: recordAdditionalInfo.html
@login_required(login_url='/adminpage/login/')
def addAdditionalInfo(request):
	if request.user.is_superuser:
		if request.method == "POST":
			form = addAdditionalinfoForm(request.POST)
			if form.is_valid():
				post = form.save()
				if '_addAnother' in request.POST:
					return HttpResponseRedirect(reverse('addAdditionalInfo', args=()))
				elif '_save' in request.POST:
					return HttpResponseRedirect(reverse('tablePage', args=("Additionalinfo",)))

		form = addAdditionalinfoForm()
	
		content = {
			'tableChoices' : TABLES_CHOICES,
			'infoChoices' : INFOTYPE_CHOICES,
			'recordExist' : False,
			'form' : form,
		}

		return render(request, 'adminpage/recordAdditionalInfo.html', content)
	else:
		return HttpResponseRedirect(reverse('adminlogin'))

# Method name: editAdditionalInfo
# Creation date: Feb 13, 2019 
# Purpose: View for a record in AdditionalInfo table. Contains the form processing, record saving and record deletion.
# Calling arguments: record id
# Required files: recordAdditionalInfo.html
@login_required(login_url='/adminpage/login/')
def editAdditionalInfo(request, id):
	if request.user.is_superuser:
		try:
			record = Additionalinfo.objects.get(additionalinfoid=id)
		except Exception:
			record = None

		if request.method=="GET":
			if '_delete' in request.GET:
				if record!=None:
					record.delete()
				else:
					messages.error(request,'Record does not exist.')
				return HttpResponseRedirect(reverse('tablePage', args=("Additionalinfo",)))
		if request.method == "POST":
			form = addAdditionalinfoForm(request.POST, instance=record)
			if form.is_valid():			
				if '_addAnother' in request.POST:
					post = form.save()
					return HttpResponseRedirect(reverse('addAdditionalInfo', args=()))
				elif '_save' in request.POST:
					if record!=None:
						post = form.save()
					else:
						messages.error(request,'Record does not exist.')
					return HttpResponseRedirect(reverse('tablePage', args=("Additionalinfo",)))
		form = addAdditionalinfoForm(instance=record)

		content = {
			'tableChoices' : TABLES_CHOICES,
			'infoChoices' : INFOTYPE_CHOICES,
			'recordExist' : True,
			'record' : record, 				#Ito yung record na result ng query sa db
			'form' : form,
			'isdeletable': not record.is_deletable(),
		}

		return render(request, 'adminpage/recordAdditionalInfo.html', content)
	else:
		return HttpResponseRedirect(reverse('adminlogin'))

# Method name: addArea
# Creation date: Feb 13, 2019 
# Purpose: View for adding a record in Area table. Contains the form processing and record adding.
# Calling arguments: 
# Required files: recordArea.html
@login_required(login_url='/adminpage/login/')
def addArea(request):
	if request.user.is_superuser:
		if request.method == "POST":
			form = addAreaForm(request.POST)
			if form.is_valid():
				post = form.save()
				if '_addAnother' in request.POST:
					return HttpResponseRedirect(reverse('addArea', args=()))
				elif '_save' in request.POST:
					return HttpResponseRedirect(reverse('tablePage', args=("Area",)))
		form = addAreaForm()

		content = {
			'tableChoices' : TABLES_CHOICES,
			'recordExist' : False,
			'form' : form,
		}

		return render(request, 'adminpage/recordArea.html', content)
	else:
		return HttpResponseRedirect(reverse('adminlogin'))

# Method name: editArea
# Creation date: Feb 13, 2019 
# Purpose: View for a record in Area table. Contains the form processing, record saving and record deletion.
# Calling arguments: record id
# Required files: recordArea.html
@login_required(login_url='/adminpage/login/')
def editArea(request, id):
	if request.user.is_superuser:
		try:
			record = Area.objects.get(areaid=id)
		except Exception:
			record = None

		if request.method=="GET":
			if '_delete' in request.GET:
				if record!=None:
					record.delete()
				else:
					messages.error(request,'Record does not exist.')
				return HttpResponseRedirect(reverse('tablePage', args=("Area",)))
		if request.method == "POST":
			form = addAreaForm(request.POST, instance=record)
			if form.is_valid():
				if '_save' in request.POST:
					if record!=None:
						post = form.save()
					else:
						messages.error(request,'Record does not exist.')
					return HttpResponseRedirect(reverse('tablePage', args=("Area",)))
		form = addAreaForm(instance=record)

		content = {
			'tableChoices' : TABLES_CHOICES,
			'recordExist' : True,
			'record' : record, 				
			'form' : form,
			'isdeletable': not record.is_deletable(),
		}

		return render(request, 'adminpage/recordArea.html', content)
	else:
		return HttpResponseRedirect(reverse('adminlogin'))

# Method name: addContact
# Creation date: Feb 13, 2019 
# Purpose: View for adding a record in Contact table. Contains the form processing and record adding.
# Calling arguments: 
# Required files: recordContact.html
@login_required(login_url='/adminpage/login/')
def addContact(request):
	if request.user.is_superuser:
		if request.method == "POST":
			form = addContactForm(request.POST)
			if form.is_valid():
				post = form.save()
				if '_addAnother' in request.POST:
					return HttpResponseRedirect(reverse('addContact', args=()))
				elif '_save' in request.POST:
					return HttpResponseRedirect(reverse('tablePage', args=("Contact",)))
		form = addContactForm()

		content = {
			'tableChoices' : TABLES_CHOICES,
			'recordExist' : False,
			'form' : form,
		}

		return render(request, 'adminpage/recordContact.html', content)
	else:
		return HttpResponseRedirect(reverse('adminlogin'))

# Method name: editContact
# Creation date: Feb 13, 2019 
# Purpose: View for a record in Contact table. Contains the form processing, record saving and record deletion.
# Calling arguments: record id
# Required files: recordContact.html
@login_required(login_url='/adminpage/login/')
def editContact(request, id):
	if request.user.is_superuser:
		try:
			record = Contact.objects.get(contactid=id)
		except Exception:
			record = None

		if request.method=="GET":
			if '_delete' in request.GET:
				if record!=None:
					record.delete()
				else:
					messages.error(request,'Record does not exist.')
				return HttpResponseRedirect(reverse('tablePage', args=("Contact",)))
		if request.method == "POST":
			form = addContactForm(request.POST, instance=record)
			if form.is_valid():
				if '_save' in request.POST:
					if record!=None:
						post = form.save()
					else:
						messages.error(request,'Record does not exist.')
					return HttpResponseRedirect(reverse('tablePage', args=("Contact",)))
		form = addContactForm(instance=record)

		content = {
			'tableChoices' : TABLES_CHOICES,
			'recordExist' : True,
			'record' : record, 				
			'form' : form,
		}

		return render(request, 'adminpage/recordContact.html', content)
	else:
		return HttpResponseRedirect(reverse('adminlogin'))

# Method name: editFeedback
# Creation date: Feb 13, 2019 
# Purpose: View for a record in Feedback table. Contains the form processing, record saving and record deletion.
# Calling arguments: record id
# Required files: recordFeedback.html
@login_required(login_url='/adminpage/login/')
def editFeedback(request, id):
	if request.user.is_superuser:
		try:
			record = Feedback.objects.get(feedbackid=id)
		except Exception:
			record = None

		if request.method=="GET":
			if '_delete' in request.GET:
				if record!=None:
					record.delete()
				else:
					messages.error(request,'Record does not exist.')
				return HttpResponseRedirect(reverse('tablePage', args=("Feedback",)))
		if request.method == "POST":
			form = addFeedbackForm(request.POST, instance=record)
			if form.is_valid():
				if '_save' in request.POST:
					if record!=None:
						post = form.save()
					else:
						messages.error(request,'Record does not exist.')
					return HttpResponseRedirect(reverse('tablePage', args=("Feedback",)))
		form = addFeedbackForm(instance=record)

		content = {
			'tableChoices' : TABLES_CHOICES,
			'recordExist' : True,
			'record' : record, 			
			'form' : form,
		}

		return render(request, 'adminpage/recordFeedback.html', content)
	else:
		return HttpResponseRedirect(reverse('adminlogin'))

# Method name: addHousetype
# Creation date: Feb 13, 2019 
# Purpose: View for adding a record in Housetype table. Contains the form processing and record adding.
# Calling arguments: 
# Required files: recordHousetype.html
@login_required(login_url='/adminpage/login/')
def addHousetype(request):
	if request.user.is_superuser:
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
	else:
		return HttpResponseRedirect(reverse('adminlogin'))

# Method name: editHousetype
# Creation date: Feb 13, 2019 
# Purpose: View for a record in Housetype table. Contains the form processing, record saving and record deletion.
# Calling arguments: record id
# Required files: recordHousetype.html
@login_required(login_url='/adminpage/login/')
def editHousetype(request, id):
	if request.user.is_superuser:
		try:
			record = Housetype.objects.get(housetypeid=id)
		except Exception:
			record = None

		if request.method=="GET":
			if '_delete' in request.GET:
				if record!=None:
					record.delete()
				else:
					messages.error(request,'Record does not exist.')
				return HttpResponseRedirect(reverse('tablePage', args=("Housetype",)))
		if request.method == "POST":
			form = addHousetypeForm(request.POST, instance=record)
			if form.is_valid():
				if '_save' in request.POST:
					if record!=None:
						post = form.save()
					else:
						messages.error(request,'Record does not exist.')
					return HttpResponseRedirect(reverse('tablePage', args=("Housetype",)))
		form = addHousetypeForm(instance=record)

		content = {
			'tableChoices' : TABLES_CHOICES,
			'recordExist' : True,
			'record' : record, 	
			'form' : form,		
			'isdeletable': not record.is_deletable(),	
		}

		return render(request, 'adminpage/recordHousetype.html', content)
	else:
		return HttpResponseRedirect(reverse('adminlogin'))

# Method name: addHousing
# Creation date: Feb 13, 2019 
# Purpose: View for adding a record in Housing table. Contains the form processing and record adding.
# Calling arguments: 
# Required files: recordHousing.html
@login_required(login_url='/adminpage/login/')
def addHousing(request):
	if request.user.is_superuser:
		if request.method == "POST":
			form = addHousingForm(request.POST)
			if form.is_valid():
				post = form.save()
				if '_addAnother' in request.POST:
					return HttpResponseRedirect(reverse('addHousing', args=()))
				elif '_save' in request.POST:
					return HttpResponseRedirect(reverse('tablePage', args=("Housing",)))

		form = addHousingForm()

		content = {
			'tableChoices' : TABLES_CHOICES,
			'recordExist' : False,
			'form' : form,
		}

		return render(request, 'adminpage/recordHousing.html', content)
	else:
		return HttpResponseRedirect(reverse('adminlogin'))

# Method name: editHousing 
# Creation date: Feb 13, 2019 
# Purpose: View for a record in Housing table. Contains the form processing, record saving and record deletion.
# Calling arguments: record id
# Required files: recordHousing.html
@login_required(login_url='/adminpage/login/')
def editHousing(request, id):
	if request.user.is_superuser:
		try:
			record = Housing.objects.get(housingid=id)
		except Exception:
			record = None

		if request.method=="GET":
			if '_delete' in request.GET:
				if record!=None:
					record.delete()
				else:
					messages.error(request,'Record does not exist.')
				return HttpResponseRedirect(reverse('tablePage', args=("Housing",)))
		if request.method == "POST":
			form = addHousingForm(request.POST, instance=record)
			if form.is_valid():		
				if '_save' in request.POST:
					if record!=None:
						post = form.save()
					else:
						messages.error(request,'Record does not exist.')
					return HttpResponseRedirect(reverse('tablePage', args=("Housing",)))
			
		form = addHousingForm(instance=record)

		content = {
			'tableChoices' : TABLES_CHOICES,
			'recordExist' : True,
			'record' : record, 			
			'form' : form,
			'isdeletable': not record.is_deletable(),
		}

		return render(request, 'adminpage/recordHousing.html', content)
	else:
		return HttpResponseRedirect(reverse('adminlogin'))

# Method name: addPropertytype
# Creation date: Feb 13, 2019 
# Purpose: View for adding a record in Propertytype table. Contains the form processing and record adding.
# Calling arguments: 
# Required files: recordPropertytype.html
@login_required(login_url='/adminpage/login/')
def addPropertytype(request):
	if request.user.is_superuser:
		if request.method == "POST":
			form = addPropertytypeForm(request.POST)
			if form.is_valid():
				post = form.save()
				if '_addAnother' in request.POST:
					return HttpResponseRedirect(reverse('addPropertytype', args=()))
				elif '_save' in request.POST:
					return HttpResponseRedirect(reverse('tablePage', args=("Propertytype",)))
		form = addPropertytypeForm()

		content = {
			'tableChoices' : TABLES_CHOICES,
			'recordExist' : False,
			'form' : form,
		}

		return render(request, 'adminpage/recordPropertytype.html', content)
	else:
		return HttpResponseRedirect(reverse('adminlogin'))

# Method name: editPropertytype
# Creation date: Feb 13, 2019 
# Purpose: View for a record in Propertytype table. Contains the form processing, record saving and record deletion.
# Calling arguments: record id
# Required files: recordPropertytype.html
@login_required(login_url='/adminpage/login/')
def editPropertytype(request, id):
	if request.user.is_superuser:
		try:
			record = Propertytype.objects.get(propertytypeid=id)
		except Exception:
			record = None

		if request.method=="GET":
			if '_delete' in request.GET:
				if record!=None:
					record.delete()
				else:
					messages.error(request,'Record does not exist.')
				return HttpResponseRedirect(reverse('tablePage', args=("Propertytype",)))
		if request.method == "POST":
			form = addPropertytypeForm(request.POST, instance=record)
			if form.is_valid():
				if '_save' in request.POST:
					if record!=None:
						post = form.save()
					else:
						messages.error(request,'Record does not exist.')
					return HttpResponseRedirect(reverse('tablePage', args=("Propertytype",)))
		form = addPropertytypeForm(instance=record)

		content = {
			'tableChoices' : TABLES_CHOICES,
			'recordExist' : True,
			'record' : record,
			'form' : form,
			'isdeletable': not record.is_deletable(),
		}

		return render(request, 'adminpage/recordPropertytype.html', content)
	else:
		return HttpResponseRedirect(reverse('adminlogin'))

# Method name: editRequest
# Creation date: Feb 13, 2019 
# Purpose: View for a record in Request table. Contains the form processing, record saving and record deletion.
# Calling arguments: record id
# Required files: recordRequest.html
@login_required(login_url='/adminpage/login/')
def editRequest(request, id):
	if request.user.is_superuser:
		try:
			record = Request.objects.get(requestid=id)
		except Exception:
			record = None

		if request.method=="GET":
			if '_delete' in request.GET:
				if record!=None:
					record.delete()
				else:
					messages.error(request,'Record does not exist.')
				return HttpResponseRedirect(reverse('tablePage', args=("Request",)))
		if request.method == "POST":
			form = addRequestForm(request.POST, instance=record)
			if form.is_valid():	
				if '_save' in request.POST:
					if record!=None:
						post = form.save()
					else:
						messages.error(request,'Record does not exist.')
					return HttpResponseRedirect(reverse('tablePage', args=("Request",)))
		form = addRequestForm(instance=record)

		content = {
			'tableChoices' : TABLES_CHOICES,
			'recordExist' : True,
			'record' : record, 		
			'form' : form,
			'isdeletable': not record.is_deletable(),
		}

		return render(request, 'adminpage/recordRequest.html', content)
	else:
		return HttpResponseRedirect(reverse('adminlogin'))


# Method name: addHousingAdditionalInfo
# Creation date: Feb 13, 2019 
# Purpose: View for adding a record in HousingAdditionalInfo table. Contains the form processing and record adding.
# Calling arguments: 
# Required files: recordHousingAdditionalInfo.html
@login_required(login_url='/adminpage/login/')
def addHousingAdditionalInfo(request):
	if request.user.is_superuser:
		if request.method == "POST":
			form = addHousingAddtnlinfoForm(request.POST)
			if form.is_valid():
				post = form.save()
				if '_addAnother' in request.POST:
					return HttpResponseRedirect(reverse('addHousingAdditionalInfo', args=()))
				elif '_save' in request.POST:
					return HttpResponseRedirect(reverse('tablePage', args=("HousingAdditionalinfo",)))
		form = addHousingAddtnlinfoForm()

		content = {
			'tableChoices' : TABLES_CHOICES,
			'recordExist' : False,
			'form' : form,
		}

		return render(request, 'adminpage/recordHousingAdditionalInfo.html', content)
	else:
		return HttpResponseRedirect(reverse('adminlogin'))


# Method name: editHousingAdditionalInfo
# Creation date: Feb 13, 2019 
# Purpose: View for a record in HousingAdditionalInfo table. Contains the form processing, record saving and record deletion.
# Calling arguments: record id
# Required files: recordHousingAdditionalInfo.html
@login_required(login_url='/adminpage/login/')
def editHousingAdditionalInfo(request, id):
	if request.user.is_superuser:
		try:
			record = HousingAdditionalInfo.objects.get(housingadditionalinfoid=id)
		except Exception:
			record = None

		if request.method=="GET":
			if '_delete' in request.GET:
				if record!=None:
					record.delete()
				else:
					messages.error(request,'Record does not exist.')
				return HttpResponseRedirect(reverse('tablePage', args=("HousingAdditionalinfo",)))
		if request.method == "POST":
			form = addHousingAddtnlinfoForm(request.POST, instance=record)
			if form.is_valid():
				if '_save' in request.POST:
					if record!=None:
						post = form.save()
					else:
						messages.error(request,'Record does not exist.')
					return HttpResponseRedirect(reverse('tablePage', args=("HousingAdditionalinfo",)))
		form = addHousingAddtnlinfoForm(instance=record)

		content = {
			'tableChoices' : TABLES_CHOICES,
			'recordExist' : True,
			'record' : record,
			'form' : form,
		}

		return render(request, 'adminpage/recordHousingAdditionalInfo.html', content)
	else:
		return HttpResponseRedirect(reverse('adminlogin'))

# Method name: addHousingOwner
# Creation date: Feb 13, 2019 
# Purpose: View for adding a record in HousingOwner table. Contains the form processing and record adding.
# Calling arguments: 
# Required files: recordHousingOwner.html
@login_required(login_url='/adminpage/login/')
def addHousingOwner(request):
	if request.user.is_superuser:
		if request.method == "POST":
			form = addHousingOwnerForm(request.POST)
			if form.is_valid():
				post = form.save()
				if '_addAnother' in request.POST:
					return HttpResponseRedirect(reverse('addHousingOwner', args=()))
				elif '_save' in request.POST:
					return HttpResponseRedirect(reverse('tablePage', args=("HousingOwner",)))
		form = addHousingOwnerForm()

		content = {
			'tableChoices' : TABLES_CHOICES,
			'recordExist' : False,
			'form' : form,
		}

		return render(request, 'adminpage/recordHousingOwner.html', content)
	else:
		return HttpResponseRedirect(reverse('adminlogin'))

# Method name: editHousingOwner
# Creation date: Feb 13, 2019 
# Purpose: View for a record in HousingOwner table. Contains the form processing, record saving and record deletion.
# Calling arguments: record id
# Required files: recordHousingOwner.html
@login_required(login_url='/adminpage/login/')
def editHousingOwner(request, id):
	if request.user.is_superuser:
		try:
			record = HousingOwner.objects.get(housingownerid=id)
		except Exception:
			record = None

		if request.method=="GET":
			if '_delete' in request.GET:
				if record!=None:
					record.delete()
				else:
					messages.error(request,'Record does not exist.')
				return HttpResponseRedirect(reverse('tablePage', args=("HousingOwner",)))
		if request.method == "POST":
			form = addHousingOwnerForm(request.POST, instance=record)
			if form.is_valid():
				if '_save' in request.POST:
					if record!=None:
						post = form.save()
					else:
						messages.error(request,'Record does not exist.')
					return HttpResponseRedirect(reverse('tablePage', args=("HousingOwner",)))
		form = addHousingOwnerForm(instance=record)

		content = {
			'tableChoices' : TABLES_CHOICES, 
			'recordExist' : True,
			'record' : record, 	
			'form' : form,			
		}

		return render(request, 'adminpage/recordHousingOwner.html', content)
	else:
		return HttpResponseRedirect(reverse('adminlogin'))

# Method name: addHousingRequest
# Creation date: Feb 13, 2019 
# Purpose: View for adding a record in HousingRequest table. Contains the form processing and record adding.
# Calling arguments: 
# Required files: recordHousingRequest.html
@login_required(login_url='/adminpage/login/')
def addHousingRequest(request):
	if request.user.is_superuser:
		if request.method == "POST":
			form = addHousingRequestForm(request.POST)
			if form.is_valid():
				post = form.save()
				if '_addAnother' in request.POST:
					return HttpResponseRedirect(reverse('addHousingRequest', args=()))
				elif '_save' in request.POST:
					return HttpResponseRedirect(reverse('tablePage', args=("HousingRequest",)))
		form = addHousingRequestForm()

		content = {
			'tableChoices' : TABLES_CHOICES,
			'recordExist' : False,
			'form' : form,
		}

		return render(request, 'adminpage/recordHousingRequest.html', content)
	else:
		return HttpResponseRedirect(reverse('adminlogin'))

# Method name: editHousingRequest
# Creation date: Feb 13, 2019 
# Purpose: View for a record in HousingRequest table. Contains the form processing, record saving and record deletion.
# Calling arguments: record id
# Required files: recordHousingRequest.html
@login_required(login_url='/adminpage/login/')
def editHousingRequest(request, id):
	if request.user.is_superuser:
		try:
			record = HousingRequest.objects.get(housingrequestid=id)
		except Exception:
			record = None

		if request.method=="GET":
			if '_delete' in request.GET:
				if record!=None:
					record.delete()
				else:
					messages.error(request,'Record does not exist.')
				return HttpResponseRedirect(reverse('tablePage', args=("HousingRequest",)))
		if request.method == "POST":
			form = addHousingRequestForm(request.POST, instance=record)
			if form.is_valid():
				if '_save' in request.POST:
					if record!=None:
						post = form.save()
					else:
						messages.error(request,'Record does not exist.')
					return HttpResponseRedirect(reverse('tablePage', args=("HousingRequest",)))
		form = addHousingRequestForm(instance=record)

		content = {
			'tableChoices' : TABLES_CHOICES,
			'recordExist' : True,
			'record' : record,
			'form' : form, 	
		}

		return render(request, 'adminpage/recordHousingRequest.html', content)
	else:
		return HttpResponseRedirect(reverse('adminlogin'))

# Method name: addPicture
# Creation date: Feb 13, 2019 
# Purpose: View for adding a record in Picture table. Contains the form processing and record adding.
# Calling arguments: 
# Required files: recordPicture.html
@login_required(login_url='/adminpage/login/')
def addPicture(request):
	if request.user.is_superuser:
		if request.method == "POST":
			form = addPictureForm(request.POST)
			if form.is_valid():
				post = form.save()
				if '_addAnother' in request.POST:
					return HttpResponseRedirect(reverse('addPicture', args=()))
				elif '_save' in request.POST:
					return HttpResponseRedirect(reverse('tablePage', args=("Picture",)))
		form = addPictureForm()

		content = {
			'tableChoices' : TABLES_CHOICES, 
			'recordExist' : False,
			'form' : form,
		}

		return render(request, 'adminpage/recordPicture.html', content)
	else:
		return HttpResponseRedirect(reverse('adminlogin'))

# Method name: editPicture
# Creation date: Feb 13, 2019 
# Purpose: View for a record in Picture table. Contains the form processing, record saving and record deletion.
# Calling arguments: record id
# Required files: recordPicture.html
@login_required(login_url='/adminpage/login/')
def editPicture(request, id):
	if request.user.is_superuser:
		try:
			record = Picture.objects.get(pictureid=id)
		except Exception:
			record = None

		if request.method=="GET":
			if '_delete' in request.GET:
				if record!=None:
					record.delete()
				else:
					messages.error(request,'Record does not exist.')
				return HttpResponseRedirect(reverse('tablePage', args=("Picture",)))
		if request.method == "POST":
			form = addPictureForm(request.POST, instance=record)
			if form.is_valid():
				if '_save' in request.POST:
					if record!=None:
						post = form.save()
					else:
						messages.error(request,'Record does not exist.')
					return HttpResponseRedirect(reverse('tablePage', args=("Picture",)))
		form = addPictureForm(instance=record)

		content = {
			'tableChoices' : TABLES_CHOICES,
			'recordExist' : True,
			'record' : record, 
			'form' : form,	
		}

		return render(request, 'adminpage/recordPicture.html', content)
	else:
		return HttpResponseRedirect(reverse('adminlogin'))

# Method name: addRoomCost
# Creation date: Feb 13, 2019 
# Purpose: View for a record in Room Cost table. Contains the form processing, record adding.
# Calling arguments: 
# Required files: recordRoomCost.html
@login_required(login_url='/adminpage/login/')
def addRoomCost(request):
	if request.user.is_superuser:
		if request.method == "POST":
			form = addRoomCostForm(request.POST)
			if form.is_valid():
				post = form.save()
				if '_addAnother' in request.POST:
					return HttpResponseRedirect(reverse('addRoomCost', args=()))
				elif '_save' in request.POST:
					return HttpResponseRedirect(reverse('tablePage', args=("RoomCost",)))
		form = addRoomCostForm()

		content = {
			'tableChoices' : TABLES_CHOICES, 
			'recordExist' : False,
			'form' : form,
		}

		return render(request, 'adminpage/recordRoomCost.html', content)
	else:
		return HttpResponseRedirect(reverse('adminlogin'))

# Method name: editRoomCost
# Creation date: Feb 13, 2019 
# Purpose: View for a record in Room Cost table. Contains the form processing, record saving and record deletion.
# Calling arguments: 
# Required files: recordRoomCost.html, recordHousing.html
@login_required(login_url='/adminpage/login/')
def editRoomCost(request, id):
	if request.user.is_superuser:
		try:
			record = RoomCost.objects.get(roomid=id)
		except Exception:
			record = None

		if request.method=="GET":
			if '_delete' in request.GET:
				if record!=None:
					record.delete()
				else:
					messages.error(request,'Record does not exist.')
				return HttpResponseRedirect(reverse('tablePage', args=("RoomCost",)))
		if request.method == "POST":
			form = addRoomCostForm(request.POST, instance=record)
			if form.is_valid():
				if '_save' in request.POST:
					if record!=None:
						post = form.save()
					else:
						messages.error(request,'Record does not exist.')
					return HttpResponseRedirect(reverse('tablePage', args=("RoomCost",)))
		form = addRoomCostForm(instance=record)

		content = {
			'tableChoices' : TABLES_CHOICES,
			'recordExist' : True,
			'record' : record, 
			'form' : form,
		}

		return render(request, 'adminpage/recordRoomCost.html', content)
	else:
		return HttpResponseRedirect(reverse('adminlogin'))

# Method name: addOwner
# Creation date: Feb 13, 2019 
# Purpose: View for a record in Owner table. Contains the form processing, record adding.
# Calling arguments: 
# Required files: recordOwner.html
@login_required(login_url='/adminpage/login/')
def addOwner(request):
	if request.user.is_superuser:
		if request.method == "POST":
			form = addOwnerForm(request.POST)
			if form.is_valid():
				post = form.save()
				if '_addAnother' in request.POST:
					return HttpResponseRedirect(reverse('addOwner', args=()))
				elif '_save' in request.POST:
					return HttpResponseRedirect(reverse('tablePage', args=("Owner",)))
		form = addOwnerForm()

		content = {
			'tableChoices' : TABLES_CHOICES,
			'recordExist' : False,
			'form' : form,
		}

		return render(request, 'adminpage/recordOwner.html', content)
	else:
		return HttpResponseRedirect(reverse('adminlogin'))

# Method name: editOwner
# Creation date: Feb 13, 2019 
# Purpose: View for a record in Owner table. Contains the form processing, record saving and record deletion.
# Calling arguments: owner id
# Required files: recordOwner.html
@login_required(login_url='/adminpage/login/')
def editOwner(request, id):
	if request.user.is_superuser:
		try:
			record = Owner.objects.get(ownerid=id)
		except Exception:
			record = None

		if request.method=="GET":
			if '_delete' in request.GET:
				if record!=None:
					record.delete()
				else:
					messages.error(request,'Record does not exist.')
				return HttpResponseRedirect(reverse('tablePage', args=("Owner",)))
		if request.method == "POST":
			form = addOwnerForm(request.POST, instance=record)
			if form.is_valid():
				if '_save' in request.POST:
					if record!=None:
						post = form.save()
					else:
						messages.error(request,'Record does not exist.')
					return HttpResponseRedirect(reverse('tablePage', args=("Owner",)))
		form = addOwnerForm(instance=record)

		content = {
			'tableChoices' : TABLES_CHOICES,
			'recordExist' : True,
			'record' : record, 
			'form' : form,
			'isdeletable': not record.is_deletable(),
		}

		return render(request, 'adminpage/recordOwner.html', content)
	else:
		return HttpResponseRedirect(reverse('adminlogin'))
