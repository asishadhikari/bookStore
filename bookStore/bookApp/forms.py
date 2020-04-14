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
    ('author', 'publisher'),
]

class RadioForm(forms.Form):
	search_technique = forms.MultipleChoiceField(label=" Choose Preferred Search Index ",choices=SEARCH_CHOICES)

