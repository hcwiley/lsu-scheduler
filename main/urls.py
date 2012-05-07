from django.conf import settings
from django.contrib import admin
from django.views.generic.simple import redirect_to, direct_to_template
from django.conf.urls.defaults import patterns, url, include
from django.contrib.auth import views as auth_views
from apps.college import urls as college_urls
from apps.course import urls as course_urls
from apps.student import urls as student_urls
admin.autodiscover()


urlpatterns = patterns('',
    (r'^favicon.ico$', redirect_to, {'url': '/site_media/static/images/fav.ico'}),
    (r'^robots.txt$', direct_to_template, {'template':'robots.txt', 'mimetype':'text/plain'}),
    (r'^sitemap.txt$', direct_to_template, {'template':'sitemap.txt', 'mimetype':'text/plain'}),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^allCollegeForm$', 'views.allCollegeForm'),
    (r'^/$', 'views.home'),
    (r'^$', 'views.home'),
    (r'^schedule/(?P<id>.*)$', 'views.schedule'),
    (r'^colleges/', include(college_urls)),
    (r'^courses/', include(course_urls)),
    (r'^students/', include(student_urls)),
    
)


if settings.DEBUG:
    # let django serve user generated media while in development
    urlpatterns += patterns('',
#TODO don't let people name their top level series admin, site_media, etc.
        (r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:], 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )