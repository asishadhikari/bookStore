from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(ToDoList)
admin.site.register(Item)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Book)