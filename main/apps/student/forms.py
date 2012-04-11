from django import forms
from apps.student.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student