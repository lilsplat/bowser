from bowser import settings
from django.core.management import setup_enviorn
setup_enviorn(settings)

from courses.models import Course

output = "["
courses = Course.objects.all()
for course in course:
	output += "'" + course_code + "', "
output += "]"
print output
