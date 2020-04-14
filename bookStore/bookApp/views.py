from django.shortcuts import render
from django.http import HttpResponse

from django.http import HttpResponseRedirect

from .forms import EmailForm

#use models to control the view

# Create your views here.
#serves all HTTP requests  
#create functions that represent view


'''
def get_email(request):
	if request.method=='POST':
		form = EmailForm(request.POST)
		if form.is_valid():
			return HTTPResponseRedirect('/thanks/')

	else:
		form = EmailForm()

	return render(request,'name.html',{'form'}:form)
'''


def login(request):
	form = EmailForm()
	return render(request,'login.html',{'form':form})

def validate_user(request):
	if request.method=='POST':
		return HttpResponse("Hi!")