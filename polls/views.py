from django.shortcuts import render, redirect 
from django.http import HttpResponse
from .models import *
from .forms import VoucherForm, CreateUserForm
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required



# authentification system start 



# authentification system end 
#@login_required(login_url='login')
def home(request):
	return render(request,'home.html')

#@login_required(login_url='login')
def base2(request):
	return render(request,'base2.html')

#@login_required(login_url='login')
def crudVoucher(request):
	vouchers = Voucher.objects.all()

	return render(request, 'pages/crudVoucher.html', {'vouchers':vouchers})		

#@login_required(login_url='login')
def createVoucher(request):
	form = VoucherForm()
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = VoucherForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/polls/crudVoucher')

	context = {'form':form}
	return render(request, 'pages/voucher_form.html', context)

#@login_required(login_url='login')
def updateVoucher(request, pk):

	voucher = Voucher.objects.get(id=pk)
	form = VoucherForm(instance=voucher)

	if request.method == 'POST':
		form = VoucherForm(request.POST, instance=voucher)
		if form.is_valid():
			form.save()
			return redirect('/polls/crudVoucher')

	context = {'form':form}
	return render(request, 'pages/voucher_form.html', context)

#@login_required(login_url='login')
def deleteVoucher(request, pk):
	voucher = Voucher.objects.get(id=pk)
	if request.method == "POST":
		voucher.delete()
		return redirect('/polls/crudVoucher')

	context = {'item':voucher}
	return render(request, 'pages/delete_voucher.html', context)	

#@login_required(login_url='login')
def login(request):
	return render(request,'accounts/login.html')	

    	