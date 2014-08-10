from django.shortcuts import render
from courses.forms import *
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from courses.models import Student

def index(request):
    return render(request, 'courses/index.html')

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
		password = request.POST['password']
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
		return render_to_response('courses/landing.html/', {'register_form':StudentProfileForm()}, context)

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
			#student_data = student_form.save(commit=False)
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
			return redirect('/') 
		else:
			print student_form.errors
	else:
		student_form = StudentProfileForm()
	return redirect('/')

def checklist(request):
	context=RequestContext(request)
	student=Student.objects.get(user=request.user)
	dists_todo=student.distributions_todo()
	# return HttpResponse("")
	return render_to_response(
		'courses/checklist.html',
		{'ds': ds,
		'cs': cs,
		'dists_todo': dists_todo},
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
def delete_course(request):
	path = request.path
	print path
	course = Course.objects.get(code=request.POST['code'])
	student = Student.objects.get(user=request.user)
	student.remove_course(course)
	student.save()
	if request.is_ajax():
		return HttpResponse("")
	return redirect('/mycourses')
