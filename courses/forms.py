from courses.models import *
from django.contrib.auth.models import User
from django import forms
from django.forms.models import modelformset_factory
from django.forms import ModelForm, Select
from crispy_forms.helper import FormHelper
from crispy_forms.layout import *
from django.core.cache import cache

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
	code = forms.ModelChoiceField(queryset=Course.objects.all(),
				widget=Select(attrs={'style':'color:#000;'}))

class ProfForm(forms.Form):
	prof = forms.ModelChoiceField(queryset=Professor.objects.all(),
				widget=Select(attrs={'style':'color:#000;'}))

class AddCourseRatingForm(forms.ModelForm):
	class Meta:
		model = CourseRating
		fields = ('score', 'comment_text')
	def __init__(self, *args, **kwargs):
		super(AddCourseRatingForm, self).__init__(*args, **kwargs)
		self.fields['comment_text'].widget.attrs['style'] = "width:100%;height:100px;color:#000;"
		self.fields['score'].widget.attrs['style'] = "color:#000;"	

class AddProfRatingForm(forms.ModelForm):
	class Meta:
		model = ProfRating
		fields = ('score', 'comment_text', 'comment_professor')
	def __init__(self, *args, **kwargs):
		super(AddProfRatingForm, self).__init__(*args, **kwargs)
		self.fields['comment_text'].widget.attrs['style'] = "width:100%;height:100px;color:#000;"
		self.fields['score'].widget.attrs['style'] = "color:#000;"	
		self.fields['comment_professor'].widget.attrs['style'] = "color:#000;"

#for an individual section
class SectionForm(forms.Form):
	#def __init__(self, user, *args, **kwargs):
	#	super(SectionForm, self).__init__(*args, **kwargs)
	# work on getting form to prepopulate based on semester	
	semester = Semester.objects.get(session='Fall', year=2014)
	semester_queryset=Section.objects.filter(semester=semester) #save and cache queryset
	course1 = forms.ModelChoiceField(queryset=semester_queryset,
		widget=Select(attrs={'style':'color:#000;'}))
	course2 = forms.ModelChoiceField(queryset=semester_queryset,
		widget=Select(attrs={'style':'color:#000;'}))
	course3 = forms.ModelChoiceField(queryset=semester_queryset,
		widget=Select(attrs={'style':'color:#000;'}))
	course4 = forms.ModelChoiceField(queryset=semester_queryset,
		widget=Select(attrs={'style':'color:#000;'}))
	course5 = forms.ModelChoiceField(queryset=semester_queryset,
		widget=Select(attrs={'style':'color:#000;'}))

class BrowserForm(forms.ModelForm):
	class Meta:
		model = Course
		fields = ('dept', 'dists')
	semester = forms.ModelChoiceField(queryset=Semester.objects.all())
	

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Student
		exclude = ('user', 'courses')	
	#def __init__(self, *args, **kwargs):
        #super(ProfileForm, self).__init__(*args, **kwargs)
        #self.queryset = Student.objects.filter(user=request.user)
