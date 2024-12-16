from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def fun(request,data):
    if data%3==0:
        return HttpResponse("is divisible by 3")
    else:
        return HttpResponse("is not divisible by 3")
    return HttpResponse(data)
