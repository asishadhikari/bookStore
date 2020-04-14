from django import forms
from .models import Category

class EmailForm(forms.Form):
    user_email = forms.EmailField(label='Enter email', max_length=100)

class CategoryForm(forms.Form):
	ca = Category.objects.all()
	categories = []
	for c in ca:
		categories.append((c.name,c.name))
	category_selected = forms.CharField(label='Select Category', widget=forms.Select(choices=categories))
	
