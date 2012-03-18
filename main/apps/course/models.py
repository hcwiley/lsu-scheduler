from django.db import models
#from django.core.exceptions import ValidationError
#from django.contrib.auth.models import User
from django.contrib import admin
#from django.dispatch import receiver 
#from django.db.models.signals import post_save, pre_save
#from django.utils.encoding import smart_str
#from django.contrib.sites.models import Site
from datetime import time

class Course(models.Model):
    WEEKDAYS = (('M', 'Monday'), ('T', 'Tuesday'), ('W', 'Wednesday'), ('TH', 'Thursday'), ('F', 'Friday'))
    title = models.CharField(max_length=30)
    number = models.IntegerField()
    section_number = models.IntegerField()
    start_time = models.TimeField(default=time.now(), blank=True, null=True)
    end_time = models.TimeField(default=time.now(), blank=True, null=True)
    time_tba = models.BooleanField()
    days = models.CharField(choices=WEEKDAYS, max_length=2)
    building = models.CharField(max_length=50, default='', blank=True, null=True)
    room = models.IntegerField(default=42, blank=True, null=True)
    instructor = models.CharField(max_length=100, default='', blank=True, null=True)
    available_seats = models.IntegerField(default=42, blank=True, null=True)
    number_enrolled = models.IntegerField(default=0, blank=True, null=True)
    special_enrollment = models.CharField(max_length=100, default='', blank=True, null=True)
    
    def save(self, *args, **kwargs):
        super(Course, self).save(*args, **kwargs)
        
admin.site.register(Course)