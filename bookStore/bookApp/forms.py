from django import forms
from .models import Category, Author

class EmailForm(forms.Form):
    user_email = forms.EmailField(label='Enter email', max_length=100)

class CategoryForm(forms.Form):
	ca = Category.objects.all()
	categories = []
	for c in ca:
		categories.append((c.name,c.name))
	category_selected = forms.CharField(label='Select Category', widget=forms.Select(choices=categories))
	
class TextBox(forms.Form):
	text_box = forms.CharField(label='Enter Author Name',max_length=100)



SEARCH_CHOICES =  [('isbn', 'isbn'),
    ('title', 'title'),
    ('publisher','publisher'),

]

class RadioForm(forms.Form):
	search_technique= forms.CharField(label='Please select search preference', widget=forms.RadioSelect(choices=SEARCH_CHOICES))
	text_box = forms.CharField(label='Specify...',max_length=100)