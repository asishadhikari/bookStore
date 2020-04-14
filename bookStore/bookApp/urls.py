from django.urls import path

from . import views

#define paths to different web pages i.e. views for views.py
#if user in empty path in app, goto views.function  
urlpatterns = [
path("",views.index,name="index"),
path("v1/",views.v1,name="view 1"),
]