from django.contrib import admin

# Register your models here.
from .models import *

class FBookLoginAdmin(admin.ModelAdmin):
	list_display=['log_email','log_password',]


class FBookSignAdmin(admin.ModelAdmin):
	list_display=['sign_first','sign_last','sign_email','sign_password','sign_day','sign_month','sign_year',]
admin.site.register(FBookLogin,FBookLoginAdmin)
admin.site.register(FBookSign,FBookSignAdmin)