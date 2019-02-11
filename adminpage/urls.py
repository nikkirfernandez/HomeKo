# CODE HISTORY #
# Sontillano     # Feb 12, 2019     # added paths for enduserHome, enduserSearchResult, enduserRecord, enduserRequest, ownerLogin

# File creation date: Feb. 12, 2019

from django.urls import path

from . import views

urlpatterns = [
     path('login/', views.login, name='login'),
     path('home/', views.home, name='home'),
     path('<table>/', views.tablePage, name='tablePage'),
     path('Additionalinfo/add/', views.addAdditionalInfo, name='addAdditionalInfo'),
]    