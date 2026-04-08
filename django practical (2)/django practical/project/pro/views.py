from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Student

def home(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        joined_date = request.POST.get('joined_date')

        # Save the new student
        Student.objects.create(
            student_id=student_id,
            name=name,
            email=email,
            age=age,
            joined_date=joined_date
        )

        return redirect('home')  # Redirect to home or success page

    return render(request, 'home_page.html')




def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})


    