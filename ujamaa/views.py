from django.shortcuts import render
from django.http import HttpResponse


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








# Create your views here.
def home(request):
  context ={
    'posts':posts
  }

  return render(request, 'users/home.html' )


def projects(request):
  context ={

    'posts': posts
  }


  return render(request, 'users/projects.html',context)

  

def about(request):


  return render(request, 'users/about.html', {'title': 'About'})

