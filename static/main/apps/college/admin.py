from django.contrib import admin
from apps.college.models import *

class MajorAdmin(admin.ModelAdmin):
    class Meta:
        model = Major

admin.site.register(College)
admin.site.register(Department)
admin.site.register(Major, MajorAdmin)
admin.site.register(Minor)