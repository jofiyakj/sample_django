from django.shortcuts import render,redirect
from .models import *
from .forms import *
# Create your views here.

def model_form_dis(request):
    data=model_form()
    if request.method=='POST':
        form=model_form(request.POST)
        if form.is_valid():
            form.save()
            print('successfull')
        else:
            print('error')
        return redirect(model_form_dis)
    return render(request,'teachers.html',{'data':data})
def upload(request):
    datas=UserUpload.objects.all()
    print(datas)
    if request.method=='POST':
         file=request.FILES['data']
         data=UserUpload.objects.create(document=file)
         data.save()
         return redirect(upload)
    return render(request,'upload.html',{'data':datas})




























