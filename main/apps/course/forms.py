from django import forms
from apps.course.models import Course

class CoursesWanted(forms.ModelForm):
    courses = forms.ModelMultipleChoiceField(queryset=Course.objects.none(), required=False)