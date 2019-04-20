# License: MIT License

# CODE HISTORY #
# Sontillano     # Feb 5, 2019     # added enduserHome, enduserSearchResult, enduserRecord, enduserRequest, ownerLogin
# Sontillano     # Feb 6, 2019     # fixed enduserHome, enduserSearchResult, enduserRecord 
# Sontillano     # Mar 5, 2019     # added comment verification
# Sontillano     # Mar 6, 2019     # added comment report functionality
# Sontillano     # Mar 20, 2019    # send request functionality added
# Fernandez      # Apr 3, 2019     # added register

# File creation date: Feb. 1, 2019


from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.template.loader import render_to_string
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Count
import datetime

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
               checkboxNames = {'kitchen': 12, 'aircon': 2, 'washer': 3, 'dryer': 4, 'wifi': 5, 'iron': 6, 'tv': 7, 'parking': 8, 'pet': 9, 'smoking': 10, 'curfew': 11}    
               for i,j in checkboxNames.items():
                    if(searchForm.cleaned_data[i])==True:
                         filtersSet2.append(Additionalinfo.objects.get(additionalinfoid=j))
                         
               # Filter round 1: get the queryset with the filtersSet1 
               housingResults = Housing.objects.filter(**filtersSet1)
               
               # Filter round 2: filter the result of filter round 1. this time, filter based on the max cost
               if priceMax!=None:
                    housingResults = RoomCost.objects.filter(housingid__in=housingResults, cost__lte = priceMax).values('housingid').distinct()
                         
               # Filter round 3: filter the result of filter round 2. this time, filter based on the filtersSet2 
               if len(filtersSet2)!=0:
                    housingResults = HousingAdditionalInfo.objects.filter(housingid__in=housingResults, additionalinfoid__in=filtersSet2).annotate(num_additionalinfoid=Count('additionalinfoid')).filter(num_additionalinfoid=len(filtersSet2)).values('housingid')
               
               results = []
               for i in housingResults:
                    results.append(i.housingid)
               # do this so that the list can be passed to the enduserSearchResult method
               request.session['searchResult'] = results
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
               if priceMin['cost__min']==None and priceMax['cost__max']==None:
                    priceRange.append("")
               elif priceMin['cost__min']==None: 
                    priceRange.append(str(priceMax['cost__max']))
               elif priceMax['cost__max']==None: 
                    priceRange.append(str(priceMin['cost__min']))
               else:
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
               checkboxNames = {'kitchen': 12, 'aircon': 2, 'washer': 3, 'dryer': 4, 'wifi': 5, 'iron': 6, 'tv': 7, 'parking': 8, 'pet': 9, 'smoking': 10, 'curfew': 11}    
               for i,j in checkboxNames.items():
                    if(searchForm.cleaned_data[i])==True:
                         filtersSet2.append(Additionalinfo.objects.get(additionalinfoid=j))
                         
               # Filter round 1: get the queryset with the filtersSet1 
               housingResults = Housing.objects.filter(**filtersSet1)
               
               # Filter round 2: filter the result of filter round 1. this time, filter based on the max cost
               if priceMax!=None:
                    housingResults = RoomCost.objects.filter(housingid__in=housingResults, cost__lte = priceMax).values('housingid').distinct()
                         
               # Filter round 3: filter the result of filter round 2. this time, filter based on the filtersSet2 
               if len(filtersSet2)!=0:
                    housingResults = HousingAdditionalInfo.objects.filter(housingid__in=housingResults, additionalinfoid__in=filtersSet2).annotate(num_additionalinfoid=Count('additionalinfoid')).filter(num_additionalinfoid=len(filtersSet2)).values('housingid')
               
               results = []
               for i in housingResults:
                    results.append(i.housingid)
               # do this so that the list can be passed to the enduserSearchResult method
               request.session['searchResult'] = results
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
     owner = HousingOwner.objects.filter(housingid=housingid).first()
     if owner!=None:
          ownerName = str(owner.ownerid.firstname) + " " + str(owner.ownerid.lastname)
          contact = Contact.objects.filter(ownerid=owner.ownerid)
          contactNo = [ c.contactno for c in contact]
          contactNo = ", ".join(contactNo)
     else:
          ownerName = None
          contactNo = None
     housingRooms = RoomCost.objects.filter(housingid=housingid)
     amenities = HousingAdditionalInfo.objects.filter(housingid=housingid, additionalinfoid__additionalinfotype=1)
     facilities = HousingAdditionalInfo.objects.filter(housingid=housingid, additionalinfoid__additionalinfotype=2)
     rules = HousingAdditionalInfo.objects.filter(housingid=housingid, additionalinfoid__additionalinfotype=3)
     comments = Feedback.objects.filter(housingid=housingid, status=2)

     searchForm = SearchHousing()
     commentForm = AddComment()
          
     # if the user submitted the form
     if request.method == "POST" :
          searchForm = SearchHousing(request.POST)
          commentForm = AddComment(request.POST)
          if commentForm.is_valid():
               post = commentForm.save(commit=False)
               post.housingid = Housing.objects.get(housingid=housingid)
               post.status = 1
               post.dateposted = datetime.date.today()   
               post.save()
               return HttpResponseRedirect(reverse('enduserRecord', args=(housingid,)))
          elif searchForm.is_valid():     
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
               checkboxNames = {'kitchen': 12, 'aircon': 2, 'washer': 3, 'dryer': 4, 'wifi': 5, 'iron': 6, 'tv': 7, 'parking': 8, 'pet': 9, 'smoking': 10, 'curfew': 11}    
               for i,j in checkboxNames.items():
                    if(searchForm.cleaned_data[i])==True:
                         filtersSet2.append(Additionalinfo.objects.get(additionalinfoid=j))
                         
               # Filter round 1: get the queryset with the filtersSet1 
               housingResults = Housing.objects.filter(**filtersSet1)
               
               # Filter round 2: filter the result of filter round 1. this time, filter based on the max cost
               if priceMax!=None:
                    housingResults = RoomCost.objects.filter(housingid__in=housingResults, cost__lte = priceMax).values('housingid').distinct()
                         
               # Filter round 3: filter the result of filter round 2. this time, filter based on the filtersSet2 
               if len(filtersSet2)!=0:
                    housingResults = HousingAdditionalInfo.objects.filter(housingid__in=housingResults, additionalinfoid__in=filtersSet2).annotate(num_additionalinfoid=Count('additionalinfoid')).filter(num_additionalinfoid=len(filtersSet2)).values('housingid')
               
               results = []
               for i in housingResults:
                    results.append(i.housingid)
               # do this so that the list can be passed to the enduserSearchResult method
               request.session['searchResult'] = results
               # go to enduserSearchResult method to display the search result 
               return HttpResponseRedirect(reverse('enduserSearchResult', args=()))

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
          'commentForm' : commentForm,
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
          requestForm = AddRequest(request.POST)

          if requestForm.is_valid():
               post = requestForm.save(commit=False)
               post.status = 1
               post.datesent = datetime.date.today()   
               post.save()
          elif searchForm.is_valid():     
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
               checkboxNames = {'kitchen': 12, 'aircon': 2, 'washer': 3, 'dryer': 4, 'wifi': 5, 'iron': 6, 'tv': 7, 'parking': 8, 'pet': 9, 'smoking': 10, 'curfew': 11}    
               for i,j in checkboxNames.items():
                    if(searchForm.cleaned_data[i])==True:
                         filtersSet2.append(Additionalinfo.objects.get(additionalinfoid=j))
                         
               # Filter round 1: get the queryset with the filtersSet1 
               housingResults = Housing.objects.filter(**filtersSet1)
               
               # Filter round 2: filter the result of filter round 1. this time, filter based on the max cost
               if priceMax!=None:
                    housingResults = RoomCost.objects.filter(housingid__in=housingResults, cost__lte = priceMax).values('housingid').distinct()
                         
               # Filter round 3: filter the result of filter round 2. this time, filter based on the filtersSet2 
               if len(filtersSet2)!=0:
                    housingResults = HousingAdditionalInfo.objects.filter(housingid__in=housingResults, additionalinfoid__in=filtersSet2).annotate(num_additionalinfoid=Count('additionalinfoid')).filter(num_additionalinfoid=len(filtersSet2)).values('housingid')
               
               results = []
               for i in housingResults:
                    results.append(i.housingid)
               # do this so that the list can be passed to the enduserSearchResult method
               request.session['searchResult'] = results
               # go to enduserSearchResult method to display the search result 
               return HttpResponseRedirect(reverse('enduserSearchResult', args=()))
     
     searchForm = SearchHousing()
     requestForm = AddRequest()

     content = {
          'areaChoices' : AREA_CHOICES,
          'propertyChoices' : PROPERTY_CHOICES,
          'homeChoices' : HOME_CHOICES,
          'amenityChoices' : AMENITY_CHOICES,
          'facilityChoices' : FACILITY_CHOICES,
          'ruleChoices' : RULE_CHOICES,
          'requestChoices' : REQUEST_TYPE_CHOICES,
          'requestForm' : requestForm,
     }
     return render(request, 'mainpage/request_enduser.html', content)

# Method name: ownerLogin
# Creation date: Apr 3, 2019 
# Purpose: log in form for the housing owners
# Calling arguments: No arguments for calling this function.
# Required files: login_owner.html
def ownerLogin(request):
     if request.user.is_authenticated:
          if request.user.is_superuser:
               return HttpResponseRedirect('/adminpage/home')        
          else:
               return HttpResponseRedirect('/ownerpage/home')
     else:
          # if the user submitted the form
          incorrect = False
          if request.method == "POST" :
               searchForm = SearchHousing(request.POST)
               ownerForm = OwnerLogin(request.POST)
               if "login" in request.POST:
                    if ownerForm.is_valid():
                         uname = request.POST['uname']
                         pw = request.POST['pw']
                         user = authenticate(request, username=uname, password=pw)
                         if user is not None:
                              if user.is_superuser==0:    
                                   login(request, user)
                                   owner = Owner.objects.get(ownername=uname).ownerid
                                   request.session['ownerid'] = owner
                                   return redirect('ownerhome')
                              else:
                                   incorrect = True
                         else:
                              incorrect = True
                    else:
                         return HttpResponseRedirect(reverse('ownerLogin'))
               elif searchForm.is_valid():     
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
                    checkboxNames = {'kitchen': 12, 'aircon': 2, 'washer': 3, 'dryer': 4, 'wifi': 5, 'iron': 6, 'tv': 7, 'parking': 8, 'pet': 9, 'smoking': 10, 'curfew': 11}    
                    for i,j in checkboxNames.items():
                         if(searchForm.cleaned_data[i])==True:
                              filtersSet2.append(Additionalinfo.objects.get(additionalinfoid=j))
                         
                    # Filter round 1: get the queryset with the filtersSet1 
                    housingResults = Housing.objects.filter(**filtersSet1)
               
                    # Filter round 2: filter the result of filter round 1. this time, filter based on the max cost
                    if priceMax!=None:
                         housingResults = RoomCost.objects.filter(housingid__in=housingResults, cost__lte = priceMax).values('housingid').distinct()
                         
                    # Filter round 3: filter the result of filter round 2. this time, filter based on the filtersSet2 
                    if len(filtersSet2)!=0:
                         housingResults = HousingAdditionalInfo.objects.filter(housingid__in=housingResults, additionalinfoid__in=filtersSet2).annotate(num_additionalinfoid=Count('additionalinfoid')).filter(num_additionalinfoid=len(filtersSet2)).values('housingid')
               
                    results = []
                    for i in housingResults:
                         results.append(i.housingid)
                    # do this so that the list can be passed to the enduserSearchResult method
                    request.session['searchResult'] = results
                    # go to enduserSearchResult method to display the search result 
                    return HttpResponseRedirect(reverse('enduserSearchResult', args=()))
     
          searchForm = SearchHousing()
          ownerForm = OwnerLogin()

          content = {
               'areaChoices' : AREA_CHOICES,
               'propertyChoices' : PROPERTY_CHOICES,
               'homeChoices' : HOME_CHOICES,
               'amenityChoices' : AMENITY_CHOICES,
               'facilityChoices' : FACILITY_CHOICES,
               'ruleChoices' : RULE_CHOICES,
               'incorrect' : incorrect,
               'ownerForm' : ownerForm,
          }
          return render(request, 'mainpage/login_owner.html', content)

# Method name: ownerLogin
# Creation date: Apr 3, 2019 
# Purpose: account creation form for the housing owners
# Calling arguments: No arguments for calling this function.
# Required files: register_owner.html
def register(request):
     if request.user.is_authenticated:
          if request.user.is_superuser:
               return HttpResponseRedirect('/adminpage/home')        
          else:
               return HttpResponseRedirect('/ownerpage/home')
     else:
          if request.method == 'POST':
               form = OwnerRegistrationForm(request.POST)
               if form.is_valid():
                    post = form.save(commit=False)
                    newOwnerRecord = Owner.objects.create(ownername=post.username, firstname=post.first_name, lastname=post.last_name)
                    newOwnerRecord.save()

                    if post.email == "":
                         post.email = "None"
                    else:
                         newOwnerRecord.email = post.email
                         newOwnerRecord.save()

                    if request.POST['contact'] != "":
                        newContactRecord = Contact.objects.create(ownerid=newOwnerRecord, contactno=request.POST['contact']) 

                    post.save()

                    user = authenticate(request, username=post.username, password=post.password1)
                    if user is not None:
                         login(request, user)
                         request.session['ownerid'] = newOwnerRecord.ownerid
                         return redirect('ownerhome')

                    #return HttpResponseRedirect(reverse('enduserRecord', args=(housingid,)))
                    return redirect('ownerLogin')
     
          form = OwnerRegistrationForm()

          content = {
               'form': form,
          }
     return render(request,'mainpage/register_owner.html', content)