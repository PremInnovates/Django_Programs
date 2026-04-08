from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm

# Create + Display
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee/list.html', {'employees': employees})

# Add Employee
def add_employee(request):
    form = EmployeeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list')
    return render(request, 'employee/form.html', {'form': form})

# Update
def update_employee(request, id):
    emp = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST or None, instance=emp)
    if form.is_valid():
        form.save()
        return redirect('list')
    return render(request, 'employee/form.html', {'form': form})

# Delete
def delete_employee(request, id):
    emp = Employee.objects.get(id=id)
    emp.delete()
    return redirect('list')