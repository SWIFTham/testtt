from django.shortcuts import render
from account.forms import UserRegistrationForm
# Create your views here.
def register(request):
	context={}
	if request.POST:
		form=UserRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
		context['register-form']=form

	else:
	    form=UserRegistrationForm()
	    context['register-form']=form
	    return render(request, "account/register.html", context)	    		

def login_view(request):
	return render(request, "account/login.html", context)