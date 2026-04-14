from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
# Create your views here.

def register(request):
    return render(request,'registration.html')

def savereg(request):
    username=request.POST['username']
    password=request.POST['password']
    email=request.POST['email']
    user=User.objects.create(username=username,password=password,email=email)
    user.save()
    return render(request,'login.html')

def logincheck(request):
    username=request.POST['username']
    password=request.POST['password']
    user=User.objects.filter(username=username)
    if user:
        return render(request,'home.html')
    return render(request,'login.html')

def login(request):
    return render(request,'login.html')


def logout(request):
    return redirect('/login')