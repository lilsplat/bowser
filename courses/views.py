from __future__ import division
from django.shortcuts import render
from courses.forms import *
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from courses.models import Student

def index(request):
	context = RequestContext(request)
	if request.user.is_authenticated():
		return render_to_response('courses/index.html', context)
	else:
		return render_to_response('courses/landing.html', 
		{'user_form': UserForm(), 'register_form': StudentProfileForm()},
		context)

def register(request):
    context = RequestContext(request)
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
			user = user_form.save(commit=False)
			user.username += '@wellesley.edu'
			user.email = user.username
			user.set_password(user.password)
			user.save()
			#login new user
			user_login(request)
			registered = True
			#create student to correspond with user
			student = Student.objects.get_or_create(user=user)
        # errors that will also be shown to the user.
        else:
            print user_form.errors
    else:
        user_form = UserForm()
   
	#include registration form too 
	return render_to_response(
            'courses/register.html',
            {'user_form': user_form, 'register_form': StudentProfileForm()},
            context)
#login
def user_login(request):
	context = RequestContext(request)
	if request.method == 'POST':
		username = request.POST['username']
		print username
		password = request.POST['password']
		print password
		#to account for the way we ask users to input their username/email
		username += "@wellesley.edu"
		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				login(request, user)
				print 'user logged in'
				return redirect('/')
			else:
				return HttpResponseNotFound('<h1>Page not found</h1>')
		else:
			return HttpResponse('Invalid Login')
	else:
		return redirect(reverse('courses.views.index')) 

def user_logout(request):
    logout(request)
    return redirect('/')

def create_student_profile(request):
	print request.user
	context = RequestContext(request)
	profile_created = False
	if request.method == 'POST':
		student_form = StudentProfileForm(request.POST)
		print 'student form data variable created'
		if student_form.is_valid():
			print 'student form valid'
			print 'student data saved'
			#first create a user object
			username = student_form.cleaned_data['username'] + '@wellesley.edu'
 			password = student_form.cleaned_data['password']
			print 'username and password saved'
			user = User.objects.create_user(username, username, password)
			print 'user created'
			print 'user: ' + str(user)
			# now create corresponding student object
			student, created  = Student.objects.get_or_create(user=user)
			student.class_year = student_form.cleaned_data['class_year']
			student.primary_major = student_form.cleaned_data['primary_major']
			student.secondary_major = student_form.cleaned_data['secondary_major']
			student.save()
			profile_created = True
			#log in user before redirecting to home page
			user_login(request)
			return redirect(reverse('courses.views.index'))
		else:
			print student_form.errors
	else:
		student_form = StudentProfileForm()
	return redirect('/')

def profile(request):
	CLASS_YEAR = [
        ('fy', 'First Year'),
        ('so', 'Sophomore'),
        ('ju', 'Junior'),
        ('se', 'Senior'),
        ]
	context=RequestContext(request)
	student=Student.objects.get(user=request.user)
	user=request.user
	username=student.user.username
	classyear=student.class_year
	for c in CLASS_YEAR:
		if c[0] == classyear:
			classyear=c[1]
	gpa=student.gpa
	qrb=student.qrb_passed
	foreignlang=student.foreign_lang_passed
	multi=student.multi_passed
	primarymajor=student.primary_major.name
	if student.secondary_major:
		secondarymajor=student.secondary_major.name
	else:
		secondarymajor='None'
	
	return render_to_response(
		'courses/profile.html',
		{'username':username,
		'classyear':classyear,
		'primarymajor':primarymajor,
		'secondarymajor':secondarymajor,
		'gpa':gpa,
		'qrb':qrb,
		'foreignlang':foreignlang,
		'multi':multi
		},
		context
		)

def checklist(request):
	context=RequestContext(request)
	student=Student.objects.get(user=request.user)
	dists_todo=student.distributions_todo()
	#create list of fulfilled dists
	dists_completed = []
	for dist in Distribution.objects.all():
		if student.has_fulfilled_dist(dist):
			dists_completed.append(dist)
	#percentage of dists fulfilled
	percentage = float(len(dists_completed)/16)*100
	return render_to_response(
		'courses/checklist.html',
		{'dists_todo': dists_todo,
		'dists_completed': dists_completed,
		'percentage': percentage},
		context
		)

def load_mycourses(request):
	context = RequestContext(request)
	student = Student.objects.get(user=request.user)
	# for when user adds a new course
	if request.method == 'POST':
		course_form = AddCourseForm(request.POST)
		rating_form = AddCourseRatingForm(request.POST)
		if course_form.is_valid():
			code = course_form.cleaned_data['code']
			try: 
				course = Course.objects.get(code=code)
				student.add_course(course)
				student.save()
			except ValueError:
				return HttpRequestBadResponse("invalid course name")
			# not able to process rating information for some reason
		if rating_form.is_valid():
			score = rating_form.cleaned_data['score']
			text = rating_form.cleaned_data['comment_text']
			course_rating, created = CourseRating.objects.get_or_create(
				comment_author=student,
				comment_course=course
				)
			course_rating.score = score 
			course_rating.comment_text = text
			course_rating.save()

	courses = student.courses.all()
	course_reviews = CourseRating.objects.all().filter(comment_author=student)
	prof_reviews = ProfRating.objects.all().filter(comment_author=student)
	course_form = AddCourseRatingForm()
	return render_to_response(
	'courses/mycourses.html',
	{'add_course_form': AddCourseForm(),
	'add_course_rating_form': AddCourseRatingForm(),
	'courses': courses,
	'reviews': course_reviews,
	'prof_reviews': prof_reviews},
	context)

@require_http_methods(['POST'])
@csrf_exempt
def delete_course(request):
	course = Course.objects.get(code=request.POST['code'])
	print str(course)
	student = Student.objects.get(user=request.user)
	student.remove_course(course)
	print 'course removed'
	student.save()
	if request.is_ajax():
		return HttpResponse("")
	return reverse('courses.views.laod_mycourses')

#SCHEDULER METHODS
#for an individual section                                                             
def load_myschedule(request):
    context = RequestContext(request)
    #section_form = modelformset_factory(Section, form=SectionForm, max_num=5)
    return render_to_response('courses/schedule.html',
    	{'section_form': SectionForm(),},
    	context)
