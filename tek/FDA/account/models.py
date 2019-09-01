from django.db import models
from datetime import datetime

# Create your models here.
class Visitor(models.Model):
	uid = models.CharField(max_length=12)
	name = models.CharField(max_length=100)
	address = models.CharField(max_length=100)
	pincode = models.CharField(max_length=6)
	purpose = models.CharField(blank = True,max_length = 100)
	whoto = models.CharField(blank = True,max_length = 50)
	email = models.EmailField(blank = True,max_length = 70)
	phone = models.CharField(max_length=10)
	date = models.DateTimeField(default = datetime.now,blank = True,null =True)


	
	def __str__(self):
		return self.name;



class Visitor_perma(models.Model):
	uid = models.CharField(max_length=12)
	name = models.CharField(max_length=100)
	address = models.CharField(max_length=100)
	pincode = models.CharField(max_length=6)
	purpose = models.CharField(max_length = 100)
	whoto = models.CharField(max_length = 50)
	email = models.EmailField(max_length = 70)
	phone = models.CharField(max_length=10)
	date = models.DateTimeField(default = datetime.now,null =True)
	


	def __str__(self):
		return self.name
		