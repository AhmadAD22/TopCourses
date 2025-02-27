from django import forms
from ..models import Session

class SessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = ['number', 'date']
        widgets = {
            'number': forms.NumberInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),

        }
        labels = {
            'number': 'Session Number',
            'date': 'Date',
            'active': 'Active',
        }
