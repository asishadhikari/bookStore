from django.shortcuts import render
from django.http import HttpResponse

from django.http import HttpResponseRedirect

from .forms import EmailForm
from django.db import connection
from .models import Author, Publisher, Book, Warehouse, Category, Customer, Cart

#use models to control the view

# Create your views here.
#serves all HTTP requests  
#create functions that represent view




def login(request):
	form = EmailForm()
	return render(request,'login.html',{'form':form})


def validate_user(request):
	user_email = request.POST['user_email']
	c = Customer.objects.all().filter(customer_email = user_email)
	if c.count() > 0:
		return HttpResponse("Record exists")
	return HttpResponse("No such user")