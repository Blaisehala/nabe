from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='home'),
    path('projects/', views.projects, name='nb-project'),
    path('about/', views.about, name='nb-about'),

]

