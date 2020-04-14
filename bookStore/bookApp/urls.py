from django.urls import path

from . import views

#define paths to different web pages i.e. views for views.py

#if user in empty path in app, goto views.index 
urlpatterns = [
path("",views.index,name="index"),
]