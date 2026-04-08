from django.shortcuts import render, redirect, get_object_or_404
from .models import student  
from .forms import StudentForm

def home(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        joined_date = request.POST.get('joined_date')

        student.objects.create(
            student_id=student_id,
            name=name,
            email=email,
            age=age,
            joined_date=joined_date
        )
        return redirect('student_list')
    
    return render(request, 'home_page.html')

def student_list(request):
    students = student.objects.all() 
    return render(request, 'student_list.html', {'students': students}) 

def update_student(request, id):
    s = get_object_or_404(student, id=id)  
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=s)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=s)
    return render(request, 'update_student.html', {'form': form})


def delete_student(request, id):
    s = get_object_or_404(student, id=id)  
    if request.method == 'POST':
        s.delete()
        return redirect('student_list')