# License: MIT License
# CODE HISTORY #
# Sontillano     # Feb 5, 2019     # added paths for enduserHome, enduserSearchResult, enduserRecord, enduserRequest, ownerLogin

# File creation date: Feb. 5, 2019

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
     #path('ownerlogin/', auth_views.LoginView.as_view(template_name = 'mainpage/login_owner.html'), name='ownerLogin'),
     path('logout/', auth_views.LogoutView.as_view(template_name = 'mainpage/logout.html'), name='logout'),
]    
