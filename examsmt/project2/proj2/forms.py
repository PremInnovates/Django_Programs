from .models import person
from django import forms

class personForm(forms.ModelForm):
    class Meta:
        model=person
        fields=['name','age','salary']
        