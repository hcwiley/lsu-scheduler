from apps.course.models import *

#re.sub('.*\*\*.*\n', '', l)




# need classes for Course, lab, multiple instructors?

lastCourse = None
schedule = []

for bob in schedule:
	if bob[6] == '*':
		break
	avail = bob[0:3].strip()
	enroll = bob[5:8].strip() if len(bob[5:8].strip()) != 0 else 0
	dept = bob[11:15].strip()
	num = bob[16:20].strip()
	courseType = bob[21:24].strip()
	section = bob[27:31].strip()
	title = bob[32:54].rstrip()
	hours = bob[55:61].strip()
	begin = bob[60:64].strip()
	end = bob[65:69].strip()
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
	else:	
		course = Course.objects.create()
		course.title = title
		course.number = num
		course.abbr = dept
		course.section_number = section 
		course.start_time = begin
		course.end_time = end
		if begin != "TBA":
			course.time_tba = False
		else:
			course.time_tba = True
		course.days = days
		course.building = building
		course.instructor = instructor
		course.available_seats = avail
		course.number_enrolled = enroll
		course.special_enrollment = special
		course.type = courseType
		lastCourse = course



#pString = 'Dept:%s Course#:%s Enrollment:%s Available:%s Type:%s Section:%s Title:%s Hours:%s Begin:%s End:%s N:%s Days:%s Room:%s Building:%s Special:%s Instructor:%s' % (dept, num, enroll, avail, type, section, title, hours, begin, end, n, days, room, building, special, instructor)

