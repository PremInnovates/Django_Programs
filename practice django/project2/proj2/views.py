from django.shortcuts import render
from .models import project2
from django.http import HttpResponse
def contactus(request):
    if request.method=="POST":
        name=request.POST.get('name')
        age=request.POST.get('age')
        marks=request.POST.get('marks')
        project2.objects.create(name=name,age=age,marks=marks)
        return HttpResponse("""<script>
                            alert("Data Saved Successfully!!!")
                            window.location.href='/contactus/'
                            </script>""")
    return render(request,'contactus.html')
# Create your views here.
