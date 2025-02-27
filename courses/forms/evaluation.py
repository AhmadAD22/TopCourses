from django import forms
from ..models import QuestionTemplate

class QuestionTemplateForm(forms.ModelForm):
    class Meta:
        model = QuestionTemplate
        fields = ['type', 'session', 'question']
        labels = {
            'type': 'النوع',
            'session': 'الجلسة',
            'question': 'السؤال',
        }
        widgets = {
            'type': forms.Select(attrs={'class': 'form-control'}),
            'session': forms.Select(attrs={'class': 'form-control'}),
            'question': forms.TextInput(attrs={'class': 'form-control'}),
        }
