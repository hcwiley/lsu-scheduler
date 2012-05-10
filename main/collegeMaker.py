from apps.college.models import College
import os
#from django.template.defaultfilters import slugify
def main():
    file = open('./apps/college/colleges.data', 'r')
    for college in file.readlines():
        college = college.strip()
        abbr = college.split(':')[0]
        name = college.split(':')[1]
        print 'abbr: %s' % abbr
        print 'name: %s' % name
        col = College.objects.get_or_create(abbr=abbr)
        if col[1]:
            col = col[0]
            col.name = name
            col.save()
