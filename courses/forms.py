from courses.models import *
from django.contrib.auth.models import User
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import *

#Creates user
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

#Creates student course profile
class StudentProfileForm(forms.ModelForm):
	username = forms.CharField(max_length=30)
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = Student
		fields = ('class_year', 'primary_major', 'secondary_major')
	

class AddCourseForm(forms.Form):
	code = forms.ModelChoiceField(queryset=Course.objects.all())

class AddCourseRatingForm(forms.ModelForm):
	class Meta:
		model = CourseRating
		fields = ('score', 'comment_text')
	def __init__(self, *args, **kwargs):
		super(AddCourseRatingForm, self).__init__(*args, **kwargs)
		self.fields['comment_text'].widget.attrs['style'] = "width:400px;height:50px;"

