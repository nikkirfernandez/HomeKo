from django.shortcuts import render

from .choices import *

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

	content = {
		'tableChoices' : TABLES_CHOICES,
		'tableName' : table,
		# 'records' : records,           
	}

	return render(request, 'adminpage/tablePage.html', content)

def addAdditionalInfo(request):

	content = {
		'tableChoices' : TABLES_CHOICES,
	}

	return render(request, 'adminpage/recordPage.html', content)

