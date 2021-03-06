from __future__ import division
from django.shortcuts import render
from courses.forms import *
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseBadRequest
from django.core.urlresolvers import reverse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
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
				return HttpResponseNotFound('<h1>Page not found</h1>')
		else:
			return redirect(reverse('courses.views.index')) 
	else:
		return redirect(reverse('courses.views.index')) 

def user_logout(request):
    logout(request)
    return redirect('/')

def about(request):
	context = RequestContext(request)
	if request.user.is_authenticated():
		return render_to_response('courses/about.html', context)
	else:
		print 'boo'
		return render_to_response('courses/about.html', context)


def create_student_profile(request):
	print request.user
	context = RequestContext(request)
	profile_created = False
	if request.method == 'POST':
		student_form = StudentProfileForm(request.POST)
		if student_form.is_valid():
			#first create a user object
			username = student_form.cleaned_data['username'] + '@wellesley.edu'
			password = student_form.cleaned_data['password_repeat']
			user = User.objects.create_user(username, username, password)
			print 'user created'
			print 'user: ' + str(user)
			# now create corresponding student object
			student, created  = Student.objects.get_or_create(user=user)
			student.save()
			profile_created = True
			#log in user before redirecting to home page
			user_login(request)
			return redirect(reverse('courses.views.load_mycourses'))
		else:
			return render_to_response(
			'courses/landing.html',
			{'errors': "Your passwords do not match!"}, context)


def profile(request):
	context=RequestContext(request)
	student=Student.objects.get(user=request.user)
	if request.method == "POST":
		profile_form = ProfileForm(request.POST)
		print profile_form
		print profile_form.is_valid()
		if profile_form.is_valid():
			student.class_year = profile_form.cleaned_data['class_year']
			student.gpa = profile_form.cleaned_data['gpa']
			student.qrb_passed = profile_form.cleaned_data['qrb_passed']
			student.foreign_lang_passed = profile_form.cleaned_data['foreign_lang_passed']
			student.multi_passed = profile_form.cleaned_data['multi_passed']
			student.save()
	else:
		profile_form = ProfileForm(initial=
					{'user': student.user,
					'class_year': student.class_year,
					'gpa': student.gpa,
					'qrb_passed': student.qrb_passed,
					'foreign_lang_passed': student.foreign_lang_passed,
					'multi_passed': student.multi_passed
					})
				
	return render_to_response(
		'courses/profile.html',
		{'profile_form': profile_form,
		'username': student.user.username},
		context)


def checklist(request):
	context=RequestContext(request)
	student=Student.objects.get(user=request.user)
	dists_todo=student.distributions_todo()
	NOT_COMPLETED='Not Completed'
	#create list of fulfilled dists
	dists_completed = []
	incomplete_dists = []
	for d in dists_todo:
		if NOT_COMPLETED not in d[1]:
			dists_completed.append(d)
		else:
			incomplete_dists.append(d)
		dists_todo.remove(d)
	print "dists_completed:"
	for dist in dists_completed:
		print dist
	percentage = float(len(dists_completed)/16)*100
	return render_to_response(
		'courses/checklist.html',
		{'dists_todo': dists_todo,
		'dists_completed': dists_completed,
		'incomplete_dists': incomplete_dists,
		'percentage': percentage},
		context
		)

def load_mycourses(request):
	context = RequestContext(request)
	student = Student.objects.get(user=request.user)
	# for when user adds a new course

	if request.method == 'POST':
		prof_form=AddProfForm(request.POST)
		rating_form = AddCourseRatingForm(request.POST)
		prof_rating_form = AddProfRatingForm(request.POST)
		code = request.POST.get('code')
		try: 
			course = Course.objects.get(code=code)
			student.add_course(course)
			student.save()
		except ValueError:
			return HttpRequestBadResponse("invalid course name")

		if rating_form.is_valid():
			course_score = rating_form.cleaned_data['course_score']
			course_text = rating_form.cleaned_data['course_comment_text']

			if CourseRating.objects.filter(
				comment_course__id=course.id
				).filter(
				course_comment_author__id=student.id
				).exists():
				return HttpResponseBadRequest('You have already entered a review for this course!')
			else:
				course_rating=CourseRating(
					course_score=course_score,
					course_comment_text=course_text
					)
				course_rating.course_comment_author=student
				course_rating.comment_course=course
				course_rating.save()
				
			# try:
			# 	course_rating, created = CourseRating.objects.get_or_create(
			# 		course_comment_author=student,
			# 		comment_course=course,
			# 		course_score=course_score,
			# 		course_comment_text=course_text
			# 		)
			# 	# course_rating.save()
			# except:
			# 	return HttpResponseBadRequest('You have already entered a review for this course!')

		if prof_form.is_valid():
			if prof_rating_form.is_valid():
				prof_score = prof_rating_form.cleaned_data['prof_score']
				prof_text = prof_rating_form.cleaned_data['prof_comment_text']
				prof=prof_form.cleaned_data['name']
				prof=Professor.objects.get(name=prof)

				if ProfRating.objects.filter(
					comment_professor__name=prof.name
					).filter(
					prof_comment_author__id=student.id
					).exists():
					return HttpResponseBadRequest('You have already entered a review for this professor!')

				else:
					prof_rating=ProfRating(
						prof_score=prof_score,
						prof_comment_text=prof_text
						)
					prof_rating.prof_comment_author=student
					prof_rating.comment_professor=prof
					prof_rating.save()
				# try:
				# 	prof_rating, created = ProfRating.objects.get_or_create(
				# 		prof_comment_author=student,
				# 		comment_professor=prof,
				# 		prof_comment_text=prof_text,
				# 		prof_score=prof_score
				# 		)
				# 	# prof_rating.save()
				# except:
				# 	return HttpResponseBadRequest('You have already entered a review for this professor!')
	
	courses = student.courses.all()
	course_reviews = CourseRating.objects.all().filter(course_comment_author=student)
	prof_reviews = ProfRating.objects.all().filter(prof_comment_author=student)
	

	return render_to_response(
	'courses/mycourses.html',
	{'add_course_form': AddCourseForm(),
	'add_prof_form': AddProfForm(),
	'add_prof_rating_form': AddProfRatingForm(),
	'add_course_rating_form': AddCourseRatingForm(),
	'courses': courses,
	'course_reviews': course_reviews,
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
	return reverse('courses.views.load_mycourses')

@require_http_methods(['POST'])
@csrf_exempt
def save_review(request):
	course = Course.objects.get(code=request.POST['code'])
	review_text = request.POST['review']
	print str(course)
	print review_text
	student = Student.objects.get(user=request.user)
	course_review = CourseRating.objects.get(
		course_comment_author=student,
		comment_course = course)
	course_review.course_comment_text = review_text
	course_review.save()
	print 'course updated'
	if request.is_ajax():
		return HttpResponse("")
	return reverse('courses.views.load_mycourses')

@require_http_methods(['POST'])
@csrf_exempt
def edit_username(request):
	student = Student.objects.get(user=request.user)
	student.user.username = request.POST['new_username']
	print student.user.username
	print 'username changed'
	student.save()
	if request.is_ajax():
		return HttpResponse("")
	return reverse('courses.views.profile')

# @require_http_methods(['POST'])
# @csrf_exempt
# def edit_profile(request):
# 	student = Student.objects.get(user=request.user)
# 	student.user.username = request.POST['new_username']
# 	print student.user.username
# 	print 'username changed'
# 	student.save()
# 	if request.is_ajax():
# 		return HttpResponse("")
# 	return reverse('courses.views.profile')

#SCHEDULER METHODS
#for an individual section                                                             
def load_myschedule(request):
    context = RequestContext(request)
    #section_form = modelformset_factory(Section, form=SectionForm, max_num=5)
    if request.method == 'POST':
		section_form = SectionForm(request.POST)
		if section_form.is_valid():
			sections_list = []
			sections_list.append(section_form.cleaned_data['course1'])
			sections_list.append(section_form.cleaned_data['course2'])
			sections_list.append(section_form.cleaned_data['course3'])
			sections_list.append(section_form.cleaned_data['course4'])
			sections_list.append(section_form.cleaned_data['course5'])
			print sections_list
			conflicts=''
			for s in sections_list:
				s_removed_list=[i for i in sections_list]
				s_removed_list.remove(s)
				if s.schedule_conflicts(s_removed_list) != 'No conflicts':
					conflicts+=s.schedule_conflicts(s_removed_list)+'\n'
					sections_list.remove(s)
			# conflicts = section_form.cleaned_data['course1'].schedule_conflicts(sections_list)			
			return render_to_response('courses/schedule.html',
			{'section_form': SectionForm(),
			'conflicts': conflicts},
			context)
    return render_to_response('courses/schedule.html',
		{'section_form': SectionForm(),},
		context)

def parse_dept(code):
	DEPARTMENTS = [
	(AFR, 'Africana Studies'),
	(AMST, 'American Studies'),
	(ANTH, 'Anthropology'),
	(ART, 'Art'),
	(ASTR, 'Astronomy'),
	(BIOC, 'Biological Chemistry'),
	(BISC, 'Biological Sciences'),
	(CAMS, 'Cinema and Media Studies'),
	(CHEM, 'Chemistry'),
	(CLSC, 'Cognitive and Linguistic Sciences'),
	(CLST, 'Classical Studies'),
	(CPLT, 'Comparative Literature'),
	(CS, 'Computer Science'),
	(EALC, 'East Asian Languages and Cultures'),
	(ECON, 'Economics'),
	(EDUC, 'Education'),
	(ENG, 'English'),
	(ES, 'Environmental Studies'),
	(FREN, 'French'),
	(GEOS, 'Geosciences'),
	(GER, 'German'),
	(HIST, 'History'),
	(ITST, 'Italian Studies'),
	(JWST, 'Jewish Studies'),
	(MATH, 'Mathematics'),
	(MER, 'Medieval Renaissance Studies'),
	(MES, 'Middle Eastern Studies'),
	(MUS, 'Music'),
	(NEUR, 'Neuroscience'),
	(PE, 'Physical Education'),
	(PEAC, 'Peace and Justice Studies'),
	(PHIL, 'Philosophy'),
	(PHYS, 'Physics'),
	(POLS, 'Political Science'),
	(PSYC, 'Psychology'),
	(QR, 'Quantitative Reasoning'),
	(REL, 'Religion'),
	(RUSS, 'Russian'),
	(SAS, 'South Asia Studies'),
	(SOC, 'Sociology'),
	(SPAN, 'Spanish'),
	(THST, 'Theatre Studies'),
	(WGST, 'Women and Gender Studies'),
	(WRIT, 'Writing'),
	(OTHER, 'Other'),
	(UND, 'Undecided'),
	(MES, 'Middle Eastern Studies'),
	(ARTH, 'Art History'),
	(ARTS, 'Studio Art'),
	(EALL, 'East Asian Language and Literature'),
	(CLCV, 'Classical Studies'),
	(HEBR, 'Jewish Studies'),
	(ITAS, 'Italian Studies')
	]

	for dept in DEPARTMENTS:
		if code == dept[0]:
			return dept[1]

#to search for courses
def browse(request):
	context = RequestContext(request)
	if request.method == 'POST':
		browser_form = BrowserForm(request.POST)
		if browser_form.is_valid():
			dept=browser_form.cleaned_data['dept']
			dept=parse_dept(dept) #parse code
			print "dept: " + dept
			dists=browser_form.cleaned_data['dists']
			print "dists: "
			for dist in  dists:
				print dist
			semester=browser_form.cleaned_data['semester']
			print "semester: " + str(semester)

			#establish queryset
			queryset=Section.objects.filter(semester=semester).filter(course__dept=dept)

			#test for dists and add valid sections to list
			sections=[]
			ratings = []
			for section in queryset:
				for dist in dists:
					if dist in section.course.dists.all():
						sections.append(section)
			sections=list(set(sections)) #remove duplicates
			print sections
			for section in sections:
				ratings.append(CourseRating.objects.filter(comment_course = section.course))
			return render_to_response('courses/scheduler.html',
			{'sections': sections,
			# 'courses': courses,
			'browser_form': BrowserForm()},
			context)
	return render_to_response('courses/scheduler.html',
		{'browser_form': BrowserForm(),},
		context)


""" REVIEWS """
def reviews(request):
	context = RequestContext(request)
	return render_to_response('courses/reviews.html', 
		{'course_form': AddCourseForm(),
		'prof_form': ProfForm()}, 
		context)

def browser_temp(request):
	context=RequestContext(request)
	return render_to_response('courses/browser.html',
		{context}
		)	

@csrf_exempt
def get_reviews(request):
	context = RequestContext(request)
	if request.method == 'POST':
		course_review_form = AddCourseForm(request.POST)
		prof_review_form = ProfForm(request.POST)
		code = ""
		course_reviews = []
		course_score = ""
		prof = ""
		prof_reviews = []
		prof_score = ""
		if course_review_form.is_valid():
			code = course_review_form.cleaned_data['code']
			course_reviews = CourseRating.objects.filter(comment_course=code)
			print 'course reviews: ' + str(course_reviews)
			course = Course.objects.get(code=code)
			print 'course: ' + str(course)
			course_score = Course.avg_score(course)
			print 'score: ' + str(course_score)
		if prof_review_form.is_valid():
			prof = prof_review_form.cleaned_data['prof']
			prof_reviews = ProfRating.objects.filter(comment_professor=prof)
			# print 'prof reviews: ' + str(prof_reviews)
			prof = Professor.objects.get(name=prof)
			# print 'prof: ' + str(prof)
			prof_score = Professor.avg_score(prof)
			# print 'score: ' + str(prof_score)
		return render_to_response('courses/reviews.html', 
			{'code': code,
			'course_reviews': course_reviews, 
			'course_score': course_score,
			'prof': prof,
			'prof_reviews': prof_reviews,
			'prof_score': prof_score, 
			'course_form': AddCourseForm(),
			'prof_form': ProfForm()}, 
			context)
	return render_to_response('courses/reviews.html', 
		{'course_form': AddCourseForm(),}, 
		context)	

