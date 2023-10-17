from django import forms


class UserAuthForm(forms.Form):
    username = forms.CharField(
        help_text="Enter your username",
    )
    password = forms.CharField(
        widget=forms.PasswordInput,
        initial="*****",
        help_text="Enter your password"
    )
