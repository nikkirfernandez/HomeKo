# This is a course requirement for CS 192 Software Engineering II under the supervision of Asst. Prof. Ma. Rowena C. Solamo of the Department of Computer Science, College of Engineering, University of the Philippines, Diliman for the AY 2018-2019.

# CODE HISTORY #
# Sontillano     # Feb 12, 2019     # added paths

# File creation date: Feb. 12, 2019

from django.urls import path

from . import views

urlpatterns = [
     path('login/', views.login, name='login'),
     path('home/', views.home, name='home'),
     path('<table>/', views.tablePage, name='tablePage'),
     path('Additionalinfo/add/', views.addAdditionalInfo, name='addAdditionalInfo'),
     path('Additionalinfo/<id>/', views.editAdditionalInfo, name='editAdditionalInfo'),
     path('Area/add/', views.addArea, name='addArea'),
     path('Area/<id>/', views.editArea, name='editArea'),
     path('Contact/add/', views.addContact, name='addContact'),
     path('Contact/<id>/', views.editContact, name='editContact'),
     path('Feedback/<id>/', views.editFeedback, name='editFeedback'),
     path('Housetype/add/', views.addHousetype, name='addHousetype'),
     path('Housetype/<id>/', views.editHousetype, name='editHousetype'),
     path('Housing/add/', views.addHousing, name='addHousing'),
     path('Housing/<id>/', views.editHousing, name='editHousing'),
     path('Propertytype/add/', views.addPropertytype, name='addPropertytype'),
     path('Propertytype/<id>/', views.editPropertytype, name='editPropertytype'),
     path('Request/<id>/', views.editRequest, name='editRequest'),
     path('HousingAdditionalinfo/add/', views.addHousingAdditionalInfo, name='addHousingAdditionalInfo'),
     path('HousingAdditionalinfo/<id>/', views.editHousingAdditionalInfo, name='editHousingAdditionalInfo'),
     path('HousingOwner/add/', views.addHousingOwner, name='addHousingOwner'),
     path('HousingOwner/<id>/', views.editHousingOwner, name='editHousingOwner'),
     path('HousingRequest/add/', views.addHousingRequest, name='addHousingRequest'),
     path('HousingRequest/<id>/', views.editHousingRequest, name='editHousingRequest'),
     path('Picture/add/', views.addPicture, name='addPicture'),
     path('Picture/<id>/', views.editPicture, name='editPicture'),
     path('RoomCost/add/', views.addRoomCost, name='addRoomCost'),
     path('RoomCost/<id>/', views.editRoomCost, name='editRoomCost'),
     path('Owner/add/', views.addOwner, name='addOwner'),
     path('Owner/<id>/', views.editOwner, name='editOwner'),
]    