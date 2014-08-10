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

#AUTHENTICATION METHODS
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

def register(request):
	print request.user
	context = RequestContext(request)
	profile_created = False
	if request.method == 'POST':
		student_form = StudentProfileForm(request.POST)
		if student_form.is_valid():
			#first create a user object
			username = student_form.cleaned_data['username'] + '@wellesley.edu'
 			password = student_form.cleaned_data['password']
			user = User.objects.create_user(username, username, password)
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

#MYCOURSES METHODS 
#ADDS COURSES AND COURSE REVIEWS FOR STUDENT
def load_mycourses(request):
	context = RequestContext(request)
	student = Student.objects.get(user=request.user)
	if request.method == 'POST':
		course_form = AddCourseForm(request.POST)
		rating_form = AddCourseRatingForm(request.POST)
		if course_form.is_valid():
			code = course_form.cleaned_data['code']
			try:
				#find course that student added  
				course = Course.objects.get(code=code)
				student.add_course(course)
				student.save()
			except ValueError:
				return HttpRequestBadResponse("invalid course name")
		if rating_form.is_valid():
			#process rating information
			score = rating_form.cleaned_data['score']
			text = rating_form.cleaned_data['comment_text']
			#create course review information or update accordingly
			course_rating, created = CourseRating.objects.get_or_create(
				comment_author=student,
				comment_course=course
				)
			course_rating.score = score 
			course_rating.comment_text = text
			course_rating.save()
	#retrieve courses and reviews associated with student
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

#WIP
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


#SCHEDULER METHODS
def load_myschedule(request):
	context = RequestContext(request)
	section_form = modelformset_factory(Section, form=SectionForm, max_num=5)
	qset = Section.objects.all()
	Section
	return render_to_response(
	'courses/schedule.html',
	{'section_form': section_form,},
	context)	
