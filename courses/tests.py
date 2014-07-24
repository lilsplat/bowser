# TODO:
# - Test Distribution
# - Fill out major, test Major
# - Test Student.distributions_todo, num_distributions todo?
# - Test Student.major_todo
# - 



from django.utils import unittest
from django.test import TestCase
# from test_utils import 
from django.contrib.auth.models import User
from courses.models import Course, Student, Distribution, Major, Rating
import datetime


class StudentTester(TestCase):
	fixtures = ['initial_data_dump_072314.json']

	def setUp(self):
		lx_user=User.objects.create_user('lxie','lxie@wellesley.edu','lilypassword')
		st_user=User.objects.create_user('stekumalla','stekumalla@wellesley.edu','sravantipassword')
		Student.objects.create(
			user=lx_user,
			class_year='ju',
			primary_major=Major.objects.get(name='Computer Science'),
			gpa=1.0,
			qrb_passed=False,
			# foreign_lang_passed=False
			)
		Student.objects.create(
			user=st_user,
			primary_major=Major.objects.get(name='Computer Science'),
			secondary_major=Major.objects.get(name='Sociology'),
			gpa=1.0,
			qrb_passed=True,
			# foreign_lang_passed=False
			)
		Rating.objects.create(
			comment_text = "yay this course rocks my socks off!",
			comment_author = Student.objects.get(user=lx_user),
			comment_course=Course.objects.filter(code='CS111')[0]
			)
		Rating.objects.create(
			comment_text = "eh, this course could have been better. maybe if i didn't fall asleep in class each day...",
			comment_author = Student.objects.get(user=st_user),
			comment_course=Course.objects.filter(code='CS111')[0]
			)
		Rating.objects.create(
			comment_text = "this course sucked. never again, never again.",
			comment_author = Student.objects.get(user=lx_user),
			comment_course=Course.objects.filter(code='CS307')[0]
			)

	def test(self):

		"""TEST USER FIELDS"""
		sravanti_object = User.objects.get(username='stekumalla')
		lily_object = User.objects.get(username='lxie')
		sravanti_object.save()
		lily_object.save()
		lily = Student.objects.get(user=lily_object)
		sravanti = Student.objects.get(user=sravanti_object)
		lily.save()
		sravanti.save()

		self.assertEqual('lxie',lily.user.username)
		self.assertEqual('stekumalla',sravanti.user.username)
		self.assertEqual('lxie@wellesley.edu',lily.user.email)
		self.assertEqual('stekumalla@wellesley.edu',sravanti.user.email)
		#password should be encrypted
		self.assertNotEqual('lilypassword',lily.user.password)
		self.assertNotEqual('sravantipassword',sravanti.user.password)

		"""TEST USER.NAME"""
		lily_object.first_name='Lily'
		lily_object.last_name='Xie'
		lily_object.save()
		lily.user = lily_object #why do i need to reassign????
		lily.save()

		sravanti_object.first_name='Sravanti'
		sravanti_object.last_name='Tekumalla'
		sravanti_object.save()
		sravanti.user = sravanti_object
		sravanti.save()

		self.assertEqual('Lily',lily_object.first_name)
		self.assertEqual('Lily',lily.user.first_name)
		self.assertEqual('Tekumalla',sravanti_object.last_name)
		self.assertEqual('Tekumalla',sravanti.user.last_name)

		"""TEST STUDENT FIELDS"""
		self.assertEqual('ju', lily.class_year)
		self.assertEqual(1.0, lily.gpa)
		self.assertEqual(Major.objects.get(name='Computer Science'),lily.primary_major)
		self.assertFalse(lily.qrb_passed)

		self.assertEqual(Major.objects.get(name='Sociology'),sravanti.secondary_major)
		self.assertTrue(sravanti.qrb_passed)
		#still need to test nullable fields

		"""TEST ADDING AND REMOVING COURSES"""
		#nb: in the future this should be improved!!!!
		astr206=Course.objects.filter(code='ASTR206')[0] #qr
		cs307=Course.objects.filter(code='CS307')[0] #300 level
		writ170=Course.objects.filter(code='WRIT170')[0] #fyw
		amst268=Course.objects.filter(code='AMST268')[0] #lang and lit
		arth100=Course.objects.filter(code='ARTH100')[0] #arts
		soc108=Course.objects.filter(code='SOC108')[0] #sba
		cs322=Course.objects.filter(code='CS322')[0] #epistemology
		phil106=Course.objects.filter(code='PHIL106')[0] #epistemology
		wgst220=Course.objects.filter(code='WGST220')[0] #history
		cs111=Course.objects.filter(code='CS111')[0] #math
		astr100=Course.objects.filter(code='ASTR100')[0] #nps

		lily.add_course(astr206)
		lily.add_course(cs307)
		lily.add_course(writ170)
		lily.add_course(amst268)
		lily.add_course(arth100)
		lily.add_course(soc108)
		lily.add_course(cs322)
		lily.add_course(phil106)
		lily.add_course(wgst220)
		lily.add_course(cs111)
		lily.add_course(astr100)
		lily.save()

		self.assertEqual(11,lily.courses.count())
		self.assertEqual('ASTR206',lily.courses.filter(code='ASTR206')[0].code)

		lily.remove_course(arth100)
		lily.remove_course(astr100)
		lily.save()

		self.assertEqual(9,lily.courses.count())

		# lily.distributions_todo()

		""" TEST COMMENTS """
		#should move this to its own class duhhhh
		good_comment=Rating.objects.get(id=1)
		print good_comment.comment_text

		mediocre_comment=Rating.objects.get(id=2)
		print mediocre_comment.comment_text

		bad_comment=Rating.objects.get(id=3)
		print bad_comment.comment_text

		good_comment.save()
		mediocre_comment.save()
		bad_comment.save()
		
		print cs111.rating_set.all()
		print cs307.rating_set.all()
		print lily.rating_set.all()[0].comment_text
		
			
class CourseTester(TestCase):
	fixtures=['initial_data_dump_072314.json']

	def setUp(self):
		Course.objects.create(
			code='test100',
			dept='Computer Science',
			name='Amen 2 Testing',
			time='1:00-4:00PM',
			date='TF',
			prof='Meek Mill',
			prof_site='When they test me i just pee rose'
			# offered_in_fall=True,
			# offered_in_spring=False
			)
		Course.objects.create(
			code='test300',
			dept='Computer Science',
			name='3hunnatest',
			time='1:00-4:00PM',
			date='TF',
			prof='Dr Sosa',
			prof_site='Bang bang it\'s macaroni time'
			# offered_in_fall=True,
			# offered_in_spring=False
			)
		Course.objects.create(
			code='test200',
			dept='Computer Science',
			name='blah',
			time='9:50-11:00AM',
			date='TF',
			prof='Dr Sosa',
			prof_site='Bang bang it\'s macaroni time'
			# offered_in_fall=True,
			# offered_in_spring=False
			)

	def test(self):
		"""INITIALIZE"""
		test100=Course.objects.filter(code='test100')[0]
		test200=Course.objects.filter(code='test200')[0] #solely for testing conflicts
		test300=Course.objects.filter(code='test300')[0]
		test100.dists.add(Distribution.objects.get(id=14))
		test100.dists.add(Distribution.objects.get(id=16))
		test300.dists.add(Distribution.objects.get(id=14))
		test300.dists.add(Distribution.objects.get(id=16))
		test300.dists.add(Distribution.objects.get(id=6))
		test100.save()
		test300.save()
		test200.save()

		"""TEST FIELDS"""
		self.assertEqual('test100',test100.code)
		self.assertEqual('Computer Science',test300.dept)
		self.assertEqual('3hunnatest',test300.name)
		self.assertEqual('1:00-4:00PM',test100.time)
		self.assertEqual('TF',test300.date)
		self.assertEqual('Dr Sosa',test300.prof)
		self.assertEqual('When they test me i just pee rose',test100.prof_site)

		"""TEST CONFLICTS"""
		self.assertTrue(test100.conflicts(test300))
		self.assertTrue(test300.conflicts(test100))
		self.assertFalse(test100.conflicts(test200))
		self.assertFalse(test200.conflicts(test300))

		# testing course.dists
		# tester=Course.objects.filter(code='AFR201')[0]
		# t2=Course.objects.filter(code='AFR208')[0]
		# t3=Course.objects.filter(code='CS111')[0]
		# print tester.dists.all()
		# print t2.dists.all()
		# print t3.dists.all()



class MajorTester(TestCase):
	fixtures = ['initial_data_dump_072314.json']
	# def setUp(self):
	def test(self):
		print 'testing major'
		cs=Major.objects.get(code='CS')
		soc=Major.objects.get(code='SOC')

		print Course.objects.filter(dept=cs.name).all()





# class CommentTester(TestCase):
# 	def setUp(self):
# 		Comment.objects.create(
# 			comment_text = "this course rocks!"
# 			comment_author = 
