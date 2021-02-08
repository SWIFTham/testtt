from django.shortcuts import render

def home(request):
	return render(request,'home.html')

def register(request):
	return render(request,'pages/register.html')

def connection(request):
	return render(request,'pages/connection.html')	