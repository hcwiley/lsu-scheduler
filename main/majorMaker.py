from apps.college.models import Major, College, Department
from glob import glob
import os
import re
#from django.template.defaultfilters import slugify
def main():
    colleges = glob('./apps/college/colleges/*.txt')
    for college in colleges:
        college = college.lstrip('./apps/college/colleges/')
        college = college.rstrip('.txt')
        college = college.strip()
        print college
        file = open('./apps/college/colleges/%s.txt' % college, 'r')
        for major in file.readlines():
            major = major.strip()
            abbr = major.split(':')[0]
            abbr = re.sub(' +',' ',abbr)
            name = major.split(':')[1]
            name = re.sub(' +',' ',name)
            maj = Major.objects.get_or_create(abbr=abbr, name=name)
            if maj[1]:
                maj[0].save()
            maj = maj[0]
            if len(abbr.split(' ')) > 0:
                abbr = abbr.split(' ')[0]
            try:
                col = College.objects.get(abbr=college)
                maj.college = col
                print 'college: %s' % col.name
                maj.save()
            except:
                print 'no matching college for: %s' % college
            try:
                dept = Department.objects.get(abbr=abbr)
                maj.department = dept
                print 'department: %s' % dept.name
                maj.save()
            except:
                try:
                    dept = Department.objects.get(abbr=college)
                    maj.department = dept
                    print 'department: %s' % dept.name
                    maj.save()
                except:
                    print 'no matching department for: %s' % abbr