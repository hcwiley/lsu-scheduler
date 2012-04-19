from django.db import models
#from django.core.exceptions import ValidationError
#from django.contrib.auth.models import User
#from django.dispatch import receiver 
#from django.db.models.signals import post_save, pre_save
#from django.utils.encoding import smart_str
#from django.contrib.sites.models import Site
from apps.course.models import *
from apps.college.models import *

class Student(models.Model):
    name = models.CharField(max_length=144, help_text='John Doe', unique=True)
    id_number = models.IntegerField(default=0, help_text='89#######', unique=True)
    major = models.ForeignKey(Major)
    minor = models.ForeignKey(Minor, related_name='Minor', null=True, blank=True, default='')
    coursesWanted = models.ManyToManyField(Course, related_name='Wanted_Course', null=True, blank=True, default=None)
    coursesRegistered = models.ManyToManyField(Course, related_name='Registered_Course', null=True, blank=True, default=None)
    coursesNeeded = models.ManyToManyField(Course, related_name='Needed_Course', null=True, blank=True, default=None)
    coursesTaken = models.ManyToManyField(Course, related_name='Taken_Course', null=True, blank=True, default=None)
    
    def __unicode__(self):
        return self.name
        
    class Meta:
        ordering = ['name']
        
    def save(self, *args, **kwargs):
        super(Student, self).save(*args, **kwargs)
        if self.coursesNeeded.count() < 1:
            if self.coursesNeeded:
                self.coursesNeeded += self.major.department.courses.all()
            else:
                self.coursesNeeded = self.major.department.courses.all()
            self.getCoursesNeeded()

        
    @models.permalink
    def get_absolute_url(self):
        return ('apps.student.views.student', [str(self.id)])
    
    ''' TODO Christian optomize this.
    this should parse the major courses required and check to see if it is in the student needed if not in taken.
    get rid of duplicates in title and number.
    if its in taken, make sure its not in needed.
    '''
    def getCoursesNeeded(self):
        for course in self.major.coursesRequired.all():
            if course not in self.coursesNeeded.all():
                self.coursesNeeded.add(course)
        for course in self.coursesNeeded.all():
            if self.coursesNeeded.filter(number=course.number, title=course.title).count() > 1:
                self.coursesNeeded.remove(course)
        for course in self.coursesTaken.all():
            self.coursesNeeded.remove(course)
        return self.coursesNeeded