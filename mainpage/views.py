from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('HELLO WORLD!');
# Create your views here.

def enduserHome(request):
	content = {}
	return render(request, 'mainpage/home.html', content)

def enduserSearchResult(request):
	content = {}
	return render(request, 'mainpage/search_enduser.html', content)

def enduserRecord(request):
	content = {}
	return render(request, 'mainpage/housing_record.html', content)
