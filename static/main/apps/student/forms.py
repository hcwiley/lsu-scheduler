from django import forms
from apps.student.models import Student

class StudentForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'John Doe', 'required' : 'required'}), required=True)
    id_number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': '89#######', 'required' : 'required'}), required=True)
    class Meta:
        model = Student