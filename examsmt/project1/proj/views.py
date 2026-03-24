from django.shortcuts import render,redirect
from .models import student
# Create your views here.
def home(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        age=request.POST.get('age')
        rollno=request.POST.get('rollno')

        student.objects.create(
            name=name,
            age=age,
            rollno=rollno
        )
    return render(request,'home.html')

def student_list(request):
    students=student.objects.all()
    return render(request,'student_list.html',{'students':students})


def update_student(request,id):
    s=student.objects.get(id=id)
    if request.method=='POST':
        s.name=request.POST.get('name')
        s.age=request.POST.get('age')
        s.rollno=request.POST.get('rollno')
        s.save()
        return redirect('student_list')
    else:
        return render(request,'update.html',{'s':s})

def delete_student(request,id):
    s=student.objects.get(id=id)
    s.delete()
    return redirect('student_list')
