from django import forms
from .models import Process, Parts

class ProcessForm(forms.ModelForm):
    class Meta:
        model = Process
        fields = ['number','judicialClass','topic','judge','parts','category']
        widgets = {
            'number': forms.TextInput(attrs={'class': 'form-control'}),
            'judicialClass': forms.TextInput(attrs={'class': 'form-control'}),
            'topic': forms.TextInput(attrs={'class': 'form-control'}),
            'judge': forms.TextInput(attrs={'class': 'form-control'}),
            'parts': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'category': forms.TextInput(attrs={'class': 'form-control'}),
        }

class PartsForm(forms.ModelForm):
    class Meta:
        model = Parts
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }