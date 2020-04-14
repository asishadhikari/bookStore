from django import forms

class EmailForm(forms.Form):
    user_email = forms.EmailField(label='Enter email', max_length=100)
