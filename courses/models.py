from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count
from datetime import datetime

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
"Foreign Language Requirement"
]

QRB_REQ = [
"Basic QR"
]

# DIST_REQ = [
#     #------------can have overlap--------------------
#     (QRF, "QR Overlay"), #QR requirement
#     (LAB, "Lab"),
#     (ANY_300, "300-level"),
#     (ANY_300, "300-level"),
#     (ANY_300, "300-level"),
#     (ANY_300, "300-level"),
#     #------------------------------------------------
#     (W, "First Year Writing"),
#     #------------humanities dist area----------------
#     (LL, "Language and Literature"),
#     (AMTFV, "Arts, Music, Theater, Film and Video"),
#     (LL_AMTFV, "Language and Literature or Arts, Music, Theater, Film and Video"),
#     #-----------social sciences dist area------------
#     (SBA, "Social and Behavioral Analysis"),
#     (EC_HS, "Epistemology and Cognition or Historical Studies"),
#     (HS_REMP, "Historical Studies or Religion, Ethics, and Moral Philosophy"),
#     #-----------math and science dist area------------
#     (MM, "Mathematical Modeling"),
#     (NPS, "Natural and Physical Sciences"),
#     (MM_NPS, "Mathematical Modeling or Natural and Physical Sciences"),
#  ]


# DIST_REQ = [
#     #------------can have overlap--------------------
#     "QR Overlay", #QR requirement
#     "Lab",
#     #-----------can have overlap but no repeats------
#     "300-level",
#     "300-level",
#     "300-level",
#     "300-level",
#     #------------------------------------------------
#     "First Year Writing",
#     #------------humanities dist area----------------
#     "Language and Literature",
#     "Arts, Music, Theater, Film and Video",
#     "Language and Literature or Arts, Music, Theater, Film and Video",
#     #-----------social sciences dist area------------
#     "Social and Behavioral Analysis",
#     "Epistemology and Cognition or Historical Studies",
#     "Historical Studies or Religion, Ethics, and Moral Philosophy",
#     #-----------math and science dist area------------
#     "Mathematical Modeling",
#     "Natural and Physical Sciences",
#     "Mathematical Modeling or Natural and Physical Sciences"
#  ]
OVERLAP_DIST_REQ=[
    #------------can have overlap--------------------
    "QR Overlay", #QR requirement
    "Lab",
    #-----------can have overlap but no repeats------
    "300-level",
    "300-level",
    "300-level",
    "300-level"
]

DIST_REQ=[
# 'Lab',
"First Year Writing",
#------------humanities dist area----------------
"Language and Literature",
"Arts, Music, Theater, Film and Video",
"Language and Literature or Arts, Music, Theater, Film and Video",
#-----------social sciences dist area------------
"Social and Behavioral Analysis",
"Epistemology and Cognition or Historical Studies",
"Historical Studies or Religion, Ethics, and Moral Philosophy",
#-----------math and science dist area------------
"Mathematical Modeling",
"Natural and Physical Sciences",
"Mathematical Modeling or Natural and Physical Sciences"
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

#temporarily same as major list
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
        #??? multidisciplinary/other majors and minors??
        (MES, 'Middle Eastern Studies'),
        (ARTH, 'Art History'),
        (ARTS, 'Studio Art'),
        (EALL, 'East Asian Language and Literature'),
        (CLCV, 'Classical Studies'),
        (HEBR, 'Jewish Studies'),
        (ITAS, 'Italian Studies')
    ]



#------BEGIN MODELS--------

class Distribution(models.Model):
    name = models.CharField(max_length=200, default=NONE)

    def __unicode__(self):
        return self.name

    """Returns if a course counts toward the Distribution"""
    def is_fulfilled_by(self, course):
        return self.course_set.filter(id=course.id).exists()

    """Returns a readable list of unique Course.codes that fulfill this Distribution"""
    def course_codes(self):
        l=[]
        for c in self.course_set.all():
            l.append(c.code.encode('UTF-8'))
        return l #remove duplicates

    """Returns a QuerySet of Courses that fulfill this Distribution"""
    @property
    def suggested_courses(self):
        courses=Course.objects.filter(dists__name=self.name).order_by('?')[:10]
        return courses

    class Meta:
        ordering = ['name']

class Professor(models.Model):
    name=models.CharField(max_length=200)
    site=models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

    """Returns this Professor's mean score based on their ProfRating"""
    def avg_score(self):
        i=0.0
        a=0.0
        for s in self.profrating_set.all():
            a+=s.score
            i+=1
        return a/i

    class Meta:
        ordering=['name']

class TimeAndDate(models.Model):
    dates=models.CharField(max_length=200) #i.e. TF,W
    starttime=models.CharField(max_length=200) #i.e. 9:50 am
    endtime=models.CharField(max_length=200) #i.e. 11:00 am

    def __unicode__(self):
        return self.dates + ' ' + self.starttime + '-' + self.endtime

    """Returns dates as a list of days, i.e. MTuThW1 --> [M, Tu, Th, W1]"""
    def datelist(self):
        dlist=[]
        for i in self.dates:
            if i.isupper():
                dlist.append(i)
            else:
                dlist[len(dlist)-1]+=i
        return dlist

    """Returns whether this TimeAndDate has a time conflict with another TimeAndDate"""
    def conflicts(self, other_section):
        #check basic equality
        if self == other_section:
            return True
        #check overlapping date and time
        if set(self.datelist()).intersection(set(other_section.datelist())):
            #if start and end times are the same, there is overlap
            if ((self.starttime == other_section.starttime) and (self.endtime == other_section.endtime)):
                return True
            #otherwise, check inexact overlap
            this_start=datetime.strptime(self.starttime.encode('UTF-8'),'%I:%M')
            this_end=datetime.strptime(self.endtime.encode('UTF-8'),'%I:%M')
            other_start=datetime.strptime(other_section.starttime.encode('UTF-8'),'%I:%M')
            other_end=datetime.strptime(other_section.endtime.encode('UTF-8'),'%I:%M')
            if ((this_start < other_end) and (this_end > other_start)):
                return True
        #if none of this is true, there is no overlap, return false
        return False


class Semester(models.Model):
    SESSIONS=[
    ('Fall','Fall'),
    ('Spring','Spring'),
    ('Wintersession','Wintersession'),
    ('Summer I','Summer I'),
    ('Summer II','Summer II'),
    ('Archive','Archive') #temp
    ]
    session=models.CharField(max_length=200,choices=SESSIONS,default='Fall')
    year=models.IntegerField() #e.g. 2014
    #0000 for archive

    def __unicode__(self):
        return self.session + ' ' + str(self.year)

    class Meta:
        ordering = ['year']

class Section(models.Model):
    NONE='None assigned'
    sec_id=models.CharField(max_length=200,default=NONE)
    crn=models.CharField(max_length=200,default=NONE)
    seats_available=models.CharField(max_length=200,default=NONE)
    max_enrollment=models.CharField(max_length=200,default=NONE)
    prof=models.ForeignKey('Professor')
    timeanddate=models.ForeignKey('TimeAndDate')
    semester=models.ForeignKey('Semester')
    course=models.ForeignKey('Course')

    """Returns whether this Section's enrollment is full"""
    def is_full(self):
        try:
            if (self.seats_available == self.max_enrollment):
                return True
            else:
                return False
        except:
            raise Exception('please enter a valid course')

    """Returns whether this Section has a time conflict with another section"""
    def conflicts(self,other_section):
        return self.timeanddate.conflicts(other_section.timeanddate)

    def schedule_conflicts(self,section_list):
        # section_list=section_list.remove(self)
        for s in section_list:
            print s
            if self.conflicts(s):
                return str(s) + ',' + str(self)
        return 'No conflicts'

    def __unicode__(self):
		return str(self.course) + ': ' + self.prof.name  + ' | ' + self.timeanddate.__unicode__()
        #return 'prof: '+self.prof.name + ', section number: ' + self.sec_id + ', t&d:' + self.timeanddate.__unicode__()

class Course(models.Model):
    NONE='None assigned'
    dept=models.CharField(max_length=200,default=NONE,choices=DEPARTMENTS)
    #NB: all labs, disc, or conf courses have 'L' appended onto the code
    #of their main course, e.g. the lab of CS111's code is CS111L
    code=models.CharField(max_length=200,default=NONE)
    title=models.CharField(max_length=200,default=NONE)
    credit_hours=models.CharField(max_length=200,default=NONE)
    description=models.CharField(max_length=200,default=NONE)
    addit_info=models.CharField(max_length=200,default=NONE)
    by_permission=models.CharField(max_length=200,default=NONE)
    prereq=models.CharField(max_length=200,default=NONE)
    notes=models.CharField(max_length=200,default=NONE)
    xlisted=models.CharField(max_length=200,default=NONE)
    dists=models.ManyToManyField('Distribution')

    class Meta:
        ordering=['code']

    def __unicode__(self):
        return self.code

    """Returns this Course's mean score based on its CourseRating"""
    def avg_score(self):
        i=0.0
        a=0.0
        for s in self.courserating_set.all():
            a+=s.score
            i+=1
        return a/i

    """Returns a String list of Distribution names, excluding those with 'OR' for readabilitly"""
    def mycourses_dists(self):
        dist_names=[]
        for d in self.dists.all():
            if 'or' not in d.name:
                dist_names.append(d.name)
            if 'Historical Studies' in d.name:
                dist_names.append(d.name)
        return list(set(dist_names)) #get rid of duplicates

    """Returns all Professors that have ever taught this Course"""
    def all_profs(self):
        prof_list=[]
        for s in self.section_set.all():
            prof_list.append(s.prof)
        return prof_list

    """Returns all Sections for the current year"""
    def current_sections(self,current_session,current_year):
        sec_list=[]
        for s in self.section_set.all():
            if s.semester.session==current_session and s.semester.year==current_year:
                sec_list.append(s)
        return sec_list

    """Returns all Professors teaching in the current session and year"""
    def current_profs(self,current_session,current_year):
        current_secs=self.current_sections(current_session,current_year)
        prof_list=[]
        for s in current_secs:
            prof_list.append(s.prof)
        return prof_list



class Student(models.Model):
    CLASS_YEAR = [
        (FIRSTYEAR, 'First Year'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
        ]
	#user object stores username, pw, email
    user=models.OneToOneField(User, unique=True)
    class_year = models.CharField(max_length=200, choices=CLASS_YEAR, default=FIRSTYEAR)
    primary_major = models.ForeignKey('Major', related_name='primary major', null=True)
    secondary_major = models.ForeignKey('Major', related_name='secondary major', null=True, blank=True) 
    gpa = models.FloatField(default=2.0, null=True)
    courses = models.ManyToManyField('Course', null=True, blank=True)
    qrb_passed = models.BooleanField(default=False, verbose_name="Passed the QR assessment test?") #if they passed the QR assessment
    foreign_lang_passed = models.BooleanField(default=False, verbose_name="Passed the Foreign Language requirement?") #if they passed the foreign lang requirement
    multi_passed = models.BooleanField(default=False, verbose_name="Passed the Multicultural requirement?") #if they passed the Multicultural requirement

    def __unicode__(self):
        return self.user.username

    """Returns whether a Student has fulfilled a particular Distribution"""
    def has_fulfilled_dist(self,dist):
        for c in self.courses.all():
            if dist.is_fulfilled_by(c):
                return True
        return False
	
    """Adds a Course to Student.courses iff the Course does not already exist"""
    def add_course(self, course):
        if course not in self.courses.all():
			self.courses.add(course)
			self.save()

    """Removes a Course from Student.courses iff the Course exists"""
    def remove_course(self, course):
		if course in self.courses.all():
			self.courses.remove(course)
			self.save()
		else:
			raise Exception('Course not in studen\'s list')

    """Returns every CourseRating and ProfRating a Student has authored"""
    def get_ratings(self):
        profratings=[]
        courseratings=[]
        for p in self.profrating_set.all():
            profratings.append(p)
        for c in self.courserating_set.all():
            courseratings.append(c)
        return profratings+courserating

    """Returns a String list representation of Student's Distributions regardless of completion"""
    def all_dist_list(self):
        #NB does not include foreign language
        all_dists = DIST_REQ #Copy list of all distribution requirements
        if self.qrb_passed == False:
            #if not passed, add QRB_REQ to list of reqs to be checked
            all_dists = all_dists + QRB_REQ
        return all_dists

    """Returns a copied list of Student.courses.dists based on how frequently they appear in Student.courses"""
    def most_freq_dists(self):
        #First, create faux 'dictionary' of existing dist. names and their frequencies
        dists_dict=[] #contains tuples (distname,frequency)
        for distname in DIST_REQ+QRB_REQ:
            d=self.courses.filter(dists=Distribution.objects.get(name=distname))
            if d.exists():
                dists_dict.append((distname,d.count()))
        #Sort dictionary by frequency
        dists_dict=sorted(dists_dict,key=lambda c: c[1])
        #Use dictionary as a guide to fill search_dists with ordered Distribution objects
        search_dists=[]
        for d in dists_dict:
            search_dists.append(Distribution.objects.get(name=d[0]))
        return search_dists

    """Returns a copied list of Student.courses sorted by how many Distributions they fulfill"""
    def most_dist_courses(self):
        course_dist=self.courses.annotate(num_dists=Count('dists')).order_by('-num_dists')
        #Copy Course objects into list
        course_dist_freq=[]
        for c in course_dist:
            course_dist_freq.append(c)
        return course_dist_freq

    """Returns a list of tuples (Distribution name,Course if completed/Not Completed if not completed)"""
    def distributions_todo(self):
        all_dists = self.all_dist_list() #Copy list of all distribution requirements
        dists_todo=[] #Initialize list to be returned
        NOT_COMPLETED='Not Completed'

        #Initialize QuerySet
        self_courses=self.courses.all()
        #Check if Student has courses
        #If so, create cache
        if self_courses: 
            #Non-destructively check overlap courses 
            #Initialize overlap QuerySets
            lab=self_courses.filter(dists=Distribution.objects.get(name='Lab'))
            qrf=self_courses.filter(dists=Distribution.objects.get(name='QR Overlay'))
            tl=self_courses.filter(dists=Distribution.objects.get(name='300-level'))

            #check lab
            if lab.exists():
                dists_todo.append((Distribution.objects.get(name='Lab'),lab[0].code))
            else:
                dists_todo.append((Distribution.objects.get(name='Lab'),NOT_COMPLETED))

            #check qrf
            if qrf.exists():
                dists_todo.append((Distribution.objects.get(name='QR Overlay'),qrf[0].code))
            else:
                dists_todo.append((Distribution.objects.get(name='QR Overlay'),NOT_COMPLETED))

            #check 4x300-levels
            if tl.exists():
                #calculate number of 300-levels completed
                if len(tl) > 4:
                    num_tl=4 #limit count to max of 4
                else:
                    num_tl=len(tl)
                i=0
                while i<num_tl: #add completed 300-levels
                    dists_todo.append((Distribution.objects.get(name='300-level'),tl[i].code))
                    i+=1
                for x in xrange(0,4-num_tl): #add non-complete 300-levels
                    dists_todo.append((Distribution.objects.get(name='300-level'),NOT_COMPLETED))

            #Organize a list of Distributions by how frequently they appear in a Student's courses
            search_dists=self.most_freq_dists()
            #Organize a list of Student's Courses by how many Distributions they contain
            course_dist_freq=self.most_dist_courses()

            #Using search_dists and course_dist_freq, iterate through self_courses and determine which Courses fulfill which Distributions
            # print 'starting to search.....'
            for d in search_dists:
                # print 'searching for ' + d.name
                for c in course_dist_freq:
                    # print '\t' + c.code
                    if d.is_fulfilled_by(c): #if found
                        # print '\tFOUND: ' + c.code + ' fulfills ' + d.name
                        dists_todo.append((Distribution.objects.get(name=d.name),c.code))
                        all_dists.remove(d.name)
                        course_dist_freq.remove(c) #no overlaps
                        break #stop loop

        #Last step, clean up and add all unfulfilled Distributions to list as 'Not Completed'
        if self.foreign_lang_passed == False:
            dists_todo.append((Distribution.objects.get(name='Foreign Language'),NOT_COMPLETED))
        else:
            dists_todo.append((Distribution.objects.get(name='Foreign Language'),'Complete'))
        for d in all_dists:
            dists_todo.append((Distribution.objects.get(name=d),NOT_COMPLETED))

        return dists_todo

    class Meta:
        unique_together=('primary_major','secondary_major')

#very similar to distribution
class CourseBucket(models.Model):
    name=models.CharField(max_length=200)
    #number of unique courses from this coursebucket needed for it to be fulfilled
    num_pick=models.IntegerField(default=1)
    courses=models.ManyToManyField('Course')
    major=models.ForeignKey('Major')
    manual_completion=models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

    def is_fulfilled_by(self, course):
        return self.courses.filter(id=course.id).exists()
    
    def is_fulfilled(self,course_list):
        #check if manual completion is True
        if manual_completion:
            return True
        #else, check fulfillment 
        num_fulfilled=0
        for c in course_list:
            if self.is_fulfilled_by(c):
                num_fulfilled+=1
            if num_fulfilled >= self.num_pick:
                return True
        #if none of the above is true, return false
        return False

    """Returns a readable list of unique Course.codes that fulfill this CourseBucket"""
    def course_codes(self):
        #if there are no courses, ask student to consult the dept page
        if self.courses.all().count() == 0:
            manual_message='Please consult ' + self.major.name + '\'s department page for more information.'
            return [manual_message]
        #else, create list
        l=[]
        for c in self.courses.all():
            l.append(c.code.encode('UTF-8'))
        return list(set(l)) #remove duplicates

    """Returns a list of suggested courses to fulfill the CourseBucket, given a list of Courses"""
    def suggested_courses(self,course_list):
        #additional functions: should compensate for fall/spring availability
        #if there are no courses, ask student to consult the dept page
        if self.courses.all().count() == 0:
            manual_message='Please consult ' + self.major.name + '\'s department page for more information.'
            return [manual_message]
        #else, create list
        suggestions=self.course_codes() #all available courses
        for c in course_list:
            if self.is_fulfilled_by(c) and c.code in suggestions: #don't try to remove twice
                suggestions.remove(c.code)
        return suggestions

class Major(models.Model):
    code = models.CharField(max_length=200, default="UND")
    name = models.CharField(max_length=200, default=UND)
    is_minor = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name'] #orders courses by name

    def is_fulfilled(self,course_list):
        for cb in self.coursebucket_set.all():
            if not cb.is_fulfilled(course_list):
                return False
        return True

    def cbs_togo(self,course_list):
        togo=[]
        for cb in self.coursebucket_set.all():
            if not cb.is_fulfilled(course_list):
                togo.append(cb.name)
        return togo

    def suggested_cbs_togo(self,course_list):
        togo=[]
        for cb in self.coursebucket_set.all():
            if not cb.is_fulfilled(course_list):
                togo.append((cb.name,cb.suggested_courses(course_list)))
        return togo
	
	
class UserProfile(models.Model):
    # Links UserProfile to a User model instance.
	user = models.OneToOneField(User)
    # additional attributes we wish to include.
	email_verified = models.BooleanField()
	
	def __unicode__(self):
		return self.user.username

class CourseRating(models.Model):
    SCORES=[
    (1, 'One star'),
    (2, 'Two stars'),
    (3, 'Three stars'),
    (4, 'Four stars'),
    (5, 'Five stars')
    ]
    score = models.IntegerField(choices=SCORES,default=5)
    comment_text = models.CharField(max_length=10000,null=True,blank=True)
    comment_author = models.ForeignKey('Student')
    comment_course = models.ForeignKey('Course')

    def __unicode__(self):
		return str(self.comment_course) + ' | ' + str(self.comment_author)

    class Meta:
        unique_together = ("comment_author", "comment_course")
    

class ProfRating(models.Model):
    SCORES=[
    (1, 'One star'),
    (2, 'Two stars'),
    (3, 'Three stars'),
    (4, 'Four stars'),
    (5, 'Five stars')
    ]
    score = models.IntegerField(choices=SCORES,default=5)
    comment_text = models.CharField(max_length=10000,null=True,blank=True)
    comment_author = models.ForeignKey('Student')
    comment_professor=models.ForeignKey('Professor')

    def __unicode__(self):
		return str(self.comment_professor) + ' | ' + str(self.comment_author)
   
    class Meta:
        unique_together = ("comment_author", "comment_professor")




