from django.urls import path

from . import views

#define paths to different web pages i.e. views for views.py
#if user in empty path in app, goto views.function  
urlpatterns = [
path("",views.login,name="login"),
path("validate_user/",views.validate_user,name="validate_user"),
path("display_category/",views.display_category,name="display_category"),
path("display_author/",views.display_author,name="display_author"),
path("search_author/",views.search_author,name="search_author"),
path("search/",views.search,name="search"),
path("search_result/",views.search_result,name="search_result"),

]
