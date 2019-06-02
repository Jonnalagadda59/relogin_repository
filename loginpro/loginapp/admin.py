from django.contrib import admin
from .models import RegistrationData
from .forms import RegistrationForm
class AdminRegistrationData(admin.ModelAdmin):
    list_display = ['first_name','last_name','username','password','mobile','email']
admin.site.register(RegistrationData,AdminRegistrationData)