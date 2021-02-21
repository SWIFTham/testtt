from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class BusinessPartner(models.Model):
	name = models.CharField(max_length=200, null=True)
	field = models.CharField(max_length=200, null=True)
	contact = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

class Voucher(models.Model):
	name = models.CharField(max_length=200, null=True)
	description = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	businesspartner = models.ForeignKey(BusinessPartner, on_delete=models.CASCADE)






	
