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

def home(request):
    args = college_args(request)
    args['departments'] = Department.objects.all()
    args['colleges'] = College.objects.all()
    args['majors'] = Major.objects.all()
    return render_to_response('college/list-all.html', args)

def department(request, abbr=None):
    if abbr == None:
        return redirect('/departments')
    args = college_args(request)
    args['department'] = Department.objects.get(abbr=abbr)
    args.update(csrf(request))
    return render_to_response('college/department.html', args)

def college(request, abbr=None):
    if abbr == None:
        return redirect('/colleges')
    args = college_args(request)
    args['college'] = College.objects.get(abbr=abbr)
    args.update(csrf(request))
    return render_to_response('college/college.html', args)

def major(request, abbr=None):
    if abbr == None:
        return redirect('/majors')
    args = college_args(request)
    args['major'] = Major.objects.get(abbr=abbr)
    args.update(csrf(request))
    return render_to_response('college/major.html', args)

def filter(request, abbr=None):
    args = college_args(request)
    args['departments'] = Department.objects.all()
    args['colleges'] = College.objects.all()
    args['majors'] = Major.objects.all()
    args.update(csrf(request))
    return render_to_response('college/filter.html', args)
    