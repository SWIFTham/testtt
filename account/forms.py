from django import forms
from django.contrib.auth.forms import UserCreationForm
from account.models import Account

class UserRegistrationForm(UserCreationForm):
	class Meta:
		model=Account
		fields = ['company_name', 'email', 'phone', 'password1', 'password2']