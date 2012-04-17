from django import forms
from apps.college.models import *

class MajorForm(forms.ModelForm):
    class Meta:
        model = Major

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        
class CollegeForm(forms.ModelForm):
    majors = forms.MultipleChoiceField()
    departments = forms.MultipleChoiceField()
    class Meta:
        model = College