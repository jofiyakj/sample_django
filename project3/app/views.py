from django.shortcuts import render,redirect

# Create your views here.
list=[]

def index(request):
    if request.method=='POST':
        name=request.POST['name']
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        list.append([name,username,password,email])

        print(list)
    return render(request,'index.html')  
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        for i in list:
            if username==i[1] and password==i[2]:
                print(i[0])
            return redirect(home)
    return render(request,'login.html')   
def home(request):
       return render(request,'home.html')   
        





