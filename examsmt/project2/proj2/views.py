from django.shortcuts import render,redirect,get_object_or_404
from django.forms import personModelForm
from .models import person 

def home(request):
    if request.method=='POST':
        name=request.POST.get('name')
        age=request.POST.get('age')
        salary=request.POST.get('salary')
        person.objects.create(
            name=name,
            age=age,
            salary=salary
        )
        return render(request,'home.html')

def person_list(request):
    persons=person.objects.all()
    return render(request,'person_list.html',{'persons':persons})

def update_person(request,id):
    s=get_object_or_404(person,id=id)
    if request.method=='POST':
        form=personForm(request.POST,instance=s)
        if form.is_valid():
            form.save()
            return redirect('person_list')
    else:
        form=personForm(instance=s)
    return render(request,'update_person.html',{'form':form})

def delete_person(request,id):
    s=get_object_or_404(person,id=id)
    if request.method=='POST':
        s.delete()
        return redirect('person_list')

