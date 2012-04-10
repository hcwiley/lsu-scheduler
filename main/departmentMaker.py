from apps.college.models import Department
from apps.course.models import Course
from glob import glob
import os
#from django.template.defaultfilters import slugify

#print os.getcwd()
#os.chdir('./apps/college/departments/')
#print os.getcwd()
print Course.objects.all()
print Department.objects.all()

def main():
    departments = glob('*.txt')
    for department in departments:
        department = department.rstrip('.txt').capitalize()
        print department
        dept = Department.objects.get_or_create(name=department)
        if dept[1]:
            dept[0].save()
