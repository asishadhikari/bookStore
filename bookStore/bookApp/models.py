from django.db import models

# Create your models here with attributes, methods

#create model which inherits from models.model which
# is database model class setup from django

class ToDoList(models.Model):
	#an attribute is created as a class variable with field type
	name = models.CharField(max_length=200)
	

	#define a method for print() calls	 
	def __str__(self):
		return self.name



# A todoList has many items
class Item(models.Model):
	# django doesn't know type of ToDoList object, define ToDoList obj as FoerignKey 
	#ondelete CASCADE means if ToDoList is deleted, all Item in it must be deleted
	todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
	text = models.CharField(max_length=1000)
	complete = models.BooleanField()

	def __str__(self):
		return self.text


class Author(models.Model):
	name = models.CharField(max_length=255)


class Publisher(models.Model):
	name = models.CharField(max_length=255)


class Book(models.Model):
	#foreign keys
	publisher = models.ForeignKey(Publisher,on_delete=models.CASCADE)
	author_name = models.ForeignKey(Author,on_delete=models.CASCADE)
	
	isbn = models.CharField(max_length=255)
	year = models.PositiveSmallIntegerField()
	title = models.CharField(max_length=255)
	price = models.PositiveSmallIntegerField()




