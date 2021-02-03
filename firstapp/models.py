from django.db import models

# Create your models here.
from django import forms  

class Login(models.Model):
	  username = models.TextField(max_length=50)
	  emailid = models.CharField(max_length=20)
	  password = models.CharField(max_length=20)
	  

class Registration(models.Model):
	  username = models.CharField(max_length=50)
	  email = models.CharField(max_length=20)
	  password = models.CharField(max_length=20)
	  password = models.CharField(max_length=20)

class Contact(models.Model):
	  fullname = models.CharField(max_length=50)
	  email = models.CharField(max_length=20)
	  message = models.TextField(max_length=20) 

class Imagetable(models.Model):
	  image = models.CharField(max_length=50)
	  price =models.IntegerField()
	 
	 

class Meta:
      db_table = "Contact"

class Meta:
     db_table = "Login"	

class Meta:
     db_table = "Registration"	

class  Imagetable:
	  db_table = "Imagetable"





