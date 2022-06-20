from django.shortcuts import render,redirect
# from django.http import HttpResponse
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile, Neighbourhood, Business





posts =[
  {
    'Neighbourhood': 'Brownsville',
    'title': 'Neighbourhood',
    'content':'Brave Neighbourhood',
    'date_posted':"August 12 2022"
  },

   {
    'Neighbourhood': 'Brownsville',
    'title': 'Neighbourhood',
    'content':'Brave Neighbourhood',
    'date_posted':"August 12 2022"
  }
]








# Landingg Page
def home(request):
  return render(request, 'users/home.html' )



# Projects Page
def projects(request):
  context ={

    'posts': posts
  }
  return render(request, 'users/projects.html',context)

  
# About Page 
def about(request):
  return render(request, 'users/about.html', {'title': 'About'})


# register 
def register(request):
  if request.method == 'POST':
    form = UserRegisterForm(request.POST)
    if form.is_valid():
      form.save()
      username=form.cleaned_data.get('username')
      messages.success(request, f'Account created for {username}.You can now Login')
      return redirect ('login')
      
  else:
    form = UserRegisterForm()
  return render(request, 'users/register.html', {'form': form})
 

# profile
@login_required
def profile(request):
  if request.method == 'POST':
    u_form = UserUpdateForm(request.POST, instance=request.user)
    p_form = ProfileUpdateForm(request.POST,request.FILES, instance=request.user.profile)
    current_user=request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    
    if u_form.is_valid() and p_form.is_valid():
       u_form.save()
       p_form.save()
       messages.success(request, f'Account updated succefully.')
       return redirect('profile')

  else:
     u_form = UserUpdateForm(instance=request.user)
     p_form = ProfileUpdateForm(instance=request.user.profile)


  context = {
    'u_form': u_form,
    'p_form': p_form,
    
  }
  
  return render(request, 'users/profile.html', context)


