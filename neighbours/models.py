from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models.deletion import CASCADE,SET_NULL
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User,primary_key=True,verbose_name='user',related_name='profile', on_delete=models.CASCADE)
    bio = models.TextField(max_length=500,blank=True,null=True)
    birth_date = models.DateField(blank=True,null=True)
    neighborhood = models.ForeignKey('NeighborHood', on_delete=SET_NULL,null=True, related_name='people', blank=True)
    picture = CloudinaryField('image',default='static/usericon.png',blank=True)
    email = models.EmailField(max_length=50,blank=True,null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()




class NeighborHood(models.Model):
  name = models.CharField(max_length=60)
  location = models.CharField(max_length=60)
  admin = models.ForeignKey(UserProfile,on_delete=CASCADE,related_name='administrator')
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