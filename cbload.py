"""DJANGO SCRIPT"""

from courses.models import *

f=open('major_cb_load.txt','r')

cbs=[]
for l in f.readlines():
	cbs.append(l)

f.close()
# print cbs[0].split(';')


w=open('missed_courses.txt','w+')

for cb in cbs:
	cb=cb.split(';')
	print 'parsing: '
	print cb
	if cb[0] == 'm':	
		print 'parse major'
		mb=cb[3].strip('\n')
		if mb=='True':
			b=True
		else:
			b=False
		m=Major.objects.create(code=cb[1],name=cb[2],is_minor=b)
		m.save()
		print m
		print '\n'
	else:
		print 'parse cb'
		if cb[4]=='True':
			b=True
		else:
			b=False
		m=Major.objects.filter(name=cb[3]).get(is_minor=b)
		new_cb=CourseBucket.objects.create(name=cb[1],num_pick=int(float(cb[2])),major=m)
		if cb[5]=='\n':
			new_cb.save()
			print 'no courses'
		else:
			cs=cb[5]
			cs=cs.split(',')
			cs=list(set(cs)) #get rid of duplicates
			for c in cs:
				c=c.strip('\n')
				c=c.replace(' ','')
				try:
					new_cb.courses.add(Course.objects.get(code=c))
				except:
					w.write(new_cb.name)
					w.write(c)
					w.write('\n')
				new_cb.save()
		print new_cb




	# if cb[0] == 'm':
	# 	print 'parse major'
	# 	if cb[3] == 'True':
	# 		b=True
	# 	else:
	# 		b=False
	# 	m=Major.objects.create(code=cb[1],name=cb[2],is_minor=b)
	# 	m.save()
	# 	print m
	# 	print '\n'
	# else:
	# 	print 'parse cb'
	# 	if cb[4] == 'True':
	# 		b=True
	# 	else:
	# 		b=False
	# 	m=Major.objects.filter(name=cb[3]).filter(is_minor=b)
	# 	new_cb=CourseBucket.objects.create(name=cb[1],num_pick=int(float(cb[2])),m)
	# 	if len(cb) == 6:
	# 		cs=cb[5]
	# 		if len(cs) > 0:
	# 			cs=cs.split(',')
	# 			cs=list(set(cs))
	# 			for c in cs:
	# 				try:
	# 					new_cb.courses.add(Course.objects.get(code=c.strip().replace(' ',''))
	# 				except:
	# 					w.write(new_cb.name)
	# 					w.write(c)
	# 					w.write('\n')
	# 	new_cb.save()
	# 	print new_cb
	# 	print '\n'

w.close()

# c=CourseBucket.objects.create()

# AFR MAJOR=====================================
# c;AFR 300;2;FREN330;Africana Studies
# AFR Elective;6;FREN330,AFR234,AFR204,AFR280;Africana Studies
# AFR MINOR=====================================
# c;AFR 300;1;FREN330;Africana Studies
# c;AFR Elective;3;FREN330,AFR234,AFR204,AFR208;Africana Studies
# AMST MAJOR====================================
# c;AMST Elective;1;ECON223,SPAN255,CAMS207,PSYC346,WGST330,POL2305,AMST269,AMST283,ECON329,AFR266,AMST320,CAMS272,ECON226,AFR320,ECON325,ECON238