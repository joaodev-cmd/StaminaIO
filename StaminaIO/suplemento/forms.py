from django import forms
from .models import Suplemento 

class SuplementoForm(forms.ModelForm):
    class Meta:
        model = Suplemento
        fields = '__all__'