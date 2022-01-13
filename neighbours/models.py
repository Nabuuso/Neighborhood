from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self,full_name,username,email,password,*args,**kwargs):
        if email is None:
            raise TypeError("Email field cannot be null")
        user = self.model(full_name=full_name,username=username,email=email,*args,**kwargs)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self,password,*args,**kwargs):
        user = self.model(**kwargs)
        user.set_password(password)
        user.save()
        return user

class Profile(AbstractBaseUser,PermissionsMixin):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255,unique=True)
    username = models.CharField(max_length=255,unique=True)
    bio = models.TextField(null=True)
    profile_photo = models.ImageField(upload_to="images/profile",null=True)
    password = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name','username','password']
    objects = UserManager()