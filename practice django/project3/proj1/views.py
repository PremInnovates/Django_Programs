from django.shortcuts import render
from . models import Student
from django.http import HttpResponse
# Create your views here.
def Add_Student(request):
    if request.method=="POST":
        Student_Name=request.POST.get("Student_Name")
        Student_ID=request.POST.get("Student_ID")
        Student_Percentage=request.POST.get("Student_Percentage")
        Student.objects.create(Student_Name=Student_Name,Student_ID=Student_ID,Student_Percentage=Student_Percentage)
        return HttpResponse("""
        <script>
        alert("Student Added Sucessfully!!")
        window.location.href="/Add_Student/"
        </script>""")
    
    return render(request,"Add_Student.html")

def show_student(request):
    students=Student.objects.all()
    return render(request,"show_student.html",{"Student":students})