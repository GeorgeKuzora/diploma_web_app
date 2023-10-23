from django import forms

from .models import Job


class JobForm(forms.Form):
    skills = forms.CharField(max_length=200, required=False)
    sallary = forms.IntegerField(required=False)
    company = forms.CharField(max_length=100, required=False)
    pub_date = forms.DateField(required=False, widget=forms.DateInput())
    country = forms.CharField(max_length=50, required=False)
    required_experience = forms.ChoiceField(choices=Job.Experience.choices, required=False)

    class Meta:
        fields = '__all__'
