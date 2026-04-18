from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import StudentForm
from .models import Student
from django.http import HttpResponse
# Create your views here.


def register(request):
    return render(request,'register.html')

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
        return redirect('home')
    return render(request,'login.html')

def login(request):
    return render(request,'login.html')

def logout(request):
    return redirect('login.html')


def home(request):
    students=Student.objects.all()
    return render(request,'home.html',{'students':students})


def add(request):
    if request.method== "POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=StudentForm()
    return render(request,'add.html',{'form':form})


def update(request,rollno):
    student=Student.objects.get(rollno=rollno)
    form=StudentForm(request.POST,instance=student)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request,'update.html',{'form':form})

def delete(request,rollno):
    Student.objects.filter(rollno=rollno).delete()
    return redirect('home')