from unicodedata import name
from django.core import validators
from django import forms
from .models import Record
class Contactus(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['name', 'phone', 'email', 'message']
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'phone' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.EmailInput(attrs={'class':'form-control'}),
            'message' : forms.TextInput(attrs={'class':'form-control', 'row':'3'}),
        }
