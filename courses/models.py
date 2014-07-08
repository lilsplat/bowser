from django.db import models

"""
LX 7/8:
minor changes to Student:
    added default class year (first year)
    defined constants
    added manytomany relationship to courses through Enrollment

Major:
    copied major list from scraped course catalog with some regex magic
    I think majors and minors should both be included in Major (atm I've only added official majors but we can
    add minors too) (also interdisciplinary majors? Idk i just put in 'other')
    established ManyToMany relationship with courses (see Major_Requirements)

Course:
    established manytomany relationship with students through Enrollment
    established ManyToMany relationship with majors (see Major_Requirements)
    still unfamiliar with Django - if we want our Course to /not/ be dynamic, i.e. we want to
    pull from our static course catalog database, how would we do that?

Enrollment:
    intermediate model to govern manytomany relationship between Student and Course 
    NB: obviously I am new to Django and i'm not all sure if this is an appropriate 
    solution - what do you think? The complexity is that we would want to make a 
    model with multiple foreign keys - that is, a Course will have relationships with
    Students and Students will have relationships with Courses, which is specified through
    the through_fields parameter. I'm _pretty_ sure this is correct but i'm not 100 on the syntax.
    At least this is what I want it to do....
    example:
        lily = Student.objects.create(name="Lilz")
        sravanti = Student.objects.create(name="Sravantea")
        cs242 = Course.objects.create(name="Netwerks")
        e = Enrollment(student=lily, course=cs242, date_joined=date(2014, 1, 1))
        e2 = Enrollment(student=sravanti, course=cs242, date_joined=date(2014, 1, 1))
        cs242.members.all() #[<Student: Lilz>, <Student: Sravantea>]
        ####this is the part I'm not 100 sure on#####
        cs111 = Course.objects.create(name="Intro")
        e3 = Enrollment(student=lily, course=cs111, date_joined=date(2013, 1, 1))
        lily.courses.all() #[<Course: Netwerks>, <Course: Intro>]


Major_Requirements:
    performs a very similar function to Enrollment, but it mediates Courses and Majors
    (i.e. what Majors a Course counts for, and what Courses factor into a Major)

TODO: 
    establish relationship between courses and distribution requirements
    testing relationships
    flesh out Course
    maybe a script to read from course catalog data and create Courses

"""

class Student(models.Model):
    FIRSTYEAR = 'fy'
    SOPHOMORE = 'so'
    JUNIOR = 'ju'
    SENIOR = 'se'
    CLASS_YEAR = [
        (FIRSTYEAR, 'First year'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
        ]
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    class_year = models.CharField(max_length=5, choices=CLASS_YEAR, default=FIRSTYEAR)
    #primary_major = models.ForeignKey(Major)
    #secondary_major = models.ForeignKey(Major)
    major_requirements_completed = models.BooleanField(default=False)
    distribution_requirements_completed = models.BooleanField(default=False)
    gpa = models.IntegerField()
    courses = models.ManyToManyField(Course, through='Enrollment', through_fields=('student', 'courses'))

class Course(models.Model):
    name = models.CharField(max_length=200)
    students = models.ManyToManyField(Student, through='Enrollment', through_fields=('course', 'student'))
    counts_toward_major = models.ManyToManyField(Major, through='Major_Requirements', through_fields=('course', 'major'))
    #similar counts_toward_ditribution

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
        (AFR, 'Africana Studies')
        (AMST, 'American Studies')
        (ANTH, 'Anthropology')
        (ART, 'Art')
        (ASTR, 'Astronomy')
        (BIOC, 'Biological Chemistry')
        (BISC, 'Biological Sciences')
        (CAMS, 'Cinema and Media Studies')
        (CHEM, 'Chemistry')
        (CLSC, 'Cognitive and Linguistic Sciences')
        (CLST, 'Classical Studies')
        (CPLT, 'Comparative Literature')
        (CS, 'Computer Science')
        (EALC, 'East Asian Languages and Cultures')
        (ECON, 'Economics')
        (EDUC, 'Education')
        (ENG, 'English')
        (ES, 'Environmental Studies')
        (FREN, 'French')
        (GEOS, 'Geosciences')
        (GER, 'German')
        (HIST, 'History')
        (ITST, 'Italian Studies')
        (JWST, 'Jewish Studies')
        (MATH, 'Mathematics')
        (MER, 'Medieval Renaissance Studies')
        (MES, 'Middle Eastern Studies')
        (MUS, 'Music')
        (NEUR, 'Neuroscience')
        (PE, 'Physical Education')
        (PEAC, 'Peace and Justice Studies')
        (PHIL, 'Philosophy')
        (PHYS, 'Physics')
        (POLS, 'Political Science')
        (PSYC, 'Psychology')
        (QR, 'Quantitative Reasoning')
        (REL, 'Religion')
        (RUSS, 'Russian')
        (SAS, 'South Asia Studies')
        (SOC, 'Sociology')
        (SPAN, 'Spanish')
        (THST, 'Theatre Studies')
        (WGST, 'Women and Gender Studies')
        (WRIT, 'Writing')
        (OTHER, 'Other')
        (UND, 'Undecided')
    ]

    name = models.CharField(max_length=5, choices=MAJORS, default=UND)
    courses = model.ManyToManyField(Course, through='Major_Requirements', through_fields('major', 'course'))

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
        (AMTFV, "Arts, Music, Theatre, Film, Video")
        (EC, "Epistemology and Cognition")
        (HS, "Historical Studies")
        (LL, "Language and Literature")
        (MM, "Mathematical Modeling")
        (NPS, "Natural and Physical Sciences")
        (QRB, "QRB") #basic QR
        (QRF, "QRF") #QR requirement
        (REMP, "Religion, Ethics, and Moral Philosophy")
        (SBA, "Social and Behavioral Analysis")
        (NONE, "None")
        (LAB, "Lab")
        (FYS, "First Year Seminar")
    ]

    name = models.CharField(max_length=5, choices=DISTRIBUTIONS, default=NONE)
    


#intermediaries 

class Enrollment(models.Model):
    student = models.ForeignKey(Student)
    course = models.ForeignKey(Course)
    date_taken = models.DateField() 
    #can contain more info

class Major_Requirements(model.Model):
    course = models.ForeignKey(Course)
    major = models.ForeignKey(Major)
    #can contain more info







    #TODO: Figure out how to represent courses in models
