from django import forms
from django.contrib.auth.forms import UserCreationForm
from account.models import Account

class UserRegistrationForm(UserCreationForm):
	class Meta:
		model=Account
		fields = '__all__'