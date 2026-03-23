from django import forms
from .models import student

class StudentForm(forms.ModelForm):
    class Meta:
        model=student
        fields=['student_id','name','email','age']
        