from django import forms
from .models import City

class FormCity(forms.ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs = {'placeholder': 'City Name'})

        }