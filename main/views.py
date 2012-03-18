from django.conf import settings
from datetime import datetime
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.core.context_processors import csrf
from django.contrib.auth import logout
from apps.course.models import *
from django.core import serializers

def common_args(request):
    """
    The common arguments for all gallery views.
    
    STATIC_URL: static url from settings
    year: the year at the time of request  
    """ 
    user = request.user if request.user.is_authenticated() else None
    args = {
                'base_template' : 'base-ajax.html' if request.is_ajax() else 'base.html',
                'STATIC_URL' : settings.STATIC_URL,
                'MEDIA_URL' : settings.MEDIA_URL,
                'user' : user,
                'cur_page' : request.path.split('/')[len(request.path.split('/'))-1]
           }
    return args


#def get_form(request, form_class, instance):
#    if request.method == 'POST':
#        print 'got here'
#        form = form_class(request.POST, request.FILES, instance=instance)
#        if form.is_valid():
#            print 'valid'
#            form.save(commit=False)
#            #DO SOMETHING HERE
#            form.save()
#            form = form_class(instance=instance)
#    else:
#        form = form_class(instance=instance)
#        
#    return form

def home(request):
    args = common_args(request)
    args['courses'] = serializers.serialize( "python", Course.objects.all())
    args.update(csrf(request))
    return render_to_response('index.html', args)