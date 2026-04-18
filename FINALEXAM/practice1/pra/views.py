from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Employee
from django.http import HttpResponse
from .forms import EmployeeForm


# Create your views here.
def register(request):
    return render(request,'registrationpage.html')

def savereg(request):
    username=request.POST['username']
    password=request.POST['password']
    email=request.POST['email']
    user=User.objects.create(username=username,password=password,email=email)
    user.save()
    return render(request,'login.html')

def logincheck(request):
    username=request.POST['usernam  e']
    password=request.POST['password']
    user=User.objects.filter(username=username)
    if user:
        return render(request,'home.html')
    return render(request,'login.html')

def login(request):
    return render(request,'login.html')

def logout(request):
    return render(request,'login.html')

def home(request):
    employees=Employee.objects.all()
    return render(request,'home.html',{'Employees':employees})

def add(request):
    if request.method=="POST":
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=EmployeeForm()
    return render(request,'add.html',{'form':form})

def update(request,id):
    emp=Employee.objects.get(id=id)
    if request.method=="POST":
        form=EmployeeForm(request.POST,instance=emp)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print(form.errors)
    else:
        form=EmployeeForm(instance=emp)
    return render(request,'update.html',{'form':form})

def delete(request,id):
    emp=Employee.objects.get(id=id)
    emp.delete()
    return redirect('home')