from django.shortcuts import render, redirect
from account.forms import UserRegistrationForm

from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):
	context={}
	if request.POST:
		form=UserRegistrationForm(request.POST)
		if form.is_valid():
			#print('Printing POST:', request.POST)
			form.save()
			return redirect('login')
		context['register_form']=form
	
	else:
		print('not valid')
		form=UserRegistrationForm()
		context['register_form']=form
	return render(request, "register.html", context)
	

#def login_view(request):
#	return render(request, "login.html")

def login_view(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('company_name')
			password =request.POST.get('password1')
			print(username)
			print(password)

			user = authenticate(request, username=username, password=password)

			if user:
				login(request, user)
				print('okkkk')
				return redirect('home')
			else:

				messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'login.html', context)

		
