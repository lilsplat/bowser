from django.db import models

class Student(models.Model):
    FIRSTYEAR = 'fy'
    SOPHOMORE = 'so'
    JUNIOR = 'ju'
    SENIOR = 'se'
	# Feel free to change year abbreviations
    CLASS_YEAR = [
        (FIRSTYEAR, 'First year'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
        ]
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    class_year = models.CharField(max_length=5, choices=CLASS_YEAR, default=FIRSTYEAR)
    primary_major = models.ForeignKey('Major', related_name='primary major')
    secondary_major = models.ForeignKey('Major', related_name='secondary major')
    major_requirements_completed = models.BooleanField(default=False)
    distribution_requirements_completed = models.BooleanField(default=False)
    gpa = models.IntegerField()
    courses = models.ManyToManyField(Course, through='Enrollment')
   
    def add_course(self, course):
	""" Adds a course to a student's courses """
        try:
            self.courses.add(course)
        except:
            raise Exception('course could not be added.')
    
    def remove_course(self, course):
        try:
            self.courses.remove(course)
        except:
            raise Exception('course could not be removed.')

	def __unicode__(self):
		return self.first_name + ' ' + self.last_name	

class Course(models.Model):
    code = models.CharField() #i.e. CS110
    name = models.CharField() 
    time = models.CharField() #i.e. 1:30-4:00pm
    date = models.CharField() #i.e. TF
    prof = models.CharField()
    prof_site = models.CharField() #link to professor's website (comes on course browser)
    dist = models.ForeignKey('Distribution', related_name='distribution')
    comments = models.TextField()
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


class Course_Bucket(models.Model):
    name = models.CharField()
    courses = models.ManyToManyField(Course)

    def equals_course_named(self, course_name):
        if Course_Bucket.objects.filter(courses__name__startswith=course_name).count() > 0: 
            #there MUST be a better way to do this????
            return True
        else:
            return False

    #wasn't sure which method was more appropriate
    def equals_course(self, course):
        return self.equals_course_named(course.name)


class Major(models.Model):
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
    ]

    name = models.CharField(max_length=5, choices=MAJORS, default=UND)
    # courses = models.ManyToManyField(Course, through='Major_Requirements') 
    #^^^^^^ need to change

class Distribution(models.Model):
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

    name = models.CharField(max_length=5, choices=DISTRIBUTIONS, default=NONE)
    
    


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
    student = models.ForeignKey(Student)
    course = models.ForeignKey(Course)
    date_taken = models.DateField()
    rating = models.IntegerField(choices=RATINGS)
    

class Major_Requirements(models.Model):
    course = models.ForeignKey(Course)
    major = models.ForeignKey(Major)
    #can contain more info







    #TODO: Figure out how to represent courses in models
