from django.core import validators
from django import forms

class StudentRegistration(forms.Form):
    name = forms.CharField(validators=[validators.MinLengthValidator(5)])
    email = forms.EmailField(validators=[validators.MaxLengthValidator(40)])
