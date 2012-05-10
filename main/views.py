from django.conf import settings
from datetime import datetime
from django.shortcuts import render_to_response, get_object_or_404, redirect, HttpResponse
from django.core.context_processors import csrf
from django.contrib.auth import logout
from apps.course.models import *
from apps.student.models import *
from apps.student.forms import *
from apps.college.models import *
from apps.college.forms import *
from apps.course.forms import *
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
    args['coursesWanted'] = CoursesWanted()
    h = []
    for i in range(7,20):
        h.append(i)
    args['hours'] = h
    args['allCollegeForm'] = AllCollegeForm()
    return render_to_response('schedule.html', args)

def allCollegeForm(request):
    if request.method == 'POST':
        form = AllCollegeForm(request.POST)
        if form.is_valid():
            #get the ID of the college
            collegeObj = form.cleaned_data['college'] #Not sure if it returns the name or the id
            collegeObj = collegeObj[0]
            
            #get the ID of the department
            try:
                departmentObj = form.cleaned_data['department'] #Not sure if it returns the name or the id
                departmentObj = departmentObj[0]
            except:
                departmentObj = None
            
            #get the ID of the major
            try:
                majorObj = form.cleaned_data['major'] #Not sure if it returns the name or the id
                majorObj = majorObj[0]
            except:
                majorObj = None
            
            courses = []
            if (departmentObj == None):
                #print("if we only have a college")
                #Get all departments of the college
                departments = []
                departments = Department.objects.filter(college=collegeObj)
                #for each department in the college, add all the courses
                
                for dept in departments:
                    for course in dept.courses.all():
                        courses.append(course)
            elif (majorObj == None):
                #print("if we have a single department, courses are all the courses of that department")
                for course in departmentObj.courses.all():
                    courses.append(course)
            else:
                #print("if we have a single major, courses are the required courses of that major")
                for majorCourse in majorObj.coursesRequired.all():
                    courses.append(majorCourse)
            form = AllCollegeForm()
            args = {'allCollegeForm' : form, 'courses': courses}
            args.update(csrf(request))
            return render_to_response('course/courseList.html', args)
    else:
        return "Raise404"

def coursesWanted(request):
    print 'hey!'
    if request.method == 'POST':
        form = CoursesWanted(request.POST)
        if form.is_valid():
            #print("valid!")
            courseBucket = form.cleaned_data['courses']
            student = form.cleaned_data['student_pk']
            student = Student.objects.get(id=student)
            #print courses
            #print student.name
            form = CoursesWanted()
            
            #this is where teh magic should happen.
            #list of tuples (section, priority) to reference conflicts
            allCourses = []
            #list of courseLists to return 
            schedules = []
            #list of (section)s where there is no conflict
            safeCourses = list(courseBucket)
            #list of tuples (section, otherSection) where there is a conflict
            conflictingCourses = []
            #list of low priority tossed classes
            tossedCourses = []
            print("first pass starting")
            #first pass, separate safe and conflicting courses
            for course in courseBucket:
                #if course.isAbstract:
                #    safeCourses.remove(course)
                #    for section in Course.objects.filter(title=course.title, number=course.number):
                #        TODO: iterate through these sections
                priority = 0
                #if the title of the course is in the courses needed, the priority is higher
                if (student.coursesNeeded.filter(title=course.title, number=course.number) > 0):
                    priority = 1
                #check to make sure the time slot isn't taken
                for otherCourse in allCourses:
                    if (otherCourse[0]==course):
                        continue
                    #if the other section's start time is the same
                    #TODO: check time 'slot' not time start
                    if (otherCourse[0].start_time == course.start_time ):
                        print("found a conflict")
                        conflictingCourses.append((course, otherCourse[0]))
                        if (safeCourses.count(course)>0):
                            safeCourses.remove(course)
                        print ("removed, moving to check")
                        if (safeCourses.count(otherCourse[0])>0):
                            safeCourses.remove(otherCourse[0])
                            
                        #here lies unused priority code
                        #if the other section's priority is higher
                        #if ():
                            #then we need to discard this class, or put it in a new schedule
                        #    safeCourses.remove(course)
                        #    tossedCourses.append(course)
                        #if the other course's priority is the same
                        #if (otherCourse[1] == priority or otherCourse[1] > priority):
                            #then we have an impasse.  We need a new schedule
                        #else, the other section's priority is lower, so put this one in instead
                        #else: 
                        #  tossedCourses.append(otherCourse[0])
                        
                allCourses.append((course, priority))
            print("finished with first pass")
            #second pass, adding up schedules
            evaluateBranches(schedules, list(safeCourses), list(conflictingCourses))
            print("finished with second pass")
            html = ""
            h = []
            for i in range(7,20):
                h.append(i)
            print("heading to append schedules")
            for schedule in schedules:
                args = {'coursesWanted' : form, 'scheduledCourse': schedule, 'schedule_number': str(schedules.index(schedule)+1)}
                args['hours'] = h
                args.update(csrf(request))
                temphtml = render_to_response('course/scheduleTable.html', args)
                print("+= here")
                html += str(temphtml)
                #print(temphtml)
            print("time to return!")
            return HttpResponse('%s' % html, content_type="text/html")

def evaluateBranch(schedules, conflicts, blackList, branchSchedule):
    print("we are evaluating a branch")
    if (len(conflicts) > 0):
        #pop. check blackList.
        flag1 = flag2 = False
        conflict = conflicts.pop()
        if (blackList.count(conflict[0]) == 0):
            blackList.append(conflict[0])
            flag1 = True
            #evaluate this with conflict0
        if (blackList.count(conflict[1]) == 0):
            blackList.append(conflict[1])
            flag2 = True
            #evaluate this with conflict1
        if (flag1):
            path1 = list(branchSchedule)
            path1.append(conflict[0])
            evaluateBranch(schedules, list(conflicts), list(blackList), path1)
        if (flag2):
            path2 = list(branchSchedule)
            path2.append(conflict[1])
            evaluateBranch(schedules, list(conflicts), list(blackList), path2)
        if (not (flag1 or flag2)):
            evaluateBranch(schedules, list(conflicts), list(blackList), branchSchedule)
    else:
        #append branchSchedule to schedules
        schedules.append(branchSchedule)
    
def evaluateBranches(schedules, safeCourses, conflicts):
    print("evaluating branches")
    if (len(conflicts) > 0):
        conflict = conflicts.pop()
        blackList = [conflict[0], conflict[1]]
        path1 = list(safeCourses)
        path1.append(conflict[0])
        path2 = list(safeCourses)
        path2.append(conflict[1])
        evaluateBranch(schedules, list(conflicts), list(blackList), path1)
        evaluateBranch(schedules, list(conflicts), list(blackList), path2)
    else:
        schedules.append(safeCourses)
        
def home(request):
    args = common_args(request)
    args['students'] = Student.objects.all()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            print 'valid'
            stu = form.save(commit=False)
            form.save()
            stu.getCoursesNeeded()
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