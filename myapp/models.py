from django.db import models

# Create your models here.
class Student(models.Model):
	name = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
	adhar = models.CharField(max_length=16)
	mobile = models.CharField(max_length=10)