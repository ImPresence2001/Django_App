from django import forms
from .models import UserProfile

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password']
        widgets = {'password': forms.PasswordInput}

class LoginForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['email', 'password']
        widgets = {'password': forms.PasswordInput}