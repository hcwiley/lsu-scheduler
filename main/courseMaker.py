from apps.course.models import Course, Date, Lab
from apps.college.models import Department
import urllib
import urllib2
#from BeautifulSoup import BeautifulSoup
import BeautifulSoup
from datetime import time

#re.sub('.*\*\*.*\n', '', l)

def pullFromHTML(semester, year, dept):
	headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US;' + 'rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)'}
	host = 'http://appl003.lsu.edu'

	req = urllib2.Request(host + '/booklet2.nsf/Selector2?OpenForm', '', headers)
	res = urllib2.urlopen(req)

	data = urllib.urlencode({'SemesterDesc': str(semester).capitalize() + " " + str(year), 'Department': str(dept).upper()})

	req = urllib2.Request(host + BeautifulSoup.BeautifulSoup(res.read()).form['action'], data, headers)
	res = urllib2.urlopen(req)

	courseslist = BeautifulSoup.BeautifulSoup(res.read())
	courseslist = courseslist.pre.string[:]
	return courseslist

#pString = 'Dept:%s Course#:%s Enrollment:%s Available:%s Type:%s Section:%s Title:%s Hours:%s Begin:%s End:%s N:%s Days:%s Room:%s Building:%s Special:%s Instructor:%s' % (dept, num, enroll, avail, type, section, title, hours, begin, end, n, days, room, building, special, instructor)



# need classes for Course, lab, multiple instructors?
def getDept(dept):
#dept = "FILM & MEDIA ARTS"
	htmlCourses = pullFromHTML("Fall", 2012, dept)
	foo = open('apps/college/departments/%s.txt' % dept, 'w') 
	foo.write(htmlCourses)

def getAllDepts():
		foo = open("apps/college/departments.data", "r")
		for dept in foo.readlines():
			dept = dept.strip()
			try:
#				print dept
#				getDept(dept)
#				print 'pulled down %s' % dept
				main(dept)
			except:
				print "couldnt get %s department" % dept

def main(dept):
	schedule = open('apps/college/departments/%s.txt' % dept, 'r')
	dept = dept.rstrip('.txt').capitalize()
	department = Department.objects.get_or_create(name=dept)
	if department[1]:
		print 'saving department: %s' % department[0].name 
		department[0].save()
	department = department[0]
	abbrSet = False
	if len(department.abbr) > 2:
		abbrSet = True
#	print department.name
	lastCourse = None
	c = -1
	for bob in schedule:
		c += 1
#		print bob
		if c < 4 or bob.replace(' ', '') == '':
			continue
		if len(bob) > 5 and bob[6] == '*':
			continue
		try:
			avail = bob[0:3].strip()
			avail = int(avail)
		except:
			avail = -1
			#print 'available not available'
		try:
			enroll = bob[5:8].strip() if len(bob[5:8].strip()) != 0 else 0
			enroll = int(enroll)
		except:
			enroll = 0
			#print 'no enrollment count'
		abbr = bob[11:15].strip()
		try:
			num = bob[16:20].strip()
			num = int(num)
		except:
			num = 0
			#print 'not good.. no number'
		courseType = bob[21:24].strip()
		section = bob[27:31].strip()
		try:
			section = int(section)
		except:
			section = 1
			#print 'no section'
		title = bob[32:54].rstrip()
		hours = bob[55:61].strip()
		try:
			hours = int(hours)
		except:
			hours = 0
			#print "no hours"
		try:
			begin = bob[60:64].strip()
#			#print "being len: %s" % len(begin)
			if begin != 'TBA':
				if len(begin) % 2 == 0:
					begin = (int(begin[:2]) , int(begin[2:]))
				else:
					begin = (int(begin[0]) , int(begin[1:]))
#			#print "begin: %s:%s" % (begin[0], begin[1])
		except:
			begin = 'TBA'
			#print "begin failed"
		try:
			end = bob[65:69].strip()
#			#print "end len: %s" % len(end)
			if end != '':
				if len(end) % 2 == 0:
					end = (int(end[:2]) , int(end[2:]))
				else:
					end = (int(end[0]) , int(end[1:]))
#			#print "end: %s:%s" % (end[0], end[1])
		except:
			end = None
			#print 'no end time'
		try:		
			n = bob[69].strip()
		except:
			n = ''
			#print 'no class number'
		try:
			days = bob[72:77].strip()
		except:
			days = ''
			#print 'no days'
		try:
			room = bob[79:83].strip()
		except:
			room = ''
			#print 'no room number'
		try:
			building = bob[84:100].rstrip()
		except:
			building = ''
			#print 'no building'
		try:
			special = bob[100:114].rstrip()
		except:
			special = ''
			#print 'no special stuff'
		try:
			instructor = bob[117:130].rstrip()
		except:
			instructor = ''
			#print 'no instructor'
		try:
			if courseType == 'LAB' and title == '' and lastCourse != None:
	#			print 'lab if'
				lab = Lab.objects.create(course = lastCourse)
				if begin != "TBA":
					lab.time_tba = False
					lab.start_time = time(begin[0], begin[1]).strftime('%H:%M')
					lab.end_time = time(end[0], end[1]).strftime('%H:%M')
				else:
					lab.time_tba = True
				try:
					for day in days:
						if day != ' ':
							lab.days.add(Date.objects.get_or_create(day = day)[0])
				except:
					print 'failed adding lab days'
				lab.building = building
				lab.instructor = instructor
				continue
		except:
			print 'lab failed'
#		if type(num) == int:
#		print "title: %s" % title
#		print "dept: %s" % abbr
#		print "number: %s" % num
#		print "section: %s" % section
#		print 'building: %s' % building 
		if not abbrSet:
			department.abbr = abbr
			department.save()
			abbrSet = True
			print 'set the abbr for dept: %s : %s' % (department.abbr, department.name)
		course = Course.objects.get_or_create(title = title, number = num, section_number = section)
		isNew = course[1]
#		print "is new: %s" % isNew
		course = course[0]
		try:
			department.courses.add(course)
		except:
			print 'failed adding course to department'
		if begin != "TBA":
			course.time_tba = False
		else:
			course.time_tba = True
		if not course.time_tba:
			course.start_time = time(begin[0], begin[1]).strftime('%H:%M')
			course.end_time = time(end[0], end[1]).strftime('%H:%M')
		try:
			for day in days:
				if day != ' ':
					course.days.add(Date.objects.get_or_create(day = day)[0])
		except:
			print 'adding days failed'
		course.building = building
		course.instructor = instructor
		course.available_seats = avail
		course.number_enrolled = enroll
		course.special_enrollment = special
		course.credit_hours = hours
		course.type = courseType
		course.abbr = abbr
        course.save()
        lastCourse = course
