from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .forms import *
from .choices import *
from .models import *

from django.db.models import Max, Min

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
			filtersSet1={}

			areaIndex = searchForm.cleaned_data['area']
			if areaIndex!='1':
				area = AREA_CHOICES[int(areaIndex)-1][1]
				filtersSet1['housingid__area'] = area
						
			propertyIndex = searchForm.cleaned_data['propertyType']
			if propertyIndex!='1':
				propertyType = PROPERTY_CHOICES[int(propertyIndex)-1][1]
				filtersSet1['housingid__propertytype__propertytypename'] = propertyType

			homeIndex = searchForm.cleaned_data['homeType']
			if homeIndex!='1':
				homeType = HOME_CHOICES[int(homeIndex)-1][1]
				filtersSet1['housingid__housetype__housetypename'] = homeType

			priceMax = searchForm.cleaned_data['priceMax']

			filtersSet2={}

			kitchen = searchForm.cleaned_data['kitchen']
			if kitchen==True:
				filtersSet2['additionalinfoid__additionalinfoname'] = "Kitchen"
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
			arguments1 = {}
			for k, v in filtersSet1.items():
				if v:
					arguments1[k] = v
					#print(v)

			arguments2 = {}
			for k, v in filtersSet2.items():
				if v:
					arguments2[k] = v
					print(v)

			housingResults = Housing.objects.filter(**arguments1)
			results2 = []
			for result in housingResults:
				print(result.housingname)
				if priceMax!=None:
					result2temp = RoomCost.objects.filter(housingid=result.housingid, cost__lte = priceMax).first()
					if result2temp!=None: 
						results2.append(result2temp.housingid)
				else:
					results2.append(result.housingid)

			results3 = []
			print(results2)
			print("results3")
			for result in results2:
				result3temp = HousingAdditionalInfo.objects.filter(**arguments2, housingid=result).first()
				#print(result3temp)
				if result3temp!=None: 
					results3.append(result3temp.housingid.housingid)
			print(results3)
			print("session")
			request.session['searchResult'] = results3
			print("after session")
			return HttpResponseRedirect(reverse('enduserSearchResult', args=()))


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
	searchResult = request.session.get('searchResult')

	housingResults = []
	priceRange = []
	for result in searchResult:
		print(result)
		housing = Housing.objects.filter(housingid=result).first()
		housingResults.append(housing)
		housingRooms = RoomCost.objects.filter(housingid=result)
		priceMin = housingRooms.aggregate(Min('cost'))
		priceMax = housingRooms.aggregate(Max('cost'))
		priceRange.append(str(priceMin['cost__min']) + "-" + str(priceMax['cost__max']))

	searchResults = [{'item1': t[0], 'item2': t[1]} for t in zip(housingResults, priceRange)]
	content = {
		'searchResults' : searchResults,
	}
	return render(request, 'mainpage/search_enduser.html', content)

def enduserRecord(request):
	housingid=1
	housing = Housing.objects.filter(housingid=housingid).first()
	owner = HousingOwner.objects.filter(housingid=housingid).first().ownerid
	ownerName = str(owner.firstname) + str(owner.lastname)
	housingRooms = RoomCost.objects.filter(housingid=housingid)
	#amenities = HousingAdditionalInfo.objects.filter()

	content = {
		'housing' : housing,
		'ownername' : ownerName,
		'rooms' : housingRooms,
	}
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
