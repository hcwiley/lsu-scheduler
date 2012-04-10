from apps.college.models import Major, College
from glob import glob
import os
import re
#from django.template.defaultfilters import slugify
def main():
    colleges = glob('./apps/college/colleges/*.txt')
    for college in colleges:
        college = college.lstrip('./apps/college/colleges/')
        college = college.rstrip('.txt')
        print college
        file = open('./apps/college/colleges/%s.txt' % college, 'r')
        for major in file.readlines():
            major = major.strip()
            abbr = major.split(':')[0]
            abbr = re.sub(' +',' ',abbr)
            name = major.split(':')[1]
            name = re.sub(' +',' ',name)
            print 'abbr: %s' % abbr
            print 'name: %s' % name
            maj = Major.objects.get_or_create(abbr=abbr)
            if maj[1]:
                maj = maj[0]
                maj.name = name
                maj.save()
                maj.college = College.objects.get_or_create(abbr=college)[0]
