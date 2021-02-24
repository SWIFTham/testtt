from django.shortcuts import render
from account.forms import UserRegistrationForm
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
	

def login_view(request):
	return render(request, "login.html")