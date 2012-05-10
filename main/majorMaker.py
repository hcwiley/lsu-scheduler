from apps.college.models import Major, College, Department
from django.template.defaultfilters import slugify
from glob import glob
import os
import re
#from django.template.defaultfilters import slugify
def main():
    colleges = glob('./apps/college/colleges/*.txt')
    for college in colleges:
        college = college.lstrip('./apps/college/colleges/')
        college = college.rstrip('.txt')
        college = college.strip()
#        print college
        file = open('./apps/college/colleges/%s.txt' % college, 'r')
        for major in file.readlines():
            major = major.strip()
            abbr = major.split(':')[0]
            abbr = re.sub(' +',' ',abbr)
            abbr = slugify(abbr).upper()
            name = major.split(':')[1]
            name = re.sub(' +',' ',name)
            try:
                degree = name.split(',')[1]
                degree = degree.strip()
                degree = degree.split(' ')[0]
#                print 'degree: %s' % degree
            except:
                pass
            maj = Major.objects.get(abbr=abbr)
            maj.degree_type = degree
            maj.save()
            
            #look for the file named maj.abbr + '.txt', parse it, and add the courses to maj.coursesRequired
            try:
                pathT ='./apps/college/majors/%s.txt' % abbr
                majorFile = open(pathT, 'r')
                print pathT
                for courseInfo in majorFile.readlines():
                    #parse the line, determine if it's important, add it as a course.
                    if courseInfo == '': #empty line. no data here
                        continue
                    elif courseInfo[0].isdigit(): #this is a semester number line
                        continue
                    courseInfo = courseInfo.strip('.') #remove '.' for the varying GEN ED lines
                    courseInfo = courseInfo.split(' ') #split into words
                    print(courseInfo[0])
                    if courseInfo[0] == 'Total': #first word is Total. Total semester hours
                        continue
                    elif courseInfo[0] == 'Critical:': #critical requirements. this could be useful later.
                        continue
                    #APPROVED, STUDIO ART, GEN ED, why do they do this crap to us?
                    #try to look up a course by college and number.
                    try:
                        myDept = abbr=courseInfo[0]
                        myNum = int(courseInfo[1])
                        print("%s: %s" % (myDept, myNum))
                        myDept = Department.objects.get(abbr=myDept)
                        print("deptobj: %s" % myDept)
                        departmentCourses = myDept.courses
                        print("deptcourses: %s" % departmentCourses)
                        course = departmentCourses.filter(number=myNum)[0]
                        print('course is: %s' % course)
                        print(maj)
                        print(len(maj.coursesRequired.filter(number=course.number, title=course.title)))
                        if(len(maj.coursesRequired.filter(number=course.number, title=course.title)) == 0):
                            maj.coursesRequired.add(course)
                            print('added course: %s' % course)
                    except:
                        print 'oh foo bar'
                        pass
                    maj.save()
                    #course's college = courseInfo[0]
                    #course's number = courseInfo[1]
                    #associate this major with the first match, if any
                    #print(courseInfo)
                    
            except:
#                print 'error 2'
                pass
            
            maj.save()
            
            if len(abbr.split(' ')) > 0:
                abbr = abbr.split(' ')[0]
            try:
                col = College.objects.get(abbr=college)
                maj.college = col
#                print 'college: %s' % col.name
                maj.save()
            except:
                pass
#                print 'no matching college for: %s' % college
            try:
                dept = Department.objects.get(abbr=abbr)
                maj.department = dept
#                print 'department: %s' % dept.name
                maj.save()
            except:
                pass
#                print 'no matching department for: %s' % abbr