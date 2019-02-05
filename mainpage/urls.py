from django.urls import path

from . import views

app_name = 'mainpage'
urlpatterns = [
    path('', views.enduserHome, name='enduserHome'),
    path('search/', views.enduserSearchResult, name='enduserSearchResult'),
    path('record/', views.enduserRecord, name='enduserRecord'),
]