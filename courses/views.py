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
    # get the request's context.
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
        # Erros that will also be shown to the user.
        else:
            print user_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()

    # Render the template depending on the context.
    return render_to_response(
            'courses/register.html',
            {'user_form': user_form, 'registered': registered},
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
				return redirect('/')
			else:
				return HttpResponseNotFound('<h1>Page not found</h1>')
		else:
			return HttpResponse('Invalid login')
	else:
		return render_to_response('courses/landing.html/', {}, context)

def user_logout(request):
    logout(request)
    return redirect('/')

def create_student_profile(request):
	print request.user
	context = RequestContext(request)
	profile_created = False
	if request.method == 'POST':
		student_form = StudentProfileForm(data=request.POST)
		if student_form.is_valid():
			student_data = student_form.save(commit=False)
			student = Student.objects.get(user=request.user)
			student.class_year = student_data.class_year
			student.primary_major = student_data.primary_major
			student.secondary_major = student_data.secondary_major
			student.gpa = student_data.gpa
			student.qrb_passed = student_data.qrb_passed
			student.save()
			profile_created = True
			return render_to_response('courses/index.html', context)
		else:
			print student_form.errors
	else:
		student_form = StudentProfileForm()
	return render_to_response(
		'courses/create_profile.html',
		{'student_form': student_form},  
		context)

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
