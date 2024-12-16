from django.shortcuts import render,redirect
from .models import *

# Create your views here.
ad_us='admin'
ad_psw='admin@123'
def adminlogin(request):
    if request.method=='POST':
        adm_us=request.POST['adminusername']
        adm_psw=request.POST['adminpassword']
        if ad_us==adm_us and ad_psw==adm_psw:
            return redirect(adminhome)
    return render(request,'admin/adminlogin.html')
def adminhome(request):
    return render(request,'admin/adminhome.html')

def register(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        username=request.POST['username']
        password=request.POST['password']
        data=user.objects.create(name=name,email=email,phone=phone,username=username,password=password)
        data.save()
    return render(request,'user/register.html')
        

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        print(username,password)
        data=user.objects.all()
        for i in data:
            if i.username==username and i.password==password: 
                print('loggedin')
                request.session['userlog']=i.username
                return redirect(home)
            
            
    return render(request,'user/login.html')

def home(request):
    if 'userlog' in request.session:
        data=user.objects.get(username=request.session['userlog'])
        return render(request,'user/home.html',{'data':data})
    else:
        return redirect(login)

def logout(request):
    if 'userlog' in request.session:
        del request.session['userlog']
        return redirect(login)
    else:
        return redirect(login)
       