from django.db import models

# Create your models here.

class FBookLogin(models.Model):
	log_email=models.CharField(max_length=30)
	log_password=models.CharField(max_length=30)
	

class FBookSign(models.Model):
	sign_first=models.CharField(max_length=30)
	sign_last=models.CharField(max_length=30)
	sign_email=models.CharField(max_length=30)
	sign_password=models.CharField(max_length=30)
	sign_day=models.CharField(max_length=30)
	sign_month=models.CharField(max_length=30)
	sign_year=models.CharField(max_length=30)