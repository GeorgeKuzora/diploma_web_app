from django import forms


class JobForm(forms.Form):
    skill = forms.CharField()
