from django.conf import settings
from django.contrib import admin
from django.views.generic.simple import redirect_to, direct_to_template
from django.conf.urls.defaults import patterns, url, include
from django.contrib.auth import views as auth_views
admin.autodiscover()


urlpatterns = patterns('apps.student.views',
    (r'^(?P<id>.*)$', 'student'),
)