from django import forms
from .models import *
from captcha import fields


class StudentForm(forms.ModelForm):
    captcha = fields.CaptchaField()

    class Meta:
        model = Student
        fields = '__all__'

