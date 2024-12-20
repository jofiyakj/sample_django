from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User,auth

# Create your views here.
adm_username='admin'
adm_password='admin@123'
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        print(username,password)
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect(home)
        else:
            return redirect(login)
    return render(request,'user/login.html')
    
def register(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        data=User.objects.create_user(first_name=name,email=email,username=username,password=password)
        data.save()
        return redirect(login)
    return render(request,'user/register.html')
           

def home(request):
    if '_auth_user_id' in request.session:
        user=User.objects.get(pk=request.session['_auth_user_id'])
        return render(request,'user/home.html',{'user':user})
    else:
        return redirect(login)

def  logout(request):
    if 'auth_user_id' in request.session:
        # del request.session['user']
        return redirect(login)
    else:
        return redirect(login)




def adminlogin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        print(username,password)
        if username==adm_username and  password==adm_password:
               print('login')
               return redirect(adminhome)
        else:
                print("Error")
    return render(request,'admin/adminlogin.html')
def adminhome(request):
         user=User.objects.filter(username__startswith='a') 
         print(user)
         return render(request,'admin/adminhome.html',{'user':user}) 