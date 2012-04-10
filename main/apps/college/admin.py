from django.contrib import admin
from apps.college.models import *

admin.site.register(College)
admin.site.register(Department)
admin.site.register(Major)
admin.site.register(Minor)