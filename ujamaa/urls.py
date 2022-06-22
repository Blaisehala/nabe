from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='ujamaa-home'),
    path('projects/', views.projects, name='nb-project'),
    path('about/', views.about, name='nb-about'),

    path ('jb/<int:id>',views.join_hood, name='jb'),

    path ('newpost/',views.new_post, name='newpost'),
    path ('businesspost/',views.biz_post, name='businesspost'),
    path ('post/',views.add_post, name='post'),
   
]

