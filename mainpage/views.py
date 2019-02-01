from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('HELLO WORLD!');
# Create your views here.
