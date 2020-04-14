from django.shortcuts import render
from django.http import HttpResponse

from django.http import HttpResponseRedirect

from .forms import EmailForm
from .forms import CategoryForm
from .forms import TextBox, RadioForm

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

def display_author(request):
	f = TextBox()
	return render(request,'display_author.html',{'f':f})



def search_author(request):
	author_searched = request.POST.get('text_box')
	#search for the author in database
	a = Author.objects.all().filter(name__icontains=author_searched)
	if not a :
		return HttpResponse("No Books are available by "+ author_searched)
	else:
		#select all boooks by author
		books_obj  = Book.objects.filter(author_name__in = a )
		return render(request,'list_author_books.html',{'books_to_display':books_obj,'author':author_searched})
		


def search(request):
	#instantiate a radio form
	r_form = RadioForm()
	return render(request,'search.html',{'form':r_form})


def search_result(request):
	preferred_method = request.POST.get('search_technique')
	return HttpResponse(preferred_method)