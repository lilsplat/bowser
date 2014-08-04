# TODO:
# - Test Distribution
# - Fill out major, test Major
# - Test Student.distributions_todo, num_distributions todo?
# - Test Student.major_todo
# - 

from django.utils import unittest
from django.test import TestCase
from django.contrib.auth.models import User
from courses.models import Course, Student, Distribution, Major, Rating, CourseBucket, Semester
import datetime
from django.db.models import Count


class StudentTester(TestCase):
	fixtures = ['initial_data_dump_080214.json']

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
			comment_course=Course.objects.filter(code='CS111')[0],
			score=5
			)
		Rating.objects.create(
			comment_text = "eh, this course could have been better. maybe if i didn't fall asleep in class each day...",
			comment_author = Student.objects.get(user=st_user),
			comment_course=Course.objects.filter(code='CS111')[0],
			score=3
			)
		Rating.objects.create(
			comment_text = "this course sucked. never again, never again.",
			comment_author = Student.objects.get(user=lx_user),
			comment_course=Course.objects.filter(code='CS307')[0],
			score=1
			)
		Rating.objects.create(
			comment_author=Student.objects.get(user=lx_user),
			comment_course=Course.objects.filter(code='CS111')[0],
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
		lily_courses=[]
		qrbcourse=Distribution.objects.get(name='Basic QR').course_set.all()[0]
		lily_courses.append(qrbcourse)
		qrfcourse=Distribution.objects.get(name='QR Overlay').course_set.all()[10]
		lily_courses.append(qrfcourse)
		labcourse=Distribution.objects.get(name='Lab').course_set.all()[20]
		lily_courses.append(labcourse)
		tlevelcourse_1=Distribution.objects.get(name='300-level').course_set.all()[30]
		lily_courses.append(tlevelcourse_1)
		tlevelcourse_2=Distribution.objects.get(name='300-level').course_set.all()[40]
		lily_courses.append(tlevelcourse_2)
		tlevelcourse_3=Distribution.objects.get(name='300-level').course_set.all()[50]
		lily_courses.append(tlevelcourse_3)
		tlevelcourse_4=Distribution.objects.get(name='300-level').course_set.all()[60]
		lily_courses.append(tlevelcourse_4)
		fywcourse=Distribution.objects.get(name='First Year Writing').course_set.all()[0]
		lily_courses.append(fywcourse)
		llcourse=Distribution.objects.get(name='Language and Literature').course_set.all()[10]
		lily_courses.append(llcourse)
		artcourse=Distribution.objects.get(name='Arts, Music, Theater, Film and Video').course_set.all()[20]
		lily_courses.append(artcourse)
		ll_artcourse=Distribution.objects.get(name='Language and Literature or Arts, Music, Theater, Film and Video').course_set.all()[7]
		lily_courses.append(ll_artcourse)
		sbacourse=Distribution.objects.get(name='Social and Behavioral Analysis').course_set.all()[0]
		lily_courses.append(sbacourse)
		ec_hscourse=Distribution.objects.get(name='Epistemology and Cognition or Historical Studies').course_set.all()[10]
		lily_courses.append(ec_hscourse)
		hs_rempcourse=Distribution.objects.get(name='Historical Studies or Religion, Ethics, and Moral Philosophy').course_set.all()[20]
		lily_courses.append(hs_rempcourse)
		mmcourse=Distribution.objects.get(name='Mathematical Modeling').course_set.all()[30]
		lily_courses.append(mmcourse)
		npscourse=Distribution.objects.get(name='Natural and Physical Sciences').course_set.all()[0]
		lily_courses.append(npscourse)
		mm_npscourse=Distribution.objects.get(name='Mathematical Modeling or Natural and Physical Sciences').course_set.all()[10]
		lily_courses.append(mm_npscourse)

		for c in lily_courses:
			lily.add_course(c)

		lily.save()

		# ostart=datetime.datetime.now()
		# lily.distributions_todo()
		# oend=datetime.datetime.now()
		# o=oend-ostart
		# print o

		print 'start'
		print Course.objects.all()




		# self.assertEqual(17,lily.courses.count())

		# lily.remove_course(qrbcourse)
		# self.assertEqual(16,lily.courses.count())
		
		


		""" TEST RATINGS """
		#should move this to its own class duhhhh
		good_comment=Rating.objects.get(id=1)
		mediocre_comment=Rating.objects.get(id=2)
		bad_comment=Rating.objects.get(id=3)
		empty_comment=Rating.objects.get(id=4)
		good_comment.save()
		mediocre_comment.save()
		bad_comment.save()
		empty_comment.save()

		#testing comments
		self.assertEqual('yay this course rocks my socks off!',good_comment.comment_text)
		self.assertEqual('eh, this course could have been better. maybe if i didn\'t fall asleep in class each day...',mediocre_comment.comment_text)
		self.assertEqual('this course sucked. never again, never again.',bad_comment.comment_text)
		#testing scores
		self.assertEqual(1,bad_comment.score)	
		self.assertEqual(3,mediocre_comment.score)
		self.assertEqual(5,good_comment.score)
		self.assertEqual(5,empty_comment.score)
		#testing course rating_set
		cs111=Course.objects.filter(code='CS111')[0]
		cs307=Course.objects.filter(code='CS307')[0]
		self.assertTrue(3,len(cs111.rating_set.all()))
		self.assertTrue(1,len(cs307.rating_set.all()))
		#testing student rating_set
		self.assertTrue(3,len(lily.rating_set.all()))
		self.assertTrue(3,len(sravanti.rating_set.all()))

		"""TESTING AVG_SCORE"""
		self.assertAlmostEqual(13.0/3.0,cs111.avg_score())
		self.assertAlmostEqual(1.0,cs307.avg_score())

class CourseTester(TestCase):
	fixtures=['initial_data_dump_080214.json']

	def setUp(self):
		Course.objects.create(
			code='test100',
			dept='Computer Science',
			crn='12345',
			title='Amen 2 Testing',
			credit_hours='1',
			description='AND I SAY CHURRRRRCH',
			addit_info='featuring Drake',
			seats_available='1',
			max_enrollment='1',
			by_permission='None assigned',
			notes='When they test me i just pee rose',
			xlisted='None assigned',
			starttime='1:00',
			endtime='4:00',
			date='TF',
			prof='Meek Mill'
			# offered_in_fall=True,
			# offered_in_spring=False
			)
		Course.objects.create(
			code='test300',
			dept='Computer Science', #?
			crn='23456',
			credit_hours='1',
			description='Bang bang it\'s macaroni time',
			addit_info='yung chop on the beat',
			seats_available='1',
			max_enrollment='10',
			by_permission='None assigned',
			notes='None assigned',
			xlisted='None assigned',
			starttime='1:00',
			endtime='4:00',
			title='3hunnatest',
			date='TF',
			prof='Dr Sosa'
			# offered_in_fall=True,
			# offered_in_spring=False
			)
		Course.objects.create(
			code='test200',
			dept='Computer Science',
			crn='12345',
			credit_hours='1',
			description='',
			addit_info='',
			seats_available='1',
			max_enrollment='1',
			by_permission='None assigned',
			notes='None assigned',
			xlisted='None assigned',
			starttime='9:50',
			endtime='11:00',
			title='blah',
			date='TF',
			prof='Dr Sosa'
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
		self.assertEqual('3hunnatest',test300.title)
		self.assertEqual('1:00',test100.starttime)
		self.assertEqual('4:00',test100.endtime)
		self.assertEqual('TF',test300.date)
		self.assertEqual('Dr Sosa',test300.prof)
		self.assertEqual('When they test me i just pee rose',test100.notes)
		self.assertEqual('12345',test100.crn)
		self.assertEqual('1',test100.credit_hours)
		self.assertEqual('Bang bang it\'s macaroni time',test300.description)
		self.assertEqual('featuring Drake',test100.addit_info)
		self.assertEqual('1',test200.seats_available)
		self.assertEqual('1',test200.max_enrollment)
		self.assertEqual('None assigned',test200.notes)
		self.assertEqual('None assigned',test200.xlisted)
		self.assertEqual('Dr Sosa',test300.prof)

		"""TEST CONFLICTS"""
		self.assertTrue(test100.conflicts(test300))
		self.assertTrue(test300.conflicts(test100))
		self.assertFalse(test100.conflicts(test200))
		self.assertFalse(test200.conflicts(test300))

		"""TEST FULL"""
		self.assertTrue(test100.is_full())
		self.assertFalse(test300.is_full())

		"""TEST DISTRIBUTIONS"""

		self.assertEqual('Mathematical Modeling',test100.dists.all()[0].name)
		self.assertEqual('300-level',test300.dists.all()[0].name)
		self.assertEqual('Mathematical Modeling or Natural and Physical Sciences',test100.dists.all()[1].name)
		self.assertEqual(2,len(test100.dists.all()))
		self.assertEqual(3,len(test300.dists.all()))
		d=Distribution.objects.create(name='Testing')
		test100.dists.add(d)
		test200.dists.add(d)
		self.assertEqual(2,len(d.course_set.all()))

		#when repopulating db, use this as a test for dist/course parallel
		# d=Distribution.objects.get(id=3)
		# print d
		# print d.course_set.all()

class DistributionTester(TestCase):
	fixtures = ['initial_data_dump_080214.json']

	def setUp(self):
		Distribution.objects.create(
			name='Testing Dist'
			)
		Course.objects.create(
			code='test123',
			dept='Test',
			crn='12345',
			title='TAST',
			credit_hours='1',
			description='mmm',
			addit_info='None',
			seats_available='1',
			max_enrollment='1',
			by_permission='None',
			prereq='None',
			xlisted='None',
			prof='None',
			date='None',
			starttime='None',
			endtime='None'
			)

	def test(self):
		"""INITIALIZE"""
		testdist=Distribution.objects.get(name='Testing Dist')
		qrb=Distribution.objects.get(name='Basic QR')
		lab=Distribution.objects.get(name='Lab')
		threehunna=Distribution.objects.get(name='300-level')
		ll=Distribution.objects.get(name='Language and Literature')
		ll_art=Distribution.objects.get(name='Language and Literature or Arts, Music, Theater, Film and Video')
		qr140_1=Course.objects.filter(code='QR140')[0]
		qr140_2=Course.objects.filter(code='QR140')[1]
		cs307=Course.objects.filter(code='CS307')[0]
		cs240=Course.objects.filter(code='CS240').exclude(credit_hours='0')[0]
		cs240_lab=Course.objects.filter(code='CS240').filter(credit_hours='0')[0]
		ealc245=Course.objects.filter(code='EALC245')[0]
		test123=Course.objects.filter(code='test123')[0]
		test123.dists.add(testdist)

		"""TESTING IS_FULFILLED_BY"""
		self.assertTrue(qrb.is_fulfilled_by(qr140_1))
		self.assertTrue(qrb.is_fulfilled_by(qr140_2))
		self.assertTrue(threehunna.is_fulfilled_by(cs307))
		self.assertTrue(lab.is_fulfilled_by(cs240_lab))
		self.assertFalse(lab.is_fulfilled_by(cs240)) #lab should be only fulfilled by the LAB, not the course
		self.assertTrue(ll.is_fulfilled_by(ealc245))
		self.assertTrue(ll_art.is_fulfilled_by(ealc245))
		self.assertTrue(testdist.is_fulfilled_by(test123))

		"""TESTING SUGGESTED_COURSES"""
		nonlab_list=[cs240,cs307,test123]
		lab_list=[cs240_lab]
		mixed_list=[cs240_lab,test123,cs307]
		self.assertIn('CS240',lab.suggested_courses(nonlab_list))
		self.assertNotIn('CS240',lab.suggested_courses(lab_list))
		self.assertNotIn('CS240',lab.suggested_courses(mixed_list))


# class CommentTester(TestCase):
# 	def setUp(self):
# 		Comment.objects.create(
# 			comment_text = "this course rocks!"
# 			comment_author = 



class MajorTester(TestCase):
	fixtures = ['initial_data_dump_080214.json']
	def setUp(self):
		Major.objects.create(
			code='TEST',
			name='Testing Major',
			is_minor=False
			)
		CourseBucket.objects.create(
			name='TEST Core',
			num_pick='2',
			major=Major.objects.get(code='TEST')
			)
		CourseBucket.objects.create(
			name='TEST Lab',
			num_pick='1',
			major=Major.objects.get(code='TEST')
			)
	def test(self):
		"""INITIALIZE"""
		cs=Major.objects.get(code='CS')
		soc=Major.objects.get(code='SOC')
		test=Major.objects.get(code='TEST')
		test_cb=CourseBucket.objects.get(name='TEST Core')
		test_cb_lab=CourseBucket.objects.get(name='TEST Lab')
		test.save()
		test_cb.save()
		test_cb_lab.save()

		cs111=Course.objects.filter(code='CS111')[0]
		cs240=Course.objects.filter(code='CS240').exclude(credit_hours='0')[0]
		cs240_lab=Course.objects.filter(code='CS240').filter(credit_hours='0')[0]

		test_cb.courses.add(cs111)
		test_cb.courses.add(cs240)
		test_cb.courses.add(cs240_lab)
		test_cb.save()

		test_cb_lab.courses.add(cs240_lab)
		test_cb_lab.save()

		cb_full_list=[cs111,cs240,cs240_lab]
		cb_empty_list=[]
		cb_half_list=[cs111]
		cb_lab_list=[cs240_lab]

		#testing coursebucket
		"""TESTING IS_FULFILLED_BY"""
		self.assertTrue(test_cb.is_fulfilled_by(cs111))
		self.assertFalse(test_cb_lab.is_fulfilled_by(cs111))
		self.assertFalse(test_cb_lab.is_fulfilled_by(cs240))
		self.assertTrue(test_cb_lab.is_fulfilled_by(cs240_lab))

		"""TESTING IS_FULFILLED"""
		self.assertTrue(test_cb.is_fulfilled(cb_full_list))
		self.assertFalse(test_cb.is_fulfilled(cb_empty_list))
		self.assertFalse(test_cb.is_fulfilled(cb_half_list))
		self.assertTrue(test_cb_lab.is_fulfilled(cb_full_list))

		"""TESTING COURSE_CODES"""
		self.assertEqual(2,len(test_cb.course_codes()))
		self.assertEqual(1,len(test_cb_lab.course_codes()))

		"""TESTING SUGGESTED_COURSES"""
		self.assertEqual('CS240',test_cb.suggested_courses(cb_half_list)[0])
		self.assertEqual([],test_cb.suggested_courses(cb_full_list))

		#testing major
		print test.coursebucket_set.all()
		"""TESTING IS_FULFILLED"""
		self.assertTrue(test.is_fulfilled(cb_full_list))
		self.assertFalse(test.is_fulfilled(cb_empty_list))
		self.assertFalse(test.is_fulfilled(cb_half_list))
		self.assertFalse(test.is_fulfilled(cb_lab_list))

		print test.cbs_togo(cb_full_list)
		print test.cbs_togo(cb_half_list)
		print test.cbs_togo(cb_empty_list)
		print test.cbs_togo(cb_lab_list)

		print test.suggested_cbs_togo(cb_full_list)
		print test.suggested_cbs_togo(cb_half_list)
		print test.suggested_cbs_togo(cb_empty_list)
		print test.suggested_cbs_togo(cb_lab_list)



		# print Course.objects.filter(dept=cs.name).all()
