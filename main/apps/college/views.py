from django.conf import settings
from datetime import datetime
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.core.context_processors import csrf
from django.contrib.auth import logout
#from apps.course.models import *
#from apps.student.models import *
from apps.college.models import *
from apps.college.forms import *
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

def collegeManager(request):
    args = college_args(request)
    if request.method == 'POST':
        print 'its a post'
        print request.POST
        pk = request.POST['pk']
        pk = pk.lstrip(' ')
        college = College.objects.get(id=pk)
        print 'college: %s' % college.name
        form = CollegeManagerForm(request.POST)
        if form.is_valid():
            print 'its valid'
            college.department_set.clear()
            for dept in form.cleaned_data['departments']:
                college.department_set.add(dept)
            college.major_set.clear()
            for maj in form.cleaned_data['majors']:
                print maj
                college.major_set.add(maj)
            college.save()
    args['majorForm'] = MajorForm()
    args['collegeForm'] = CollegeManagerForm()
    args['departmentForm'] = DepartmentForm()
    args['departments'] = Department.objects.all()
    args['colleges'] = College.objects.all()
    args['majors'] = Major.objects.all()
    args.update(csrf(request))
    return render_to_response("college/collegeManager.html", args)

def majorManager(request):
    args = college_args(request)
    if request.method == 'POST':
        print 'its a post'
        print request.POST
        abbr = request.POST['abbr']
        major = Major.objects.get(abbr=abbr)
        form = MajorForm(request.POST, instance=major)
        if form.is_valid():
            form.save()
            print 'its valid'
    args['majorForm'] = MajorForm()
    args['collegeForm'] = CollegeManagerForm()
    args['departmentForm'] = DepartmentForm()
    args['departments'] = Department.objects.all()
    args['colleges'] = College.objects.all()
    args['majors'] = Major.objects.all()
    args['courses'] = Course.objects.all()
    args.update(csrf(request))
    return render_to_response("college/majorManager.html", args)
