from django.urls import path

from . import views

#define paths to different web pages i.e. views for views.py
#if user in empty path in app, goto views.function  
urlpatterns = [
path("",views.login,name="login"),
path("validate_user/",views.validate_user,name="validate_user"),
path("display_category/",views.display_category,name="display_category"),

]
