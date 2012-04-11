from django.db import models
#from django.core.exceptions import ValidationError
#from django.contrib.auth.models import User
#from django.dispatch import receiver 
#from django.db.models.signals import post_save, pre_save
#from django.utils.encoding import smart_str
#from django.contrib.sites.models import Site
from apps.course.models import *
from django.template.defaultfilters import slugify

class College(models.Model):
    name = models.CharField(max_length=200, unique=True)
    abbr = models.CharField(max_length=4, unique=True, null=True, blank=True, default='')
    slug = models.SlugField(null=True, blank=True, default='', editable=False)
    
    def __unicode__(self):
        return self.name
    
    
    class Meta:
        ordering = ['abbr']
    
    def save(self, *args, **kwargs):
        if self.slug == '':
            self.slug = slugify(self.name)
        super(College, self).save(*args, **kwargs)
        
    @models.permalink
    def get_absolute_url(self):
        return ('apps.college.views.college', [str(self.abbr)])

class Department(models.Model):
    name = models.CharField(max_length=200, unique=True)
    abbr = models.CharField(max_length=4, unique=True, null=True, blank=True, default='')
    slug = models.SlugField(null=True, blank=True, default='', editable=False)
    college = models.ForeignKey(College, null=True, blank=True, default=None)
    courses = models.ManyToManyField(Course, related_name='Courses', null=True, blank=True, default=None)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ['abbr']
    
    def save(self, *args, **kwargs):
        if self.slug == '':
            self.slug = slugify(self.name)
        super(Department, self).save(*args, **kwargs)
    
    @models.permalink
    def get_absolute_url(self):
        return ('apps.college.views.department', [str(self.abbr)])

class Major(models.Model):
    name = models.CharField(max_length=100)
    college = models.ForeignKey(College, null=True, blank=True, default=None)
    department = models.ForeignKey(Department, null=True, blank=True, default=None)
    abbr = models.CharField(max_length=15, null=True, blank=True, default="")
    coursesRequired = models.ManyToManyField(Course, related_name='Required_Course', null=True, blank=True, default=None)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ['abbr']
        
    @models.permalink
    def get_absolute_url(self):
        return ('apps.college.views.major', [str(self.abbr)])
    
class Minor(Major):
    pass