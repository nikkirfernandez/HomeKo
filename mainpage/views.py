from django.shortcuts import render
from django.http import HttpResponse

from .forms import *
from .choices import *

def home(request):
    return HttpResponse('HELLO WORLD!');
# Create your views here.

def enduserHome(request):
	print("outside post")
	if request.method == "POST" :
		searchForm = SearchHousing(request.POST)
		print("inside post")
		print(searchForm.errors)
		if searchForm.is_valid():
			print("FORM IS VALID")
			areaIndex = searchForm.cleaned_data['area']
			area = AREA_CHOICES[int(areaIndex)-1][1]
			propertyIndex = searchForm.cleaned_data['propertyType']
			propertyType = PROPERTY_CHOICES[int(propertyIndex)-1][1]
			homeIndex = searchForm.cleaned_data['homeType']
			homeType = HOME_CHOICES[int(homeIndex)-1][1]
			priceMin = searchForm.cleaned_data['priceMin']
			priceMax = searchForm.cleaned_data['priceMax']
			kitchen = searchForm.cleaned_data['kitchen']
			aircon = searchForm.cleaned_data['aircon']
			washer = searchForm.cleaned_data['washer']
			dryer = searchForm.cleaned_data['dryer']
			wifi = searchForm.cleaned_data['wifi']
			iron = searchForm.cleaned_data['iron']
			tv = searchForm.cleaned_data['tv']
			parking = searchForm.cleaned_data['parking']
			pet = searchForm.cleaned_data['pet']
			smoking = searchForm.cleaned_data['smoking']
			curfew = searchForm.cleaned_data['curfew']

			### read from db according to the filters ###
			#housingResults = 


	searchForm = SearchHousing()

	content = {
	    'areaChoices' : AREA_CHOICES,
	    'propertyChoices' : PROPERTY_CHOICES,
	    'homeChoices' : HOME_CHOICES,
	    'amenityChoices' : AMENITY_CHOICES,
	    'facilityChoices' : FACILITY_CHOICES,
	    'ruleChoices' : RULE_CHOICES,
	}
	#return HttpResponse('HELLO WORLD!');
	return render(request, 'mainpage/home.html', content)

def enduserSearchResult(request):
	content = {}
	return render(request, 'mainpage/search_enduser.html', content)

def enduserRecord(request):
	content = {}
	return render(request, 'mainpage/housing_record.html', content)

def enduserRequest(request):
	if request.method == "POST" :
		requestForm = AddRequest(request.POST)
		searchForm = SearchHousing(request.POST)
		if requestForm.is_valid():
			print("FORM IS VALID")
			email = requestForm.cleaned_data['email']
			requestIndex = requestForm.cleaned_data['requestType']
			requestType = REQUEST_CHOICES[int(requestIndex)-1][1]
			reqcontent = requestForm.cleaned_data['content']
		elif searchForm.is_valid():
			print("FORM IS VALID")
			areaIndex = searchForm.cleaned_data['area']
			area = AREA_CHOICES[int(areaIndex)-1][1]
			propertyIndex = searchForm.cleaned_data['propertyType']
			propertyType = PROPERTY_CHOICES[int(propertyIndex)-1][1]
			homeIndex = searchForm.cleaned_data['homeType']
			homeType = HOME_CHOICES[int(homeIndex)-1][1]
			priceMin = searchForm.cleaned_data['priceMin']
			priceMax = searchForm.cleaned_data['priceMax']
			kitchen = searchForm.cleaned_data['kitchen']
			aircon = searchForm.cleaned_data['aircon']
			washer = searchForm.cleaned_data['washer']
			dryer = searchForm.cleaned_data['dryer']
			wifi = searchForm.cleaned_data['wifi']
			iron = searchForm.cleaned_data['iron']
			tv = searchForm.cleaned_data['tv']
			parking = searchForm.cleaned_data['parking']
			pet = searchForm.cleaned_data['pet']
			smoking = searchForm.cleaned_data['smoking']
			curfew = searchForm.cleaned_data['curfew']

	requestForm = AddRequest()
	searchForm = SearchHousing()

	content = {
	    'requestChoices' : REQUEST_CHOICES,
	    'areaChoices' : AREA_CHOICES,
	    'propertyChoices' : PROPERTY_CHOICES,
	    'homeChoices' : HOME_CHOICES,
	    'amenityChoices' : AMENITY_CHOICES,
	    'facilityChoices' : FACILITY_CHOICES,
	    'ruleChoices' : RULE_CHOICES,
	}
	return render(request, 'mainpage/request_enduser.html', content)

def ownerLogin(request):
	content = {}
	return render(request, 'mainpage/login_owner.html', content)
