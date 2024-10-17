# forms.py
from django import forms
from ..models import SessionRating

class SessionRatingForm(forms.ModelForm):
    class Meta:
        model = SessionRating
        fields = ['rating', 'message']
        widgets = {
            'rating': forms.NumberInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
    
    def __init__(self, *args, **kwargs):
        super(SessionRatingForm, self).__init__(*args, **kwargs)
        self.fields['rating'].label = "تقييم"  # Arabic for "Rating"
        self.fields['message'].label = "رسالة"  # Arabic for "Message"
