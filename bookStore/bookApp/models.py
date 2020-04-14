from django.db import models

# Create your models here with attributes, methods

#create model which inherits from models.model which
# is database model class setup from django

class Author(models.Model):
	name = models.CharField(max_length=255)
	def __str__(self):
		return self.name

class Publisher(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name

class Book(models.Model):
	isbn = models.PositiveIntegerField()

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
		return str(self.warehouse_code)


class Category(models.Model):
	name = models.CharField(max_length=255)
	isbn = models.ForeignKey(Book,on_delete=models.CASCADE)

class Customer(models.Model):
	customer_email = models.CharField(max_length=255)
	customer_name = models.CharField(max_length=255)

class Cart(models.Model):
	cart_id = models.PositiveIntegerField()
	isbn = models.ForeignKey(Book,on_delete=models.CASCADE)
	count = models.PositiveIntegerField()
	customer_email = models.ForeignKey(Customer, on_delete=models.CASCADE)



