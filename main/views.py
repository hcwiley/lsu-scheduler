from django.conf import settings
from datetime import datetime
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.core.context_processors import csrf
from django.contrib.auth import logout
from apps.course.models import *
from apps.student.models import *
from apps.student.forms import *
from apps.college.models import *
from apps.college.forms import *
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


def get_form(request, form_class, instance=None):
    if request.method == 'POST':
        form = form_class(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            print 'valid'
            form.save(commit=False)
            #DO SOMETHING HERE
            form.save()
            form = form_class(instance=instance)
    else:
        form = form_class(instance=instance)
        
    return form

def schedule(request, id=None):
    student = Student.objects.get(id=id)
    args = common_args(request)
    args.update(csrf(request))
    args['courses'] = Course.objects.all()
    args['departments'] = Department.objects.all()
    args['colleges'] = College.objects.all()
    args['majors'] = Major.objects.all()
    args['student'] = student
    # manual filter for not showing classes already taken 
    coursesStillNeeded = student.major.coursesRequired
    for course1 in coursesStillNeeded.all():
        for course2 in student.coursesTaken.all():
            if course1.id == course2.id:
                coursesStillNeeded.remove(course1)
    args['coursesStillNeeded'] =  coursesStillNeeded
    args['courseBucket'] = []
    h = []
    for i in range(7,20):
        h.append(i)
    args['hours'] = h
    args['allCollegeForm'] = AllCollegeForm()
    return render_to_response('schedule.html', args)

def allCollegeForm(request):
    print 'hey!'
    if request.method == 'POST':
        form = AllCollegeForm(request.POST)
        if form.is_valid():
            print 'valid'
            #get the ID of the college
            collegeObj = form.cleaned_data['college'] #Not sure if it returns the name or the id
            print collegeObj
            
            #get the ID of the department
            departmentObj = form.cleaned_data['department'] #Not sure if it returns the name or the id
            print departmentObj
            
            #get the ID of the major
            majorObj = form.cleaned_data['major'] #Not sure if it returns the name or the id
            print majorObj
            
            courses = []
            if (departmentObj == ""):
                #if we only have a college,
                #Get all departments of the college
                departments = []
                departments = Department.objects.get(college=collegeObj) 
                #for each department in the college, add all the courses
                
                for dept in departments:
                    for course in dept.courses.all():
                        courses.append(course)
            elif (majorObj == ""):
                #if we have a single department, courses are all the courses of that department
                for course in deptObj.courses.all():
                    courses.append(course)
            else:
                #if we have a single major, courses are the required courses of that major
                for majorCourse in majorObj.coursesRequired.all():
                    courses.append(majorCourse)
                    
                form = AllCollegeForm()
                args = {'allCollegeForm' : form, 'courses': courses}
            args.update(csrf(request))
            return render_to_response('courseList.html', args)
    else:
        return "Raise404"

def home(request):
    args = common_args(request)
    args['students'] = Student.objects.all()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            print 'valid'
            stu = form.save(commit=False)
            form.save()
            return redirect('/schedule/%s' % stu.id )
            return redirect(stu.get_absolute_url())
    else:
        form = StudentForm()#instance=instance)
        args['studentForm'] = form
        args['courses'] = Course.objects.all()
        args['departments'] = Department.objects.all()
        args['colleges'] = College.objects.all()
        args['majors'] = Major.objects.all()
        args.update(csrf(request))
        return render_to_response('index.html', args)