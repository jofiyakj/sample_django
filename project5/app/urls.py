from django.urls import path
from . import views

urlpatterns=[
    path('',views.register),
    path('login',views.login),
    path('home',views.home),
    path('logout',views.logout),
    path('adminhome',views.adminhome),
    path('adminlogin',views.adminlogin),


   
]