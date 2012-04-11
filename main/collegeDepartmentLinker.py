from apps.college.models import Major, College, Department
#from django.template.defaultfilters import slugify
def main():
    colleges = College.objects.all()
    for college in colleges:
        for major in college.major_set.all():
            print 'major: %s' % major
            try:
                department = major.department
                print 'department: %s' % department
                department.college = college
                department.save()
            except:
                print 'no department'