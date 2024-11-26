from django.urls import path
from . import views
urlpatterns = [
    path('fun/<int:data>',views.fun)

]