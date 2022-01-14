from sys import setprofile
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from cloudinary.models import CloudinaryField
from django.db.models.deletion import CASCADE,SET_NULL
from django.contrib.auth.models import User

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
    
    
class NeighborHood(models.Model):
    name = models.CharField(max_length=60)
    location = models.CharField(max_length=60)
    admin = models.ForeignKey(setprofile,on_delete=CASCADE,related_name='administrator')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    population = models.IntegerField(null=True,blank = True)  
    police_address = models.CharField(max_length=60,blank=True,null=True)
    police_contact = models.IntegerField(null=True,blank = True)
    police_email = models.EmailField(max_length=50,blank=True,null=True)
    hospital_address = models.CharField(max_length=60,blank=True,null=True)
    hospital_contact = models.IntegerField(null=True,blank = True)
    hospital_email = models.EmailField(max_length=50,blank=True,null=True)
    image = CloudinaryField('image')

    def create_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def find_neighborhood(cls, neighborhood_id):
        return cls.objects.filter(id=neighborhood_id)
    
    def __str__(self):
        return self.name
    
class Business(models.Model):
    name =models.CharField(max_length=60)
    description = models.TextField()
    image = CloudinaryField('image')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    neighborhood = models.ForeignKey(NeighborHood,on_delete=CASCADE,related_name='business', null=True, blank=True)
    user = models.ForeignKey(User,on_delete=CASCADE)
    email = models.EmailField()
    phone_number = models.IntegerField(null=True,blank = True)

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def search_businesses(cls, business):
        return cls.objects.filter(name__icontains=business).all()

    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=144)
    post = models.TextField()
    image = CloudinaryField('image')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User,on_delete=CASCADE,related_name='poster')

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    @classmethod
    def show_posts(cls):
        posts = cls.objects.all()
        return posts

    def __str__(self):
        return self.title

