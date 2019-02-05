from django.urls import path

from . import views

urlpatterns = [
    path('', views.enduserHome, name='enduserHome'),
    path('request/', views.enduserRequest, name='enduserRequest'),
    path('ownerlogin/', views.ownerLogin, name='ownerLogin'),
    path('search/', views.enduserSearchResult, name='enduserSearchResult'),
    path('record/', views.enduserRecord, name='enduserRecord'),
]