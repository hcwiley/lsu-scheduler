from django.conf import settings
from django.contrib import admin
from django.views.generic.simple import redirect_to, direct_to_template
from django.conf.urls.defaults import patterns, url, include
from django.contrib.auth import views as auth_views
admin.autodiscover()


urlpatterns = patterns('apps.college.views',
   (r'^$', 'home'),
   (r'^collegeManager', 'collegeManager'),
   (r'^majorManager', 'majorManager'),
   (r'^department/filter$', 'filter'),
   (r'^department/(?P<abbr>.*)$', 'department'),
   (r'^college/(?P<abbr>.*)$', 'college'),
   (r'^major/(?P<abbr>.*)$', 'major'),
)