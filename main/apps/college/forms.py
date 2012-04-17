from django import forms
from apps.college.models import *

class MajorForm(forms.ModelForm):
    class Meta:
        model = Major

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        
class CollegeManagerForm(forms.Form):
    pk = forms.IntegerField()
    name = forms.CharField()
    abbr = forms.CharField()
    majors = forms.ModelMultipleChoiceField(queryset=Major.objects.all(), required=False)
    departments = forms.ModelMultipleChoiceField(queryset=Department.objects.all(), required=False)
    class Meta:
        model = College