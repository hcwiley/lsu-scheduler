from django.contrib import admin
from apps.course.models import *

admin.site.register(Lab)
admin.site.register(Course, CourseAdmin)
admin.site.register(Date)