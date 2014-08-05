from courses.models import *
from django.contrib.auth.models import User
from django import forms

#Creates user
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

#Creates student course profile
class StudentProfileForm(forms.ModelForm):
		
	class Meta:
		model = Student
		exclude = (
			'user', 
			'major_requirements_completed', 
			'distribution_requirements_completed'
			) 

class AddCourseForm(forms.Form):
	dept = forms.CharField(max_length=100, widget=forms.Select(choices=DEPARTMENTS))
	code = forms.ModelChoiceField(queryset=Course.objects.all())

class AddCourseRatingForm(forms.ModelForm):
	class Meta:
		model = CourseRating
		exclude = ('comment_author')
