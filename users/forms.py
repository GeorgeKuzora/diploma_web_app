from django import forms


class UserAuthForm(forms.Form):
    user_email = forms.EmailField(
        widget=forms.EmailInput,
        initial="example@email.com",
        help_text="Enter your email",
    )
    user_password = forms.CharField(
        widget=forms.PasswordInput,
        initial="*****",
        help_text="Enter your password"
    )
