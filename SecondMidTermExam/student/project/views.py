from django.shortcuts import render,redirect,get_object_or_404
from .models import student
from .forms import StudentForm

def home(request):
    if request.method=='POST':
        student_id=request.POST.get('student_id')
        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        joined_date=request.POST.get('joined_date')

        student.object.create(
            student_id=student_id,
            name=name,
            email=email,
            age=age,
            joined_date=joined_date
        )
        return redirect('student_list')
    return render(request,'home_page.html')
# Create your views here.

def student_list(request):
    students=student.object.all()
    return render(request,'student_list.html',{'students':students})