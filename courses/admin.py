from django.contrib import admin
from courses.models import * 

admin.site.register(UserProfile)
admin.site.register(Student)
admin.site.register(Major)
admin.site.register(Course)
admin.site.register(CourseRating)
admin.site.register(ProfRating)
