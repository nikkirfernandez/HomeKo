
# CODE HISTORY #
# Sontillano     # Feb 5, 2019     # added paths for enduserHome, enduserSearchResult, enduserRecord, enduserRequest, ownerLogin

# File creation date: Feb. 5, 2019

from django.urls import path

from . import views

urlpatterns = [
     path('', views.enduserHome, name='enduserHome'),
     path('request/', views.enduserRequest, name='enduserRequest'),
     path('ownerlogin/', views.ownerLogin, name='ownerLogin'),
     path('search/', views.enduserSearchResult, name='enduserSearchResult'),
     path('record/<housingid>/', views.enduserRecord, name='enduserRecord'),
]