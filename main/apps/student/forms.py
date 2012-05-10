from django import forms
from apps.student.models import Student

class StudentForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'John Doe', 'required' : 'required'}), required=True)
    class Meta:
        model = Student