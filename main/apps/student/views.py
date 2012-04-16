from django.conf import settings
from datetime import datetime
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.core.context_processors import csrf
from django.contrib.auth import logout
from apps.course.models import *
from apps.student.models import *
from apps.college.models import *
from django.core import serializers
from main.views import common_args
from apps.student.forms import StudentForm

def student_args(request):
    args = common_args(request)
    return args 

def student(request, id=None):
    if id == None:
        return redirect('/students')
    args = student_args(request)
    args.update(csrf(request))
    student = Student.objects.get(id=id)
    args['student'] = student
    if request.method == 'POST':
        print 'its a post'
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            print 'its valid'
            form.save()
    student.getCoursesNeeded()
    args['courses'] = Course.objects.all()
    args['studentForm'] = StudentForm(instance=student)
    return render_to_response('student/student.html', args)