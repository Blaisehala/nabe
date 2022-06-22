from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Neighbourhood, Business,Post



class UserRegisterForm(UserCreationForm):
  email = forms.EmailField()


  class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
  email = forms.EmailField()


  class Meta:
    model = User
    fields = ['username', 'email']



class ProfileUpdateForm(forms.ModelForm):
  class Meta:
    model = Profile
    exclude = ['user']



class NewProjectForm(forms.ModelForm):
  class Meta:
    model = Neighbourhood

    fields =['title', 'description', 'location','county','neighbourhood_image','neighbourhood_admin','health_department','police_department']


class NewBusinessForm(forms.ModelForm):
  class Meta:
    model = Business

    fields =['name','description','business_email','business_type']
    

class NewPostForm(forms.ModelForm):
  class Meta:
    model = Post

    fields =['title','image','content','neighbourhood']
