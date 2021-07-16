from django import forms
from .models import ClassLevel, Student, Teacher
from captcha import fields


class ClassLevelForm(forms.ModelForm):
    class Meta:
        model = ClassLevel
        fields = '__all__'


class StudentForm(forms.ModelForm):
    class_level = forms.ModelChoiceField(
        queryset=ClassLevel.objects.all(),
        to_field_name="level",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    captcha = fields.CaptchaField()

    class Meta:
        model = Student
        fields = ('name', 'email', 'class_level', 'roll')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'roll': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Your roll number'}),

        }

