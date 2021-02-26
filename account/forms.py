from django import forms
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from account.models import Account
from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms

class UserRegistrationForm(UserCreationForm):
	class Meta:
		model=Account
		fields = ['company_name', 'email', 'phone', 'password1', 'password2']

#class UserLoginPB():
#	class Meta:
#		model=Account
#		fields = ['company_name', 'password1']

			
		