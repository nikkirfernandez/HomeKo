

# CODE HISTORY #
# Sontillano     # Feb 5, 2018     # added enduserHome, enduserSearchResult, enduserRecord, enduserRequest, ownerLogin
# Sontillano     # Feb 6, 2018     # fixed enduserHome, enduserSearchResult, enduserRecord       

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .forms import *
from .choices import *
from .models import *

from django.db.models import Max, Min

# Dummy view 
def home(request):
     return HttpResponse('HELLO WORLD!');

# This is the view for the home page.
def enduserHome(request):
     if request.method == "POST" :
          searchForm = SearchHousing(request.POST)

          if searchForm.is_valid():     

               filtersSet1={}
               filtersSet2=[]     

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

               if(searchForm.cleaned_data['kitchen'])==True:
                    filtersSet2.append("Kitchen")
               if(searchForm.cleaned_data['aircon']) == True:
                    filtersSet2.append("Air conditioning")
               if(searchForm.cleaned_data['washer']) == True:
                    filtersSet2.append("Washer")
               if(searchForm.cleaned_data['dryer'])==True:
                    filtersSet2.append("Dryer")
               if(searchForm.cleaned_data['wifi']) == True:
                    filtersSet2.append("Wifi")
               if(searchForm.cleaned_data['iron'])==True:
                    filtersSet2.append("Iron")
               if(searchForm.cleaned_data['tv'])==True:
                    filtersSet2.append("TV")
               if(searchForm.cleaned_data['parking'])==True:
                    filtersSet2.append("Parking")
               if(searchForm.cleaned_data['pet'])==True:
                    filtersSet2.append("Pets allowed")
               if(searchForm.cleaned_data['smoking'])==True:
                    filtersSet2.append("Smoking allowed")
               if(searchForm.cleaned_data['curfew'])==True:
                    filtersSet2.append("No curfew")     

               ### read from db according to the filters ###
               arguments1 = {}
               for k, v in filtersSet1.items():
                    if v:
                         arguments1[k] = v
               
               housingResults = Housing.objects.filter(**arguments1)
               
               results2 = []
               if priceMax!=None:
                    for result in housingResults:
                         result2temp = RoomCost.objects.filter(housingid=result.housingid, cost__lte = priceMax).first()
                         if result2temp!=None: 
                              results2.append(result2temp.housingid.housingid)
               else:
                    results2 = [result.housingid for result in housingResults]     

               results3 = []
               for result in results2:
                    housingTemp = HousingAdditionalInfo.objects.filter(housingid=result)
                    for filters in filtersSet2:
                         result3temp = housingTemp.filter(additionalinfoid__additionalinfoname=filters).first()
                         if result3temp != None:
                              results3.append(result3temp.housingid.housingid)
               if len(filtersSet2)==0:
                    results3=results2
               
               request.session['searchResult'] = results3
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

def enduserRecord(request, housingid):
     housing = Housing.objects.filter(housingid=housingid).first()
     owner = HousingOwner.objects.filter(housingid=housingid).first().ownerid
     ownerName = str(owner.firstname) + str(owner.lastname)
     housingRooms = RoomCost.objects.filter(housingid=housingid)
     amenities = HousingAdditionalInfo.objects.filter(housingid=housingid, additionalinfoid__additionalinfotype=1)
     facilities = HousingAdditionalInfo.objects.filter(housingid=housingid, additionalinfoid__additionalinfotype=2)
     rules = HousingAdditionalInfo.objects.filter(housingid=housingid, additionalinfoid__additionalinfotype=3)
     comments = Feedback.objects.filter(housingid=housingid, status=2)

     content = {
          'housing' : housing,
          'ownername' : ownerName,
          'rooms' : housingRooms,
          'amenities' : amenities,
          'facilities' : facilities,
          'rules' : rules,
          'comments' : comments,
     }
     return render(request, 'mainpage/housing_record.html', content)

def enduserRequest(request):
	if request.method == "POST" :
		requestForm = AddRequest(request.POST)
		searchForm = SearchHousing(request.POST)
		if requestForm.is_valid():
			email = requestForm.cleaned_data['email']
			requestIndex = requestForm.cleaned_data['requestType']
			requestType = REQUEST_CHOICES[int(requestIndex)-1][1]
			reqcontent = requestForm.cleaned_data['content']
		elif searchForm.is_valid():
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
