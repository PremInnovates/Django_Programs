from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from . models import Product
from .forms import ProductForm
# Create your views here.

def register(request):
    return render(request,'register.html')
    
def savereg(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        user=User.objects.create(username=username,password=password,email=email)
        user.save()
        return render(request,'login.html')
    return render(request,'register.html')

def login(request):
            return render(request,'login.html')

def logout(request):
    return render(request,'login.html')

def logincheck(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=User.objects.filter(username=username)
        if user:
            return render(request,'home.html')
        return render(request,'login.html')

def home(request):
    products=Product.objects.all()
    return render(request,'home.html',{'products':products})


def add(request):
    if request.method=='POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'add.html')


def update(request,id):
    product=Product.objects.get(id=id)
    if request.method=='POST':
        form=ProductForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
        return redirect('home')
    else:
        form=ProductForm(instance=product)
    return render(request,'update.html',{'form':form})

def delete(request,id):
    Product.objects.get(id=id).delete()
    return redirect('home')