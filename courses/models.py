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
'Lab',
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
        return list(set(l)) #remove duplicates

    """Returns a list of suggested courses to fulfill the Distribution, given a list of Courses"""
    def suggested_courses(self,courses):
        #additional functions: should compensate for fall/spring availability
        suggestions = self.course_codes() #all available courses
        for c in courses:
            if self.is_fulfilled_by(c):
                suggestions.remove(c.code)
        return suggestions

    class Meta:
        ordering = ['name']


class Course(models.Model):
    dept = models.CharField(max_length=200) #i.e. CS
    code = models.CharField(max_length=200) #i.e. CS110, aka course
    crn = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    credit_hours = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    addit_info = models.CharField(max_length=200)
    seats_available = models.CharField(max_length=200)
    max_enrollment = models.CharField(max_length=200)
    by_permission = models.CharField(max_length=200)
    prereq = models.CharField(max_length=200)
    notes = models.CharField(max_length=200)
    xlisted = models.CharField(max_length=200)
    prof = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    starttime = models.CharField(max_length=200)
    endtime = models.CharField(max_length=200)
    offered_in_fall = models.BooleanField(default=True)#temporary for fall2014
    offered_in_spring = models.BooleanField(default=False)

    dists = models.ManyToManyField(Distribution)

    def __unicode__(self):
        return self.code

    """Returns whether this Course has a time conflict with another Course"""
    def conflicts(self, other_course):
        try:
            if (self.starttime == other_course.starttime and self.date == other_course.date and self.endtime == other_course.endtime):
                return True
            else:
                return False
        except:
            raise Exception('please enter a valid course')

    """Returns whether this Course's enrollment is full"""
    def is_full(self):
        try:
            if (self.seats_available == self.max_enrollment):
                return True
            else:
                return False
        except:
            raise Exception('please enter a valid course')

    """Returns this Course's mean score based on its Ratings"""
    def avg_score(self):
        i=0.0
        a=0.0
        for s in self.rating_set.all():
            a+=s.score
            i+=1
        return a/i

    class Meta:
        ordering = ['code'] #orders courses by name


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
    qrb_passed = models.BooleanField(default=False) #if they passed the QR assessment
    foreign_lang_passed = models.BooleanField(default=False) #if they passed the foreign lang requirement

    def __unicode__(self):
        return self.user.username

    # def credit_hours_completed
	
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

    def distributions_todo(self):
        all_dists = DIST_REQ
        overlap_dists = OVERLAP_DIST_REQ
        dists_todo=[] #list to be returned

        """Check if foreign language and qrb is passed"""
        if self.foreign_lang_passed == False:
            all_dists = all_dists + LANG_REQ
        if self.qrb_passed == False:
            all_dists = all_dists + QRB_REQ

        """Copy all Student_courses info so we only query the db here"""
        course_dists=[] #tuple of (name,[dist_names])
        dist_freq={} #dictionary of distributions and their frequencies
        for c in self.courses.all(): #iterate through all courses
            c_dists=[]
            for d in c.dists.all(): #iterate through all c's dists
                c_dists.append(d.name) #and add each dist to c_dists list
                if d.name in dist_freq: #create and update dictionary
                    dist_freq[d.name]+=1
                else:
                    dist_freq[d.name]=1
            c_dists=(c.code,c_dists) #make c_dists a tuple including c's code for readability
            course_dists.append(c_dists) #add tuple to the list
        
        print 'unsorted dist_freq: '
        print dist_freq
       
        """Perform a non-destructive search to check for overlap courses"""
        #check fulfillment of qrf and lab
        if 'QR Overlay' in dist_freq:
            overlap_dists.remove('QR Overlay')
            print 'QR Overlay fulfilled by '
        if 'Lab' in dist_freq:
            overlap_dists.remove('Lab')
            print 'Lab fulfilled by '
        #check fulfillment of 300 levels
        try:
            if dist_freq['300-level'] >= 4:
                overlap_dists.remove('300-level')
                #remove all 300-level
                overlap_dists=filter(lambda y: y!='300-level', overlap_dists) 
                print '300-levels fulfilled'
            else:
                i=0
                while i < dist_freq['300-level']:
                    overlap_dists.remove('300-level')
                    i+=1
                print str(dist_freq['300-level']) + ' 300 levels done'
        except:
            #if exception caught, there are no 300 levels
            print 'No 300 levels taken'

        """Clean up dictionary"""
        #non-destructively remove 300 and qrf from dist_freq
        print'\nremoving 300 and qrf from dist_freq: '
        temp_dist_freq=dict(dist_freq)
        del temp_dist_freq['300-level']
        del temp_dist_freq['QR Overlay']
        #and reconstruct dictionary
        dist_freq=temp_dist_freq

        """Attempt to find all dist requirements by searching for the Student's  
        'rarest' dists first, through a course list organized by how 'specific'
        each Course's dists are. If a dist is found in the Student's course
        list, remove the dist from the list of all_dists. Finally, return
        the list of all_dists."""
        print '\nsorted dist_freq: '
        #sort dist_freq by frequency, least to most
        dist_freq=sorted(dist_freq,key=dist_freq.get)
        print dist_freq
        #sort course_dists by # of dists, least to most
        course_dists=sorted(course_dists,key=lambda c: len(c[1]))
        print '\nsorted course_dists: '
        print course_dists

        while len(dist_freq) > 0: #search through all dists that exist in the Student's course list
            d=dist_freq[0].encode('UTF-8') #always search for dist_freq[0]
            print 'searching for dist: ' + str(d)
            for c in course_dists: #iterate through Student's courses
                print 'reading: ' + str(c[0])
                if d in c[1]: #if d is found
                    print 'found ' + str(d) + ' in ' + str(c[0]) + '\n'
                    course_dists.remove(c) #remove course (no repeats)
                    all_dists.remove(d) #remove dist from list
                    break #stop loop
            dist_freq.remove(d) #remove this dist from all existing dists
        print '\ndists togo: ' 
        return all_dists+overlap_dists
        print '\n\ndone\n'
	
	# def major_todo(self):
	# 	major_course_list = primary_major.major_courses
	# 	for course in major_course_list:
	# 		if course in self.courses:
	# 			major_course_list.remove(course)
	# 	return major_course_list

    class Meta:
        unique_together=('primary_major','secondary_major')

#very similar to distribution
class CourseBucket(models.Model):
    name=models.CharField(max_length=200)
    #number of unique courses from this coursebucket needed for it to be fulfilled
    num_pick=models.IntegerField(default=1)
    courses=models.ManyToManyField(Course)
    major=models.ForeignKey('Major')

    def __unicode__(self):
        return self.name

    def is_fulfilled_by(self, course):
        return self.courses.filter(id=course.id).exists()
    
    def is_fulfilled(self,course_list):
        num_fulfilled=0
        for c in course_list:
            if self.is_fulfilled_by(c):
                num_fulfilled+=1
        if num_fulfilled >= self.num_pick:
            return True
        else:
            return False

    """Returns a readable list of unique Course.codes that fulfill this CourseBucket"""
    def course_codes(self):
        l=[]
        for c in self.courses.all():
            l.append(c.code.encode('UTF-8'))
        return list(set(l)) #remove duplicates

    """Returns a list of suggested courses to fulfill the CourseBucket, given a list of Courses"""
    def suggested_courses(self,course_list):
        #additional functions: should compensate for fall/spring availability
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
	
	# major_courses = Course.objects.filter(dept=self.name)
	#below methods are copied from the Distribution model.
    # """Returns if a course counts toward the Major"""
    # def is_fulfilled_by(self, course):
    #     return self.course_set.filter(id=course.id).exists()

    # """Returns a list of suggested courses to fulfill the Major, given a list of Courses"""
    # def suggested_courses(self,courses):
    #     #additional functions: should compensate for fall/spring availability
    #     suggestions = self.course_codes() #all available courses
    #     for c in courses:
    #         if self.is_fulfilled_by(c):
    #             suggestions.remove(c.code)
    #     return suggestions

class UserProfile(models.Model):
    # Links UserProfile to a User model instance.
    user = models.OneToOneField(User)
    # additional attributes we wish to include.
    email_verified = models.BooleanField()

    def __unicode__(self):
        return self.user.username

class Rating(models.Model):
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

    # class Meta:
    #     ordering = ['name'] #orders courses by name

