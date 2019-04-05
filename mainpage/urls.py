# This is a course requirement for CS 192 Software Engineering II under the supervision of Asst. Prof. Ma. Rowena C. Solamo of the Department of Computer Science, College of Engineering, University of the Philippines, Diliman for the AY 2018-2019.

# CODE HISTORY #
# Sontillano	# March 31, 2019  # added paths for enduserHome, enduserSearchResult, enduserRecord, enduserRequest, ownerLogin
# Fernandez     # Apr 5, 2019     # added path for reqister

# File creation date: March. 31, 2019

from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
     path('', views.enduserHome, name='enduserHome'),
     path('request/', views.enduserRequest, name='enduserRequest'),
     path('ownerlogin/', views.ownerLogin, name='ownerLogin'),
     path('search/', views.enduserSearchResult, name='enduserSearchResult'),
     path('record/<housingid>/', views.enduserRecord, name='enduserRecord'),
     path('ownerlogin/signup/', views.register, name='register'),
 ]    
