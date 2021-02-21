from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class MyAccountManager(BaseUserManager):

	def create_user(self, email, company_name, phone, password=None):
		if not email:
			raise ValueError("email required")
		if not company_name:
			raise ValueError("company required")
		if not phone:
			raise ValueError("phone required")
		
		user= self.model(
			email=self.normalize_email(email),
			company_name=company_name,
			phone=phone
			)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, company_name, phone, password=None):
		user=self.create_user(
			email=email,
		    company_name=company_name,
			phone=phone,
			password=password
			)
		user.is_admin=True
		user.is_superuser=True
		user.save(using=self._db)
		return user
		
		

class Account(AbstractBaseUser):
	email=models.EmailField(verbose_name="email address",max_length=60, unique=True)
	company_name = models.CharField(verbose_name="company name", max_length=200, unique=True)
	phone=models.CharField(max_length=20, verbose_name="company phone")
	date_joined=models.DateTimeField(verbose_name="date joined",auto_now_add=True)
	last_login=models.DateTimeField(verbose_name="last login", auto_now=True)
	is_admin=models.BooleanField(default=False)
	is_active=models.BooleanField(default=True)
	is_staff=models.BooleanField(default=False)
	is_superuser=models.BooleanField(default=False)

	USERNAME_FIELD="email"

	REQUIRED_FIELS=['company_name','phone']

	objects=MyAccountManager()

	def __str__(self):
		return self.company_name

	def has_perm(self, perm, obj=None):
		return self.is_admin

	def has_module_perms(self, app_label):
		return True
	


		