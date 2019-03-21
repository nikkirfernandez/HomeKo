# This is a course requirement for CS 192 Software Engineering II under the supervision of Asst. Prof. Ma. Rowena C. Solamo of the Department of Computer Science, College of Engineering, University of the Philippines, Diliman for the AY 2018-2019.

# CODE HISTORY #
# Sontillano     # Mar 21, 2019     # added paths

# File creation date: Mar 21, 2019

from django.urls import path, include

from . import views

urlpatterns = [
     path('home/', views.home, name='home'),
     path('account/', views.account, name='account'),
     path('housing/add', views.addHousingRecord, name='addHousingRecord'),
     path('housing/<housingid>', views.editHousingRecord, name='editHousingRecord'),
]    