# This is a course requirement for CS 192 Software Engineering II under the supervision of Asst. Prof. Ma. Rowena C. Solamo of the Department of Computer Science, College of Engineering, University of the Philippines, Diliman for the AY 2018-2019.

# CODE HISTORY #
# Sontillano     # Mar 21, 2019     # added paths

# File creation date: Mar 21, 2019

from django.urls import path, include

from . import views

urlpatterns = [
     path('home/', views.home, name='ownerhome'),
     path('logout/', views.ownerlogout, name='ownerlogout'),
     path('account/', views.account, name='account'),
     path('contact/', views.editContactRecord, name='editContactRecord'),
     path('housing/<housingid>', views.editHousingRecord, name='editHousingRecord'),
     path('housing/<housingid>/room', views.editRoomRecord, name='editRoomRecord'),
     path('housing/<housingid>/amenity', views.editAmenityRecord, name='editAmenityRecord'),
     path('housing/<housingid>/facility', views.editFacilityRecord, name='editFacilityRecord'),
     path('housing/<housingid>/rule', views.editRuleRecord, name='editRuleRecord'),

]    