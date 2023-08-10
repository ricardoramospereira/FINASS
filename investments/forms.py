from django.forms import ModelForm
from .models import Investment
from django import forms

class InvestmentForm(ModelForm):
    class Meta:
        model = Investment
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'required': 'required'}),
            'value': forms.TextInput(attrs={'required': 'required'}),
            # Adicione outros campos aqui, se necessário
        }