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
	# django doe sn't know type of ToDoList object, define ToDoList obj as FoerignKey 
	#ondelete CASCADE means if ToDoList is deleted, all Item in it must be deleted
	todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
	text = models.CharField(max_length=1000)
	complete = models.BooleanField()

	def __str__(self):
		return self.text


class Author(models.Model):
	name = models.CharField(max_length=255)
	def __str__(self):
		return self.name

class Publisher(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name

class Book(models.Model):
	isbn = models.CharField(max_length=255)

	#foreign keys
	publisher = models.ForeignKey(Publisher,on_delete=models.CASCADE)
	author_name = models.ForeignKey(Author,on_delete=models.CASCADE)
	
	year = models.PositiveIntegerField()
	title = models.CharField(max_length=255)
	price = models.PositiveIntegerField()
	num_sold = models.PositiveIntegerField(default=0)

	def __str__(self):
		return self.title


class Warehouse(models.Model):
	warehouse_code = models.PositiveIntegerField()

	#foreign key
	isbn = models.ForeignKey(Book,on_delete=models.CASCADE)
	count  = models.PositiveIntegerField(default=0)

	
	def __str__(self):	
		return self.warehouse_code


class Category(models.Model):
	name = models.CharField(max_length=255)
	isbn = models.ForeignKey(Book,on_delete=models.CASCADE)


class Cart(models.Model):
	cart_id = models.PositiveIntegerField()
	isbn = models.ForeignKey(Book,on_delete=models.CASCADE)
	count = models.PositiveIntegerField()

class Customer(models.Model):
	customer_email = models.CharField(max_length=255)
	customer_name = models.CharField(max_length=255)
	cart_id = models.ForeignKey(Cart,on_delete=models.CASCADE)

