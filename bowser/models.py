from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=200)
