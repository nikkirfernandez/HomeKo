# License: MIT License

# CODE HISTORY #
# Sontillano     # Feb 5, 2019     # added enduserHome, enduserSearchResult, enduserRecord, enduserRequest, ownerLogin
# Sontillano     # Feb 6, 2019     # fixed enduserHome, enduserSearchResult, enduserRecord 

# File creation date: Feb. 1, 2019


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

# Method name: enduserHome
# Creation date: Feb 5, 2019 
# Purpose: View for the home page. Contains the processing of forms when submitted. It also passes the choices for the dropdown. 
# Calling arguments: No arguments for calling this function.
# Required files: home.html
def enduserHome(request):
     # if the user submitted the form
     if request.method == "POST" :
          searchForm = SearchHousing(request.POST)

          if searchForm.is_valid():     
               filtersSet1={}
               filtersSet2=[]     
               
               # get the inputs to these dropdown boxes then add to filterSet1 to be used in the query later 
               areaIndex = searchForm.cleaned_data['area']
               if areaIndex!='1':
                    area = AREA_CHOICES[int(areaIndex)-1][1]
                    filtersSet1['area__areaname'] = area						
               propertyIndex = searchForm.cleaned_data['propertyType']
               if propertyIndex!='1':
                    propertyType = PROPERTY_CHOICES[int(propertyIndex)-1][1]
                    filtersSet1['propertytype__propertytypename'] = propertyType     
               homeIndex = searchForm.cleaned_data['homeType']
               if homeIndex!='1':
                    homeType = HOME_CHOICES[int(homeIndex)-1][1]
                    filtersSet1['housetype__housetypename'] = homeType     
               
               # get the input to this textbox
               priceMax = searchForm.cleaned_data['priceMax']

               # get the inputs to these checkboxes then add to filterSet2 to be used in the query later      
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

               # Filter round 1: get the queryset with the filtersSet1 
               housingResults = Housing.objects.filter(**filtersSet1)
               
               # Filter round 2: filter the result of filter round 1. this time, filter based on the max cost
               results2 = []
               if priceMax!=None:
                    for result in housingResults:
                         result2temp = RoomCost.objects.filter(housingid=result.housingid, cost__lte = priceMax).first()
                         if result2temp!=None: 
                              results2.append(result2temp.housingid.housingid)
               else:
                    results2 = [result.housingid for result in housingResults]     

               # Filter round 3: filter the result of filter round 2. this time, filter based on the filtersSet2 
               results3 = []
               if len(filtersSet2)==0:
                    results3=results2
               else:
                    for result in results2:
                         housingTemp = HousingAdditionalInfo.objects.filter(housingid=result)
                         ctr = 0
                         for filters in filtersSet2:
                              result3temp = housingTemp.filter(additionalinfoid__additionalinfoname=filters).first()
                              if result3temp == None:
                                   break
                              ctr = ctr+1
                         if ctr==len(filtersSet2):
                              results3.append(result3temp.housingid.housingid)
               
               # do this so that the list can be passed to the enduserSearchResult method
               request.session['searchResult'] = results3
               # go to enduserSearchResult method to display the search result 
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

# Method name: enduserSearchResult
# Creation date: Feb 5, 2019 
# Purpose: View for the search result page. Contains the processing of search form when submitted. Passes the choices for the dropdown. Passes the information needed in the search result page. 
# Calling arguments: No arguments for calling this function.
# Required files: search_enduser.html
def enduserSearchResult(request):
     # get the passed search result from enduserHome 
     searchResult = request.session.get('searchResult')

     if len(searchResult)!=0:
          # initialize lists of necessary information of each record in the search result
          housingResults = []
          priceRange = []     

          # get the necessary information of each record in the search result
          for result in searchResult:
               housing = Housing.objects.filter(housingid=result).first()
               housingResults.append(housing)
               housingRooms = RoomCost.objects.filter(housingid=result)
               priceMin = housingRooms.aggregate(Min('cost'))
               priceMax = housingRooms.aggregate(Max('cost'))
               priceRange.append(str(priceMin['cost__min']) + "-" + str(priceMax['cost__max']))

          # zip to loop easily in the html
          searchResults = [{'item1': t[0], 'item2': t[1]} for t in zip(housingResults, priceRange)]
     else:
          searchResults = False
     
     # if the user submitted the form
     if request.method == "POST" :
          searchForm = SearchHousing(request.POST)

          if searchForm.is_valid():     
               filtersSet1={}
               filtersSet2=[]     
               
               # get the inputs to these dropdown boxes then add to filterSet1 to be used in the query later 
               areaIndex = searchForm.cleaned_data['area']
               if areaIndex!='1':
                    area = AREA_CHOICES[int(areaIndex)-1][1]
                    filtersSet1['area__areaname'] = area						
               propertyIndex = searchForm.cleaned_data['propertyType']
               if propertyIndex!='1':
                    propertyType = PROPERTY_CHOICES[int(propertyIndex)-1][1]
                    filtersSet1['propertytype__propertytypename'] = propertyType     
               homeIndex = searchForm.cleaned_data['homeType']
               if homeIndex!='1':
                    homeType = HOME_CHOICES[int(homeIndex)-1][1]
                    filtersSet1['housetype__housetypename'] = homeType     
               
               # get the input to this textbox
               priceMax = searchForm.cleaned_data['priceMax']

               # get the inputs to these checkboxes then add to filterSet2 to be used in the query later      
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

               # Filter round 1: get the queryset with the filtersSet1 
               housingResults = Housing.objects.filter(**filtersSet1)
               
               # Filter round 2: filter the result of filter round 1. this time, filter based on the max cost
               results2 = []
               if priceMax!=None:
                    for result in housingResults:
                         result2temp = RoomCost.objects.filter(housingid=result.housingid, cost__lte = priceMax).first()
                         if result2temp!=None: 
                              results2.append(result2temp.housingid.housingid)
               else:
                    results2 = [result.housingid for result in housingResults]     

               # Filter round 3: filter the result of filter round 2. this time, filter based on the filtersSet2 
               results3 = []
               if len(filtersSet2)==0:
                    results3=results2
               else:
                    for result in results2:
                         housingTemp = HousingAdditionalInfo.objects.filter(housingid=result)
                         ctr = 0
                         for filters in filtersSet2:
                              result3temp = housingTemp.filter(additionalinfoid__additionalinfoname=filters).first()
                              if result3temp == None:
                                   break
                              ctr = ctr+1
                         if ctr==len(filtersSet2):
                              results3.append(result3temp.housingid.housingid)
               
               # do this so that the list can be passed to the enduserSearchResult method
               request.session['searchResult'] = results3
               # go to enduserSearchResult method to display the search result 
               return HttpResponseRedirect(reverse('enduserSearchResult', args=()))
     
     searchForm = SearchHousing()

     content = {
          'searchResults' : searchResults,
          'areaChoices' : AREA_CHOICES,
          'propertyChoices' : PROPERTY_CHOICES,
          'homeChoices' : HOME_CHOICES,
          'amenityChoices' : AMENITY_CHOICES,
          'facilityChoices' : FACILITY_CHOICES,
          'ruleChoices' : RULE_CHOICES,
     }
     return render(request, 'mainpage/search_enduser.html', content)

# Method name: enduserRecord
# Creation date: Feb 5, 2019 
# Purpose: View for each housing record page. Contains the processing of search form when submitted. Passes the choices for the dropdown. Passes the information of the selected housing record. 
# Calling arguments: No arguments for calling this function.
# Required files: search_enduser.html
def enduserRecord(request, housingid):
     # get the information of the selected housing record
     housing = Housing.objects.filter(housingid=housingid).first()
     owner = HousingOwner.objects.filter(housingid=housingid).first().ownerid
     ownerName = str(owner.firstname) + " " + str(owner.lastname)
     contact = Contact.objects.filter(ownerid=owner)
     contactNo = [ c.contactno for c in contact]
     contactNo = ", ".join(contactNo)
     housingRooms = RoomCost.objects.filter(housingid=housingid)
     amenities = HousingAdditionalInfo.objects.filter(housingid=housingid, additionalinfoid__additionalinfotype=1)
     facilities = HousingAdditionalInfo.objects.filter(housingid=housingid, additionalinfoid__additionalinfotype=2)
     rules = HousingAdditionalInfo.objects.filter(housingid=housingid, additionalinfoid__additionalinfotype=3)
     comments = Feedback.objects.filter(housingid=housingid, status=2)

     # if the user submitted the form
     if request.method == "POST" :
          searchForm = SearchHousing(request.POST)

          if searchForm.is_valid():     
               filtersSet1={}
               filtersSet2=[]     
               
               # get the inputs to these dropdown boxes then add to filterSet1 to be used in the query later 
               areaIndex = searchForm.cleaned_data['area']
               if areaIndex!='1':
                    area = AREA_CHOICES[int(areaIndex)-1][1]
                    filtersSet1['area__areaname'] = area						
               propertyIndex = searchForm.cleaned_data['propertyType']
               if propertyIndex!='1':
                    propertyType = PROPERTY_CHOICES[int(propertyIndex)-1][1]
                    filtersSet1['propertytype__propertytypename'] = propertyType     
               homeIndex = searchForm.cleaned_data['homeType']
               if homeIndex!='1':
                    homeType = HOME_CHOICES[int(homeIndex)-1][1]
                    filtersSet1['housetype__housetypename'] = homeType     
               
               # get the input to this textbox
               priceMax = searchForm.cleaned_data['priceMax']

               # get the inputs to these checkboxes then add to filterSet2 to be used in the query later      
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

               # Filter round 1: get the queryset with the filtersSet1 
               housingResults = Housing.objects.filter(**filtersSet1)
               
               # Filter round 2: filter the result of filter round 1. this time, filter based on the max cost
               results2 = []
               if priceMax!=None:
                    for result in housingResults:
                         result2temp = RoomCost.objects.filter(housingid=result.housingid, cost__lte = priceMax).first()
                         if result2temp!=None: 
                              results2.append(result2temp.housingid.housingid)
               else:
                    results2 = [result.housingid for result in housingResults]     

               # Filter round 3: filter the result of filter round 2. this time, filter based on the filtersSet2 
               results3 = []
               if len(filtersSet2)==0:
                    results3=results2
               else:
                    for result in results2:
                         housingTemp = HousingAdditionalInfo.objects.filter(housingid=result)
                         ctr = 0
                         for filters in filtersSet2:
                              result3temp = housingTemp.filter(additionalinfoid__additionalinfoname=filters).first()
                              if result3temp == None:
                                   break
                              ctr = ctr+1
                         if ctr==len(filtersSet2):
                              results3.append(result3temp.housingid.housingid)
               
               # do this so that the list can be passed to the enduserSearchResult method
               request.session['searchResult'] = results3
               # go to enduserSearchResult method to display the search result 
               return HttpResponseRedirect(reverse('enduserSearchResult', args=()))
     
     searchForm = SearchHousing()

     content = {
          'housing' : housing,
          'ownername' : ownerName,
          'contact' : contactNo,
          'rooms' : housingRooms,
          'amenities' : amenities,
          'facilities' : facilities,
          'rules' : rules,
          'comments' : comments,
          'areaChoices' : AREA_CHOICES,
          'propertyChoices' : PROPERTY_CHOICES,
          'homeChoices' : HOME_CHOICES,
          'amenityChoices' : AMENITY_CHOICES,
          'facilityChoices' : FACILITY_CHOICES,
          'ruleChoices' : RULE_CHOICES,
     }
     return render(request, 'mainpage/housing_record.html', content)

# Method name: enduserRequest
# Creation date: Feb 5, 2019 
# Purpose: View for each request page. Contains the processing of search form and request form when submitted. Passes the choices for the dropdown.
# Calling arguments: No arguments for calling this function.
# Required files: search_enduser.html
def enduserRequest(request):
     # if the user submitted the form
     if request.method == "POST" :
          searchForm = SearchHousing(request.POST)

          if searchForm.is_valid():     
               filtersSet1={}
               filtersSet2=[]     
               
               # get the inputs to these dropdown boxes then add to filterSet1 to be used in the query later 
               areaIndex = searchForm.cleaned_data['area']
               if areaIndex!='1':
                    area = AREA_CHOICES[int(areaIndex)-1][1]
                    filtersSet1['area__areaname'] = area						
               propertyIndex = searchForm.cleaned_data['propertyType']
               if propertyIndex!='1':
                    propertyType = PROPERTY_CHOICES[int(propertyIndex)-1][1]
                    filtersSet1['propertytype__propertytypename'] = propertyType     
               homeIndex = searchForm.cleaned_data['homeType']
               if homeIndex!='1':
                    homeType = HOME_CHOICES[int(homeIndex)-1][1]
                    filtersSet1['housetype__housetypename'] = homeType     
               
               # get the input to this textbox
               priceMax = searchForm.cleaned_data['priceMax']

               # get the inputs to these checkboxes then add to filterSet2 to be used in the query later      
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

               # Filter round 1: get the queryset with the filtersSet1 
               housingResults = Housing.objects.filter(**filtersSet1)
               
               # Filter round 2: filter the result of filter round 1. this time, filter based on the max cost
               results2 = []
               if priceMax!=None:
                    for result in housingResults:
                         result2temp = RoomCost.objects.filter(housingid=result.housingid, cost__lte = priceMax).first()
                         if result2temp!=None: 
                              results2.append(result2temp.housingid.housingid)
               else:
                    results2 = [result.housingid for result in housingResults]     

               # Filter round 3: filter the result of filter round 2. this time, filter based on the filtersSet2 
               results3 = []
               if len(filtersSet2)==0:
                    results3=results2
               else:
                    for result in results2:
                         housingTemp = HousingAdditionalInfo.objects.filter(housingid=result)
                         ctr = 0
                         for filters in filtersSet2:
                              result3temp = housingTemp.filter(additionalinfoid__additionalinfoname=filters).first()
                              if result3temp == None:
                                   break
                              ctr = ctr+1
                         if ctr==len(filtersSet2):
                              results3.append(result3temp.housingid.housingid)
               
               # do this so that the list can be passed to the enduserSearchResult method
               request.session['searchResult'] = results3
               # go to enduserSearchResult method to display the search result 
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
     return render(request, 'mainpage/request_enduser.html', content)

def ownerLogin(request):
     # if the user submitted the form
     if request.method == "POST" :
          searchForm = SearchHousing(request.POST)

          if searchForm.is_valid():     
               filtersSet1={}
               filtersSet2=[]     
               
               # get the inputs to these dropdown boxes then add to filterSet1 to be used in the query later 
               areaIndex = searchForm.cleaned_data['area']
               if areaIndex!='1':
                    area = AREA_CHOICES[int(areaIndex)-1][1]
                    filtersSet1['area__areaname'] = area						
               propertyIndex = searchForm.cleaned_data['propertyType']
               if propertyIndex!='1':
                    propertyType = PROPERTY_CHOICES[int(propertyIndex)-1][1]
                    filtersSet1['propertytype__propertytypename'] = propertyType     
               homeIndex = searchForm.cleaned_data['homeType']
               if homeIndex!='1':
                    homeType = HOME_CHOICES[int(homeIndex)-1][1]
                    filtersSet1['housetype__housetypename'] = homeType     
               
               # get the input to this textbox
               priceMax = searchForm.cleaned_data['priceMax']

               # get the inputs to these checkboxes then add to filterSet2 to be used in the query later      
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

               # Filter round 1: get the queryset with the filtersSet1 
               housingResults = Housing.objects.filter(**filtersSet1)
               
               # Filter round 2: filter the result of filter round 1. this time, filter based on the max cost
               results2 = []
               if priceMax!=None:
                    for result in housingResults:
                         result2temp = RoomCost.objects.filter(housingid=result.housingid, cost__lte = priceMax).first()
                         if result2temp!=None: 
                              results2.append(result2temp.housingid.housingid)
               else:
                    results2 = [result.housingid for result in housingResults]     

               # Filter round 3: filter the result of filter round 2. this time, filter based on the filtersSet2 
               results3 = []
               if len(filtersSet2)==0:
                    results3=results2
               else:
                    for result in results2:
                         housingTemp = HousingAdditionalInfo.objects.filter(housingid=result)
                         ctr = 0
                         for filters in filtersSet2:
                              result3temp = housingTemp.filter(additionalinfoid__additionalinfoname=filters).first()
                              if result3temp == None:
                                   break
                              ctr = ctr+1
                         if ctr==len(filtersSet2):
                              results3.append(result3temp.housingid.housingid)
               
               
               # do this so that the list can be passed to the enduserSearchResult method
               request.session['searchResult'] = results3
               # go to enduserSearchResult method to display the search result 
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
     return render(request, 'mainpage/login_owner.html', content)
