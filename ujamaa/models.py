from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.


class Neighbourhood(models.Model):
  title = models.CharField(max_length=200, verbose_name='Neighbourhood Title', null=True, blank=True)
  description = models.TextField(max_length=200, verbose_name='Description')
  location = models.CharField(max_length=150, verbose_name='Neighbourhood Location', null=True, blank=True)
  county = models.CharField (max_length=150, verbose_name='Neighbourhood County', null=True, blank=True)
  neighbourhood_image = models.ImageField(default='default.jpg', upload_to='profile_pics')
  neighbourhood_admin= models.ForeignKey(User, on_delete=models.CASCADE)
  health_department= models.CharField (max_length=100, verbose_name='Health')
  
  police_department= models.CharField (max_length=100, verbose_name='Police')
  
  date_created= models.DateTimeField(auto_now_add=True, verbose_name='Date Created')
  date_updated= models.DateTimeField(auto_now=True, verbose_name='Date Updated')


  def __str__(self):
      return self.title

  def get_neighbourhood(self):
    neighbourhood = Neighbourhood.objects.all()
    return neighbourhood

  def delete_neighbourhood(self):
    self.delete()

  def save_neighbourhood(self):
    self.save()

  def get_neighbourhood(self,neighbourhood_id):
    neighbourhood = Neighbourhood.objects.filter(self=neighbourhood_id)
    return neighbourhood

  # def update_neighbourhood(self,neighbourhood):



class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  image = models.ImageField(default='default.jpg', upload_to='profile_pics')
  neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE,null=True)
  Bio = models.TextField(max_length=300, blank=True, null=True)

  def __str__(self):
    return f'{self.user.username} Profile'


    
    
    
class Business(models.Model):
  name = models.CharField(max_length=200, blank=True)
  description = models.TextField(blank=True)
  business_email = models.EmailField(max_length=200, blank=True)
  business_type = models.CharField (max_length=150, blank=True)
  user = models.ForeignKey (Profile,on_delete=models.CASCADE)
  date_created = models.DateTimeField(auto_now_add=True)
  date_updated = models.DateTimeField(auto_now=True)



def __str__(self):
  return str(self.name)
    
def get_business(self):
  business = Business.objects.all()
  return business

def create_business(self):
  self.save()


class Post(models.Model):
  title = models.CharField(max_length=255)
  image =models.ImageField(upload_to='media')
  content = models.TextField(blank=True, null=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, default=1)
  date_posted = models.DateTimeField(auto_now_add=True)