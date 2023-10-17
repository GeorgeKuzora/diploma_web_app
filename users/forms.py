from django import forms
from django.contrib.auth.forms import BaseUserCreationForm


class UserAuthForm(forms.Form):
    username = forms.CharField(
        help_text="Enter your username",
    )
    password = forms.CharField(
        widget=forms.PasswordInput,
        initial="*****",
        help_text="Enter your password"
    )


class UserRegisterForm(BaseUserCreationForm):
    email = forms.EmailField(help_text="Enter your email")
