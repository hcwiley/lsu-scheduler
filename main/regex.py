from apps.course.models import *
import urllib
import urllib2
#from BeautifulSoup import BeautifulSoup
import BeautifulSoup
from datetime import time

#re.sub('.*\*\*.*\n', '', l)
'''
def pullFromHTML(semester, year, dept):
	headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US;' +'rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)'}
	host = 'http://appl003.lsu.edu'

	req = urllib2.Request(host + '/booklet2.nsf/Selector2?OpenForm', '', headers)
	res = urllib2.urlopen(req)

	data = urllib.urlencode({'SemesterDesc': str(semester).capitalize() + " " + str(year), 'Department': str(dept).upper()})

	req = urllib2.Request(host + BeautifulSoup(res.read()).form['action'], data, headers)
	res = urllib2.urlopen(req)

	courseslist = BeautifulSoup(res.read()).pre.string[:]
	return courseslist

#pString = 'Dept:%s Course#:%s Enrollment:%s Available:%s Type:%s Section:%s Title:%s Hours:%s Begin:%s End:%s N:%s Days:%s Room:%s Building:%s Special:%s Instructor:%s' % (dept, num, enroll, avail, type, section, title, hours, begin, end, n, days, room, building, special, instructor)



# need classes for Course, lab, multiple instructors?
htmlCourses = pullFromHTML("Fall", 2012, "CSC")
print htmlCourses
'''
lastCourse = None
schedule = []
def main():
	c = -1
	for bob in schedule:
		c += 1
		print bob
		if c < 4:
			continue
		if len(bob) > 5 and bob[6] == '*':
			continue
		avail = bob[0:3].strip()
		enroll = bob[5:8].strip() if len(bob[5:8].strip()) != 0 else 0
		dept = bob[11:15].strip()
		num = bob[16:20].strip()
		courseType = bob[21:24].strip()
		section = bob[27:31].strip()
		title = bob[32:54].rstrip()
		hours = bob[55:61].strip()
		begin = bob[60:64].strip()
		begin = (int(begin[:len(begin)/2]) , int(begin[len(begin)/2:]))
		print begin
		end = bob[65:69].strip()
		end = (int(end[:len(end)/2]) , int(end[len(end)/2:]))
		print end
		n = bob[69].strip()
		days = bob[72:77].strip()
		room = bob[79:83].strip()
		building = bob[84:100].rstrip()
		special = bob[100:114].rstrip()
		instructor = bob[117:130].rstrip()
		if courseType == 'LAB' and title == '':
			lab = Lab.objects.create(course=lastCourse)
			lab.start_time = begin
			lab.end_time = end
			if begin != "TBA":
				lab.time_tba = False
			else:
				lab.time_tba = True
			lab.days = days
			lab.building = building
			lab.instructor = instructor
		elif title:
			print "title: %s" % title
			course = Course.objects.create(title=title)
#			course.title = title
			course.number = num
			course.abbr = dept
			course.section_number = section 
			course.start_time = time(begin[0], begin[1]).strftime('%H:%M')
			course.end_time = time(end[0], end[1]).strftime('%H:%M')
			if begin != "TBA":
				course.time_tba = False
			else:
				course.time_tba = True
			course.days.add(Date.objects.get_or_create(day=days)[0])
			course.building = building
			course.instructor = instructor
			course.available_seats = avail
			course.number_enrolled = enroll
			course.special_enrollment = special
			course.type = courseType
			course.save()
			print course
			lastCourse = course
