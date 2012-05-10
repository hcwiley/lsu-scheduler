from django.db import models
#from django.core.exceptions import ValidationError
#from django.contrib.auth.models import User
from django.contrib import admin
#from django.dispatch import receiver 
#from django.db.models.signals import post_save, pre_save
#from django.utils.encoding import smart_str
#from django.contrib.sites.models import Site
from datetime import datetime
import time
from django.contrib.admin.sites import site

WEEKDAYS = (('M', 'Monday'), ('T', 'Tuesday'), ('W', 'Wednesday'), ('TH', 'Thursday'), ('F', 'Friday'))

class Date(models.Model):
    day = models.CharField(choices=WEEKDAYS, max_length=2, default='', unique=True)
    
    def __unicode__(self):
        return self.day    

class Course(models.Model):
    CLASS_TYPE = (('RES', 'Research'), ('LAB', 'Lab'), ('SEM', 'SEMINAR'), ('',''))
    
    title = models.CharField(max_length=30)
    number = models.IntegerField()
    section_number = models.IntegerField(default=1)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    credit_hours = models.IntegerField(default=3)
    time_tba = models.BooleanField(default=False)
    days = models.ManyToManyField(Date, default='')
    building = models.CharField(max_length=50, default='', blank=True, null=True)
    room = models.IntegerField(default=0, blank=True, null=True)
    instructor = models.CharField(max_length=100, default='', blank=True, null=True)
    available_seats = models.IntegerField(default=0, blank=True, null=True)
    number_enrolled = models.IntegerField(default=0, blank=True, null=True)
    special_enrollment = models.CharField(max_length=100, default='', blank=True, null=True)
    type = models.CharField(choices=CLASS_TYPE, max_length=3, default='', null=True, blank=True)
    pretty_days = models.CharField(max_length=10, blank=True, null=True, default='')
    pretty_start = models.CharField(max_length=10, blank=True, null=True, default='')
    pretty_end = models.CharField(max_length=10, blank=True, null=True, default='')
    abbr = models.CharField(max_length=4, blank=True, null=True, default='')
    
    class Meta:
        ordering = ['number']
    
    def __unicode__(self):
        return '%s: %s' % (self.number, self.title)
    
    @models.permalink
    def get_absolute_url(self):
        return ('apps.course.views.course', [str(self.id)])
    
    def get_pretty_days(self):
        days = ""
        for day in self.days.all():
            if day.day == 'H':
                day = "TH"
            days += '%s ' % (day)
        self.pretty_days = days
        return self.pretty_days
    
    def set_pretty_days(self):
        if self.pretty_days == '':
            days = ""
            for day in self.days.all():
                if day.day == 'H':
                    day = "TH"
                days += '%s ' % (day)
            self.pretty_days = days
            self.save()  
              
    def pretty_start_time(self):
        if self.start_time:
            self.pretty_start = self.start_time.strftime("%H:%M")
            return self.pretty_start
    
    def pretty_end_time(self):
        if self.end_time:
            self.pretty_end = self.end_time.strftime("%H:%M")
            return self.pretty_end
    
    def save(self, *args, **kwargs):
        days = ""
        for day in self.days.all():
            if day.day == 'H':
                day = "TH"
            days += '%s ' % (day)
        if self.days:
            self.pretty_days = days.rstrip(' ')
        if self.start_time:
            self.pretty_start = self.start_time.strftime("%H:%M")
        if self.end_time:
            self.pretty_end = self.end_time.strftime("%H:%M")
        super(Course, self).save(*args, **kwargs)
#
#def update_course(modeladmin, request, queryset):
#    queryset.update(status='p')
#update_course.short_description = "Get courses from regex file parsing"
class CourseAdmin(admin.ModelAdmin):
    class Meta:
        model = Course
#   actions = [update_course]
class Lab(models.Model):
    days = models.ManyToManyField(Date, default='', blank=True, null=True)
    building = models.CharField(max_length=50, default='', blank=True, null=True)
    room = models.IntegerField(default=42, blank=True, null=True)
    instructor = models.CharField(max_length=100, default='', blank=True, null=True)
    start_time = models.TimeField(default=datetime.time(datetime.now()), blank=True, null=True)
    end_time = models.TimeField(default=datetime.time(datetime.now()), blank=True, null=True)
    course = models.ForeignKey(Course)
    
    def __unicode__(self):
        return 'LAB %s' % (self.course)
    