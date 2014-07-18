"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.utils import unittest
from django.test import TestCase
from courses.models import Course, Student, Distribution, Major, Enrollment
import datetime


class StudentTester(TestCase):
	fixtures = ['initial_data_dump.json']

	def setUp(self):
		Student.objects.create(
			email='lxie@wellesley.edu',
			first_name='lily',
			last_name='xie',
			class_year='ju',
			primary_major=Major.objects.get(name='Computer Science'),
			gpa=1.0
			)
		Student.objects.create(
			first_name='sravanti',
			last_name='tekumalla',
			# class_year=''
			primary_major=Major.objects.get(name='Sociology'),
			gpa=1.0
			)

	def test(self):
		lily = Student.objects.get(first_name='lily')
		print lily.email
		print lily.email.split('@')[0]
		print lily.username
		print lily.primary_major
		self.assertEqual('lily', lily.first_name)
		self.assertEqual('xie', lily.last_name)
		self.assertEqual('ju', lily.class_year)

		sravanti = Student.objects.get(first_name='sravanti')
		print sravanti.primary_major

		#arbitrarily gets first object in list b/c CS111-01
		cs111 = Course.objects.filter(code='CS111')[0]
		soc108 = Course.objects.filter(code__contains='SOC108')[0]

		e1 = Enrollment.objects.create(student=lily, course=cs111, date_taken=datetime.date.today(), rating=5)

		e2 = Enrollment.objects.create(student=sravanti,course=cs111,date_taken=datetime.date.today(),rating=5)

		print lily.courses
		print cs111.student_set.all()

		# for c in Course.objects.order_by('id'):
		# 	print (c.code)


class DistributionTester(TestCase):
	fixtures = ['initial_data_dump.json']


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



