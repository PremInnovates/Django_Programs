from django.shortcuts import render,redirect,get_object_or_404
from .models import men
from .forms import menForm
# Create your views here.

def home(request):
    if request.method=='POST':
        name=request.POST.get('name')
        age=request.POST.get('age')

        men.objects.create(
            name=name,
            age=age
        )
        return redirect('men_list')
    return render(request,'home_page.html')

def men_list(request):
    mens=men.objects.all()
    return render(request,'men_list.html',{'mens':mens})

def update_men(request,id):
    s=get_object_or_404(men,id=id)
    if request.method=='POST':
        form=menForm(request.POST,instance=s)
        if form.is_valid():
            form.save()
        return redirect('men_list')
    else:
        form=menForm(instance=s)
    return render(request,'update_men.html',{'form':form})
    
def delete_men(request,id):
    s=get_object_or_404(men,id=id)
    if request.method=="POST":
        s.delete()
    return redirect('men_list')