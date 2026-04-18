from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Person
from .forms import PersonForm
# Create your views here.

def register(request):
    return render(request,'register.html')

def savereg(request):
    if request.method=='POST':
        username=request.POST['username']
        passowrd=request.POST['password']
        email=request.POST['email']
        user=User.objects.create(username=username,password=password,email=email)
        user.save()
        return render(request,'login.html')
    return render(request,'register.html')

def logincheck(request):
    username=request.POST['username']
    password=request.POST['password']
    user=User.objects.filter(username=username)
    if user:
        return render(request,'home.html')
    else:
        return render(request,'login.html')

def home(request):
    products=Product.objects.all()
    return render(request,'home.html',{'products':products})



def login(request):
    return render(request,'login.html')

def logout(request):
    return render(request,'login.html')