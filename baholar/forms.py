from django import forms
from .models import Subject,Student,Grade


class AddSubjectFrom(forms.ModelForm):
    class Meta:
        model=Subject
        fields="__all__"


class AddStudentFrom(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"

class AddGradeFrom(forms.ModelForm):
    class Meta:
        model=Grade
        fields="__all__"