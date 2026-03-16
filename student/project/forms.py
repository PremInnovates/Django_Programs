from django import forms
from .models import student

class StudentForm(forms.ModelForm):
    class Meta:
        model = student
        fields = ['student_id', 'name', 'email', 'age'] 
        # widgets = {
        #     'student_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Student ID'}),
        #     'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Full Name'}),
        #     'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}),
        #     'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Age'}),
        # }