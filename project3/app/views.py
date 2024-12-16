from django.shortcuts import render,redirect

# Create your views here.
list=[]
adm_username='admin'
adm_password='admin@123'

def index(request):
    if request.method=='POST':
        name=request.POST['name']
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        # list.append([name,username,password,email])
        list.append({'name':name,'username':username,'password':password,'email':email})
    

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
def admlogin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        if username==adm_username and password==adm_password:
            print('login')
            return redirect(admhome)
        
        else:
             print("Error")
    return render(request,'admlogin.html')
def admhome(request):
       return render(request,'admhome.html',{'users':list}) 
   

        





