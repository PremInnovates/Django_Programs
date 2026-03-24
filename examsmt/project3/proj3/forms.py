from django import forms
from .models import men

class menForm(forms.ModelForm):
    class Meta:
        model=men
        fields=['name','age']