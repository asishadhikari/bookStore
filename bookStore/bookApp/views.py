from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#serves all HTTP requests  
#create functions that represent view

def index(response):
	return HttpResponse("<h1>Some HTML code </h1>")

def v1(response):
	return HttpResponse("</h2>View 1</h2>")

