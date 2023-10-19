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


class UserSettingsForm(forms.Form):
    username = forms.CharField(help_text="User's username")
    firstname = forms.CharField(help_text="User's firstname")
    lastname = forms.CharField(help_text="User's lastname")
    parent_name = forms.CharField(help_text="User's parentname")
    email = forms.EmailField(help_text="User's email")
    birthdate = forms.DateField(help_text="User's birthdate")
    skills = forms.TextInput()
    phone = forms.CharField(help_text="User's phone")
    address = forms.CharField(help_text="User's address")
