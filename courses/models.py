from django.db import models
from django.contrib.auth.models import User

#------CLASS YEARS--------
FIRSTYEAR = 'fy'
SOPHOMORE = 'so'
JUNIOR = 'ju'
SENIOR = 'se'

#------DISTRIBUTIONS--------
AMTFV = "AMTFV"
EC = "EC"
HS = "HS"
LL = "LL"
MM = "MM"
NPS = "NPS"
QRB = "QRB"
QRF = "QRF"
REMP = "REMP"
SBA = "SBA"
NONE = "NONE"
LAB = "LAB"
FYS = "FYS"
W = "W" #fyw
LANG100 = "LANG100"
LANG200 = "LANG200"
LL_AMTFV = "LL_AMTFV"
EC_HS = "EC_HS"
HS_REMP = "HS_REMP"
MM_NPS = "MM_NPS"
ANY_300 = "ANY_300"

#multicultural requirement??

#------DISTRIBUTION REQUIREMENTS--------
LANG_REQ = [
    #------------can have overlap--------------------
    (LANG100, "Foreign Language 100L"), #perhaps to increase simplicity should these just include 
    (LANG100, "Foreign Language 100L"), #the ability to be fulfilled by 'passed the language req'?
    (LANG200, "Foreign Language 200L"),
    (LANG200, "Foreign Language 200L")
]

QRB_REQ = [
    (QRB, "Basic QR")
]

DIST_REQ = [
    #------------can have overlap--------------------
    (QRF, "QR Overlay"), #QR requirement
    (LAB, "Lab"),
    (ANY_300, "300-level"),
    (ANY_300, "300-level"),
    (ANY_300, "300-level"),
    (ANY_300, "300-level"),
    #------------------------------------------------
    (W, "First Year Writing"),
    #------------humanities dist area-----------------
    (LL, "Language and Literature"),
    (AMTFV, "Arts, Music, Theater, Film and Video"),
    (LL_AMTFV, "Language and Literature or Arts, Music, Theater, Film and Video"),
    #-----------social sciences dist area------------
    (SBA, "Social and Behavioral Analysis"),
    (EC_HS, "Epistemology and Cognition or Historical Studies"),
    (HS_REMP, "Historical Studies or Religion, Ethics, and Moral Philosophy"),
    #-----------math and science dist area------------
    (MM, "Mathematical Modeling"),
    (NPS, "Natural and Physical Sciences"),
    (MM_NPS, "Mathematical Modeling or Natural and Physical Sciences"),
 ]

#------MAJORS--------
AFR = "AFR"
AMST = "AMST"
ANTH = "ANTH"
ART = "ART"
ASTR = "ASTR"
BIOC = "BIOC"
BISC = "BISC"
CAMS = "CAMS"
CHEM = "CHEM"
CLSC = "CLSC"
CLST = "CLST"
CPLT = "CPLT"
CS = "CS"
EALC = "EALC"
ECON = "ECON"
EDUC = "EDUC"
ENG = "ENG"
ES = "ES"
FREN = "FREN"
GEOS = "GEOS"
GER = "GER"
HIST = "HIST"
ITST = "ITST"
JWST = "JWST"
MATH = "MATH"
MER = "MER"
MES = "MES"
MUS = "MUS"
NEUR = "NEUR"
PE = "PE"
PEAC = "PEAC"
PHIL = "PHIL"
PHYS = "PHYS"
POLS = "POLS"
PSYC = "PSYC"
QR = "QR"
REL = "REL"
RUSS = "RUSS"
SAS = "SAS"
SOC = "SOC"
SPAN = "SPAN"
THST = "THST"
WGST = "WGST"
WRIT = "WRIT"
OTHER = "OTHER"
UND = "Undecided"
#??
MES = "MES"
ARTH = "ARTH"
ARTS = "ARTS"
EALL = "EALL"
CLCV = "CLCV"
HEBR = "HEBR"
ITAS = "ITAS"



#------BEGIN MODELS--------





"""
Distribution todo:
- still working toward a better distribution model...how to correctly represent fulfillment of distribution??
- otherwise working
"""
class Distribution(models.Model):
    DISTRIBUTIONS = [
        (AMTFV, "Arts, Music, Theatre, Film, Video"),
        (EC, "Epistemology and Cognition"),
        (HS, "Historical Studies"),
        (LL, "Language and Literature"),
        (MM, "Mathematical Modeling"),
        (NPS, "Natural and Physical Sciences"),
        (QRB, "QRB"), #basic QR
        (QRF, "QRF"), #QR requirement
        (REMP, "Religion, Ethics, and Moral Philosophy"),
        (SBA, "Social and Behavioral Analysis"),
        (NONE, "None"),
        (LAB, "Lab"),
        (FYS, "First Year Seminar"),
    ]

    name = models.CharField(max_length=200, choices=DISTRIBUTIONS, default=NONE)
    #courses ok can be accessed by Distribution.course_set

    def __unicode__(self):
        return self.name

    """Returns if a course counts toward the Distribution"""
    def is_fulfilled_by(self, course):
        if self.course_set.filter(name__contains=course.name).count() > 0:
            return True
        else:
            return False

    # """Returns the number of courses left to take in the Distribution, given a list of Courses"""
    # def num_courses_togo(self, courses):
    #     num_togo = self.num_courses
    #     for course in courses:
    #         if self.is_fulfilled_by(course) == True:
    #             num_togo -= 1
    #     return num_togo

    """Returns a list of suggested courses to fulfill the Distribution, given a list of Courses"""
    def suggested_courses(self, courses):
        #additional functions: should compensate for fall/spring availability
        suggestions = Distributions.course_set.all() #all available courses
        for course in courses:
            if self.is_fulfilled_by(course):
                suggestions.remove(course)
        return suggestions

    def is_completed(self, courses):
        """Returns if the distribution is complete, based on the given list of Courses"""
        if self.num_courses_togo(courses) == 0:
            return True
        else:
            return False



"""
Course ok
"""
class Course(models.Model):
    code = models.CharField(max_length=200) #i.e. CS110
    dept = models.CharField(max_length=200)
    name = models.CharField(max_length=200) 
    time = models.CharField(max_length=200) #i.e. 1:30-4:00pm
    date = models.CharField(max_length=200) #i.e. TF
    prof = models.CharField(max_length=200)
    prof_site = models.CharField(max_length=200) #link to professor's website (comes on course browser)
    comments = models.TextField(null=True, blank=True)
    dists = models.ManyToManyField(Distribution)
    # A corrolary to dists, to keep track of which majors each course counts toward
    # majors = models.ManyToManyField(Major)

    def __unicode__(self):
        return course.code

    #students can be accessed through Course.student_set

    def conflicts(self, other_course):
        """Returns whether this Course has a time conflict with another Course"""
        try:
            if (self.time == other_course.time) and (self.date == other_course.date):
                return True
            else:
                return False
        except:
            raise Exception('please enter a valid course')

    class Meta:
        ordering = ['name'] #orders courses by name


"""Student todo:
- figure out if possible to make username = email.split('@')[0]
- how to remove a course??????? gah
"""
class Student(models.Model):
    CLASS_YEAR = [
        (FIRSTYEAR, 'First year'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
        ]
	#user object stores username, pw
    user = models.OneToOneField(User)
    email = models.EmailField(max_length=200)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    class_year = models.CharField(max_length=200, choices=CLASS_YEAR, default=FIRSTYEAR)
    primary_major = models.ForeignKey('Major', related_name='primary major', null=True)
    secondary_major = models.ForeignKey('Major', related_name='secondary major', null=True, blank=True) 
    major_requirements_completed = models.BooleanField(default=False)
    distribution_requirements_completed = models.BooleanField(default=False)
    gpa = models.IntegerField()
    courses = models.ManyToManyField('Course', through='Enrollment')

    qrb_passed = models.BooleanField(default=False) #if they passed the QR assessment
    foreign_lang_passed = models.BooleanField(default=False) #if they passed the foreign lang requirement

    def __unicode__(self):
        return self.first_name + ' ' + self.last_name
	
	def add_course(self, course):
		if course not in self.courses.all():
			enrollment = Enrollment(
				student=self,
				course=course,
				date_taken = None, #need to change this later
				rating = None
			)
			enrollment.save()
			return enrollment.save()
		else:
			#Course is already in student's course list
			return None
 
	def remove_course(self, course):
		enrollment = Enrollment.objects.get(
			student=self,
			course=course
		)
		enrollment.delete()
	
	# def distributions_todo(self):
	# # I'm thinking Distributions, courses and all our long lists will be in a SQL table
	# # So we don't have to have these lists as global vars
	# 	distributions_list = DISTRIBUTIONS
	# 	for distribution in distributions_list:
	# 		if not is_completed(distribution, self.courses):
	# 			distributions_list.remove(distribution)
	# 	return distributions_list

    def distributions_todo(self):
        distribution_list = DIST_REQ
        num_overlap = 6 #default num 'overlap' courses i.e. courses that  can count for multiple majors; always at head of list

        #modify distribution_list to suit Student
        """not sure if you can do this comparison...field may return 1 or 0 instead of True or False"""
        if foreign_lang_passed == False:
            distribution_list = LANG_REQ + distribution_list
            num_overlap += 4 #adding 4 lang classes to the overlap category at head of list
        if qrb_passed == False:
            distribution_list = distribution_list + QRB_REQ

        #copy Student's courses
        courses_taken = self.courses.all()

        #check fulfillment of all "overlap" dist
        for distribution in distribution_list[:num_overlap]:
            for course in courses_taken:
                if distribution.is_fulfilled_by(course):
                    # courses_taken.remove(course) no need to do this b/c it is overlap dist
                    distribution_list.remove(distribution)
                    num_overlap -= 1

        """NB: does not yet account for courses w/ multiple dists"""
        #check fulfillment of all other dists
        for distribution in distribution_list[num_overlap:]:
            for course in courses_taken:
                if distribution.is_fulfilled_by(course):
                    courses_taken.remove(course)
                    distribution_list.remove(distribution)

        return distribution_list

        """Possible solution to account for multiple dists commented out below"""
        # #first loop: check fulfillment of all dists, first 'fitting' all courses with only 1 distribution
        # #to a distribution
        # for distribution in distribution_list[num_overlap:]:
        #     for course in courses_taken:
        #         if distribution.is_fulfilled_by(course):
        #             if course.dists.count() > 1: #if course has multiple dists
        #                 #do nothing, table this course
        #             else:
        #                 courses_taken.remove(course)
        #                 distribution_list.remove(distribution)

        # #second loop: arbitrarily assign all multi-dist courses to the first dist they fit
        # for distribution in distribution_list[num_overlap:]:
        #     for course in courses_taken:
        #         if distribution.is_fulfilled_by(course):
        #             courses_taken.remove(course)
        #             distribution_list.remove(distribution)


	
	def major_todo(self):
		major_course_list = primary_major.major_courses
		for course in major_course_list:
			if course in self.courses:
				major_course_list.remove(course)
		return major_course_list


class Course_Bucket(models.Model):
    name = models.CharField(max_length=200)
    courses = models.ManyToManyField(Course)

    def equals_course_named(self, course_name):
        if Course_Bucket.objects.filter(courses__name__contains=course_name): 
            return True
        else:
            return False

    #wasn't sure which method was more appropriate
    def equals_course(self, course):
        return self.equals_course_named(course.name)

"""
Major ok
"""
class Major(models.Model):
    
    MAJORS = [
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
        #??? multidisciplinary/other majors and minors??
        (MES, 'Middle Eastern Studies'),
        (ARTH, 'Art History'),
        (ARTS, 'Studio Art'),
        (EALL, 'East Asian Language and Literature'),
        (CLCV, 'Classical Studies'),
        (HEBR, 'Jewish Studies'),
        (ITAS, 'Italian Studies')
    ]

    name = models.CharField(max_length=200, choices=MAJORS, default=UND)

    def __unicode__(self):
        return self.name
	
	major_courses = Course.objects.filter(dept=self.name)
	#below methods are copied from the Distribution model.
    # """Returns if a course counts toward the Major"""
    def is_fulfilled_by(self, course):
        if self.course_set.filter(name__contains=course.name).count() > 0:
            return True
        else:
            return False
        

    # """Returns the number of courses left to take in the Major, given a list of Courses"""
    # def num_courses_togo(self, courses):
    #     num_togo = self.num_courses
    #     for course in courses:
    #         if self.is_fulfilled_by(course) == True:
    #             num_togo -= 1
    #     return num_togo

    """Returns a list of suggested courses to fulfill the Major, given a list of Courses"""
    def suggested_courses(self, courses):

        #additional functions: should compensate for fall/spring availability
        suggestions = Distributions.course_set.all() #all available courses
        for course in courses:
            if self.is_fulfilled_by(course):
                suggestions.remove(course)
        return suggestions

    """Returns if the major is complete, based on the given list of Courses"""
    def is_completed(self, courses):
        if self.num_courses_togo(courses) == 0:
            return True
        else:
            return False


#intermediaries 

class Enrollment(models.Model):
    ONE_STAR = "ONE_STAR"
    TWO_STARS = "TWO_STARS"
    THREE_STARS = "THREE_STARS"
    FOUR_STARS = "FOUR_STARS"
    FIVE_STARS = "FIVE_STARS"

    RATINGS = [
        (ONE_STAR, 1),
        (TWO_STARS, 2),
        (THREE_STARS, 3),
        (FOUR_STARS, 4),
        (FIVE_STARS, 5)
    ]
    """
	SEMESTER_LIST = [
		'FALL 2010',
		'SPRING 2011',
		'FALL 2011',
		'SPRING 2012',
		'FALL 2012',
		'SPRING 2013',
		'FALL 2013',
		'SPRING 2014',
		'FALL 2014',
		'SPRING 2015',
		'FALL 2015',
		'SPRING 2016',
		'FALL 2016',
		'SPRING 2017',
		'FALL 2017',
		'SPRING 2018',
		'FALL 2018',
		'SPRING 2019',
		'FALL 2019',
		'SPRING 2020',
	]
    """
    student = models.ForeignKey(Student)
    course = models.ForeignKey(Course)
    date_taken = models.CharField(max_length=200, null=True, blank=True)
    rating = models.IntegerField(choices=RATINGS, null=True, blank=True)
	
    class Meta:
		unique_together = [('student', 'course')]

    #TODO: Figure out how to represent courses in models

#for user auth
class UserProfile(models.Model):
    # Links UserProfile to a User model instance.
    user = models.OneToOneField(User)
    # additional attributes we wish to include.
    email_verified = models.BooleanField()
    def __unicode__(self):
        return self.user.username
