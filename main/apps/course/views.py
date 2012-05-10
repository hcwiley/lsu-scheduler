from django.conf import settings
from datetime import datetime
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.core.context_processors import csrf
from django.contrib.auth import logout
#from apps.course.models import *
#from apps.student.models import *
from apps.college.models import *
from django.core import serializers
from main.views import common_args
from apps.course.models import WEEKDAYS

def course_args(request):
    args = common_args(request)
    return args

def course(request, id=None):
    if id == None:
        redirect('/courses')
    args = course_args(request)
    args['course'] = serializers.serialize('python', Course.objects.filter(id=id))[0]
    args['weekdays'] = WEEKDAYS
    args.update(csrf(request))
    return render_to_response('course/course.html', args)