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

def college_args(request):
    args = common_args(request)
    return args

def department(request, abbr=None):
    if abbr == None:
        return redirect('/departments')
    args = college_args(request)
    args['department'] = Department.objects.get(abbr=abbr)
    args.update(csrf(request))
    return render_to_response('college/department.html', args)