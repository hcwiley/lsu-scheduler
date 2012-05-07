from django import forms
from apps.course.models import Course

class CoursesWanted(forms.Form):
    courses = forms.ModelMultipleChoiceField(queryset=Course.objects.all(), required=False)