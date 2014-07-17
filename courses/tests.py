"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.utils import unittest
from django.test import TestCase
from courses.models import *
import datetime

cs = Major.objects.create(name='CS')

# class DistributionTester(TestCase):
# 	def setUp(self):


class StudentTester(TestCase):
	def setUp(self):
		# cs = Major.objects.create(name='CS')
		Student.objects.create(
			email='lxie@wellesley.edu',
			first_name='lily',
			last_name='xie',
			class_year='ju',
			primary_major=cs,
			gpa=1.0
			)
		Student.objects.create(
			first_name='sravanti',
			last_name='tekumalla',
			# class_year=''
			primary_major=Major.objects.create(name='CS'),
			gpa=1.0
			)
		Course.objects.create(code='cs111',name='Intro CS',time='1:00',
			date='MF',prof='rhys',prof_site='blah')
		Course.objects.create(code='soc100',name='Intro Soc',time='1:00',
			date='MF',prof='x',prof_site='blah')


	def test(self):
		lily = Student.objects.get(first_name='lily')
		print lily.email
		print lily.email.split('@')[0]
		print lily.username
		self.assertEqual('lily', lily.first_name)
		self.assertEqual('xie', lily.last_name)
		self.assertEqual('ju', lily.class_year)
		# self.assertEqual(Major.objects.create(name='CS'), lily.primary_major)


		sravanti = Student.objects.get(first_name='sravanti')
		cs111 = Course.objects.get(code='cs111')
		soc100 = Course.objects.get(code='soc100')

		e1 = Enrollment.objects.create(student=lily, course=cs111, date_taken=datetime.date.today(), rating=5)
		print e1.date_taken

		e2 = Enrollment.objects.create(student=sravanti,course=cs111,date_taken=datetime.date.today(),rating=5)

		# print lily.courses
		# print cs111.student_set.all()


class DistributionTester(TestCase):
	def setUp(self):
		Distribution.objects.create(name='mm')
		Distribution.objects.create(name='sba')
		Course.objects.create(code='cs111',name='Intro CS',time='1:00',
			date='MF',prof='rhys',prof_site='blah')
		Course.objects.create(code='soc100',name='Intro Soc',time='1:00',
			date='MF',prof='x',prof_site='blah')

	def test(self):
		mm = Distribution.objects.get(name='mm')
		sba = Distribution.objects.get(name='sba')
		cs111 = Course.objects.get(code='cs111')
		soc100 = Course.objects.get(code='soc100')
		cs111.dists.add(mm)
		soc100.dists.add(sba)

		courselist = [cs111, soc100]

		self.assertTrue(mm.is_fulfilled_by(cs111))
		self.assertTrue(sba.is_fulfilled_by(soc100))
		self.assertFalse(mm.is_fulfilled_by(soc100))
		self.assertFalse(sba.is_fulfilled_by(cs111))

		print mm.num_courses
		print mm.num_courses_togo(courselist)


