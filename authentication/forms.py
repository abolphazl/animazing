from django import forms
from django.core.exceptions import ValidationError

class LoginForm(forms.Form):
    username = forms.CharField(label=False, max_length=64, widget=forms.TextInput(attrs={'class': 'input', 'id': 'username'}))
    password = forms.CharField(label=False, max_length=64, widget=forms.PasswordInput(attrs={'class': 'input', 'id': 'password'}))

class RegisterForm(forms.Form):
    username = forms.CharField(label=False, max_length=64, widget=forms.TextInput(attrs={'class': 'input', 'id': 'username'}))
    email = forms.EmailField(label=False, max_length=64, widget=forms.TextInput(attrs={'class': 'input', 'id': 'email'}))
    password = forms.CharField(label=False, max_length=64, widget=forms.PasswordInput(attrs={'class': 'input', 'id': 'password'}))
    confirm_password = forms.CharField(label=False, max_length=64, widget=forms.PasswordInput(attrs={'class': 'input', 'id': 'confirm-password'}))

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise ValidationError("Passwords don't match")
        
        return confirm_password