from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from ..models import Student

# Signup form
class SignupForm(forms.ModelForm):
    password = forms.CharField(
        label=_("كلمة المرور"), 
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password_confirm = forms.CharField(
        label=_("تأكيد كلمة المرور"), 
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Student
        fields = ['fullName', 'phone', 'email']
        labels = {
            'fullName': _('الاسم الكامل'),
            'phone': _('رقم الهاتف'),
            'email': _('البريد الإلكتروني'),
        }
        widgets = {
            'fullName': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password != password_confirm:
            raise forms.ValidationError(_("كلمات المرور غير متطابقة"))
        return cleaned_data

    def save(self, commit=True):
        user = super(SignupForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

# Login form
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label=_("رقم الهاتف"),
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label=_("كلمة المرور"),
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
