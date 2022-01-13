from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Profile, UserManager

admin.site.register(Profile)
admin.site.register(UserManager)
