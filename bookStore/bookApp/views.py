from django.shortcuts import render
from django.http import HttpResponse

from django.http import HttpResponseRedirect

from .forms import EmailForm
from .forms import CategoryForm
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
		#get categories 
		cats = CategoryForm()
		return render(request,'dashboard.html',{'user_email':user_email, 'cats':cats})
	form = EmailForm()
	return render(request,'login.html',{'form':form})


def display_category(request):
	category_selected = request.POST.get('category_selected', False)
	book_isbn = Category.objects.all().filter(name=category_selected)
	books_to_display = []
	for b in book_isbn:
		books_to_display.append((b.isbn))
	return render(request,'display_categories.html',{'books_to_display':books_to_display, 'category':category_selected})	
#	return HttpResponse(str(res[0][1].isbn))


