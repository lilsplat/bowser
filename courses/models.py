from django.db import models

class Student(models.Model):
	# Feel free to change year abbreviations
    CLASS_YEAR = [
        ('fy', 'First year'),
        ('so', 'Sophomore'),
        ('ju', 'Junior'),
        ('se', 'Senior'),
        ]
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    class_year = models.CharField(max_length=5, choices=CLASS_YEAR)
	# Currently commented out until Major foregin key is fully defined 
    #primary_major = models.ForeignKey(Major)
    #secondary_major = models.ForeignKey(Major)
    major_requirements_completed = models.BooleanField(default=False)
    distribution_requirements_completed = models.BooleanField(default=False)
    gpa = models.IntegerField()

class Major(models.Model):
    name = models.CharField(max_length=200)
    #TODO: Figure out how to represent courses in models
