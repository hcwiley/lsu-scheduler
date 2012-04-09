from django.db import models
#from django.core.exceptions import ValidationError
#from django.contrib.auth.models import User
from django.contrib import admin
#from django.dispatch import receiver 
#from django.db.models.signals import post_save, pre_save
#from django.utils.encoding import smart_str
#from django.contrib.sites.models import Site
from apps.course.models import *

class Major(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    coursesRequired = models.ManyToManyField(Course, related_name='Required_Course');
    def __unicode__(self):
        return self.name
    
class Minor(Major):
    pass

class Student(models.Model):
    name = models.CharField(max_length=144)
    id_number = models.IntegerField(default=0)
    major = models.ForeignKey(Major)
    minor = models.ForeignKey(Minor, related_name='Minor')
    coursesWanted = models.ManyToManyField(Course, related_name='Wanted_Course');
    coursesRegistered = models.ManyToManyField(Course, related_name='Registered_Course');
    coursesNeeded = models.ManyToManyField(Course, related_name='Needed_Course');
    
    def __unicode__(self):
        return self.name
    
admin.site.register(Student)
admin.site.register(Major)
admin.site.register(Minor)