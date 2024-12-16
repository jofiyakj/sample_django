from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('login',views.login),
    path('home',views.home),
    path('admlogin',views.admlogin),
    path('admhome',views.admhome)

]