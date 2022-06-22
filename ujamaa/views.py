from django.shortcuts import render,redirect,get_object_or_404
# from django.http import HttpResponse
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm,NewProjectForm,NewBusinessForm,NewPostForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile, Neighbourhood, Business





# posts =[
#   {
#     'Neighbourhood': 'Brownsville',
#     'title': 'Neighbourhood',
#     'content':'Brave Neighbourhood',
#     'date_posted':"August 12 2022"
#   },

#    {
#     'Neighbourhood': 'Brownsville',
#     'title': 'Neighbourhood',
#     'content':'Brave Neighbourhood',
#     'date_posted':"August 12 2022"
#   }
# ]








# Landingg Page
def home(request):
  return render(request, 'users/home.html' )



# Projects Page
@login_required
def projects(request):
  neighbourhood = Neighbourhood.objects.all()

  return render(request, 'users/projects.html', {'neighbourhood': neighbourhood})

  
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

# ________________________________________________________________

def join_hood(request,id):
    neighbourhood = get_object_or_404(Neighbourhood, id=id)
    request.user.profile.neighbourhood = neighbourhood
    request.user.profile.save()
    return render(request,'users/specific.html', {'id':id, 'neighbourhood':neighbourhood})






# _______________________________________________________________


@login_required(login_url='/users/login')
def new_post(request):
  current_user = request.user
  if request.method == 'POST':
    form =NewProjectForm(request.POST, request.FILES)
    if form.is_valid():
      print('post')
      project = form.save(commit=False)
      
      project.user = current_user
      project.save()
    return redirect('nb-project')
  
  else:
    form = NewProjectForm()

  return render(request, 'users/newpost.html', {'form':form})


# business_post

@login_required(login_url='/users/login')
def biz_post(request):
  current_user = request.user
  if request.method == 'POST':
    form =NewBusinessForm(request.POST, request.FILES)
    if form.is_valid():
      print('post')
      business = form.save(commit=False)
      
      business.user = current_user
      business.save()
    return redirect('jb')
  
  else:
    form = NewBusinessForm()

  return render(request, 'users/businesspost.html', {'form':form})




  # Add_post
def add_post(request):
  current_user = request.user
  if request.method == 'POST':
    form =NewPostForm(request.POST, request.FILES)
    if form.is_valid():
      print('post')
      project = form.save(commit=False)
      
      project.user = current_user
      project.save()
    return redirect('jb')
  
  else:
    form = NewPostForm()

  return render(request, 'users/post.html', {'form':form})