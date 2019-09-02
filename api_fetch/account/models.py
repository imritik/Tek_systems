from django.db import models
from django.contrib.auth.models import User
from datetime import datetime    
from django.core.validators import RegexValidator

                                                                                          		
class Temp(models.Model):                                
	uid=models.CharField(max_length=12, validators=[RegexValidator(r'^\d{1,10}$')])
	name=models.CharField(max_length=100)
	address=models.CharField(max_length=100)
	pincode=models.IntegerField(default=245101)
	purpose=models.CharField(blank=True,max_length=1000)
	whoto=models.CharField(blank=True,max_length=50)
	email=models.CharField(blank=True,max_length=70)
	phone=models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
	date=models.DateTimeField(default=datetime.now,blank=True,null=True)               


class Visitor_perma(models.Model):
	uid=models.CharField(max_length=12, validators=[RegexValidator(r'^\d{1,10}$')]) 
	name=models.CharField(max_length=100)  
	address=models.CharField(max_length=100)
	email=models.CharField(blank=True,max_length=70)
	phone=models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])                         
	pincode=models.IntegerField(default=245101)    
	purpose=models.CharField(blank=True,max_length=1000)   
	whoto=models.CharField(blank=True,	max_length=50)
	date=models.DateTimeField(default=datetime.now,blank=True,null=True)     




# # MODEL 2
# class admin(models.Model):
# 	name = models.CharField(max_length=100)
# 	user_name=models.OneToOneField(User)
# 	password=models.CharField(widget=forms.PasswordInput)
# 	created_at = models.DateTimeField(default=datetime.now, blank=True)


# # # MODEL 3
# class visit_detail(models.Model):
# 	uid=models.IntegerField()
# 	purpose=models.TextField()
# 	date = models.DateTimeField(default=datetime.now, blank=True)
# 	no_of_visits=models.AutoField()


# # # MODEL 3
# class perma(models.Model):
# 	phone=models.CharField(max_length=12)
# 	visits=models.AutoField()
# 	name=models.CharField(max_length=100)
# 	dob=models.DateField()
# 	address=models.TextField()
# 	uid=models.IntegerField()
# 	date = models.DateTimeField(default=datetime.now, blank=True)


# class receip(models.Model):
# 	name = models.CharField(max_length=100)
# 	user_name=models.OneToOneField(User)
# 	password=models.CharField(widget=forms.PasswordInput)

