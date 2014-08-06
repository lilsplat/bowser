from django.shortcuts import render
from courses.forms import *
from django.template import RequestContext
from django.shortcuts import render_to_response
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

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid():
		# Save the user's form data to the database.
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			registered = True
			#create student to correspond with user
			student = Student.objects.get_or_create(user=user)
        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
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
		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/courses/create_profile')
			else:
				return HttpResponseNotFound('<h1>Page not found</h1>')
		else:
			return HttpResponse('Invalid login')
	else:
		return render_to_response('courses/login.html/', {}, context)

def user_logout(request):
    logout(request)
    return render_to_response('courses/index.html')

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
	courses = student.courses.all()
	course_reviews = CourseRating.objects.all().filter(comment_author=student)
	course_form = AddCourseRatingForm()
	return render_to_response(
	'courses/mycourses.html',
	{'add_course_form': AddCourseForm(),
	'add_course_rating_form': AddCourseRatingForm(),
	'courses': courses,
	'reviews': course_reviews},
	context)

@require_http_methods(['POST'])
@login_required
def add_course(request):
	print 'starting'
	student = Student.objects.get(user=request.user)
	print student
	try:
		course = Course.objects.get(code=request.POST.get('code'))
		print course
	except ValueError:
		return HttpRequestBadResponse('Invalid course name')
	student.add_course(course)
	student.save()
	print 'student saved'
	if request.is_ajax():
		return HttpResponse("")
	return redirect('/courses/mycourses.html')
	
