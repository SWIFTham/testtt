from django.forms import ModelForm
from .models import Voucher
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class VoucherForm(ModelForm):
	class Meta:
		model = Voucher
		fields = '__all__'

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']