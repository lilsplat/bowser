#run with ./manage.py shell < django_shell_script.py

from courses.models import *
from django.db.models import Count

"""PROFESSOR M2M POPULATION"""
# x=1
# proflist=[]
# for c in Course.objects.all():
# 	p=c.prof
# 	p=p.split(',')
# 	for prof in p:
# 		if Professor.objects.filter(name=prof).exists():
# 			#pk, course id, prof id
# 			proflist.append((x,c.id,Professor.objects.filter(name=prof)[0].id))
# 			x+=1

# # with open('all_courses_fall2014_profs.txt','w+') as txt:
# # print proflist
# txt=open('all_courses_fall2014_profs.txt','w+')
# for p in proflist:
# 	txt.write(str(p).replace(' ','')+'\n')

# txt.close()

# print 'start testing'
# for c in Course.objects.all():
# 	p=c.prof
# 	print p
# 	p=p.split(',')
# 	i=0
# 	for prof in p:
# 		if Professor.objects.filter(course=c.id)[i].name != prof:
# 			print 'Error: prof should be: ' + str(prof) + ' and is ' + Professor.objects.filter(course=c.id)[i].name

"""TIMEANDDATE M2M POPULATION"""
# x=1
# tdlist=[]
# for c in Course.objects.all():
# 	if TimeAndDate.objects.filter(dates=c.date,starttime=c.starttime,endtime=c.endtime).exists():
# 		#id | course_id | timeanddate_id
# 		tdlist.append((x,c.id,TimeAndDate.objects.filter(dates=c.date,starttime=c.starttime,endtime=c.endtime)[0].id))
# 	else:
# 		#td object does not exist; create it
# 		TimeAndDate.objects.create(dates=c.date,starttime=c.starttime,endtime=c.endtime)
# 		tdlist.append((x,c.id,TimeAndDate.objects.filter(dates=c.date,starttime=c.starttime,endtime=c.endtime)[0].id))
# 	x+=1

# # with open('all_courses_fall2014_profs.txt','w+') as txt:
# # print proflist
# txt=open('all_courses_fall2014_tds.txt','w+')
# for t in tdlist:
# 	txt.write(str(t).replace(' ','')+'\n')

# txt.close()


"""FINDING DUPLICATES"""

# ledger=[]
# for c in Course.objects.all():
# 	ledgercode=c.code + c.credit_hours
# 	if ledgercode in ledger:
# 		#create section
# 		print 'creating section for:'
# 		print c
# 		ctemp=CourseTemp.objects.filter(code=c.code).get(credit_hours=c.credit_hours)
# 		i=ctemp.section_set.count()
# 		i=int(float(i))
# 		i+=1
# 		p=Professor.objects.filter(course=c.id)[0]
# 		td=TimeAndDate.objects.filter(course=c.id)[0]
# 		s=Semester.objects.filter(course=c.id)[0]
# 		sec=Section.objects.create(sec_id=i,crn=c.crn,seats_available=c.seats_available,max_enrollment=c.max_enrollment,prof=p,timeanddate=td,semester=s,course=ctemp)
# 		#save
# 		sec.save()
# 	else:
# 		#create new coursetemp object and section
# 		print 'creating initial coursetemp objects for: '
# 		print c
# 		ledger.append(ledgercode) #mark as made
# 		ctemp=CourseTemp.objects.create(dept=c.dept,code=c.code,title=c.title,credit_hours=c.credit_hours,description=c.description,addit_info=c.addit_info,by_permission=c.by_permission,prereq=c.prereq,notes=c.notes,xlisted=c.xlisted)
# 		ds=c.dists.all()
# 		for d in ds:
# 			ctemp.dists.add(d)
# 		#create first section
# 		p=Professor.objects.filter(course=c.id)[0]
# 		td=TimeAndDate.objects.filter(course=c.id)[0]
# 		s=Semester.objects.filter(course=c.id)[0]
# 		sec=Section.objects.create(sec_id='1',crn=c.crn,seats_available=c.seats_available,max_enrollment=c.max_enrollment,prof=p,timeanddate=td,semester=s,course=ctemp)
# 		#save
# 		sec.save()
# 		ctemp.save()

"""CHECKING DUPLICATE SCRIPT"""
# for c in Course.objects.all():
# 	print c
# 	print c.section_set.all()
# 	print '\n\n'

"""RENAMING LABS AND OTHER SECTIONS"""
# labs=Course.objects.filter(credit_hours='0')
# print labs
# for l in labs:
# 	old_code=l.code
# 	print 'old code: ' + old_code
# 	new_code=old_code + 'L'
# 	print 'new code: ' + new_code
# 	l.code=new_code
# 	l.save()

"""READING ARCHIVE JSON FILE, CHECKING FOR DUPLICATES"""
import json
from pprint import pprint
json_data=open('browser_spider_archives.json')
data=json.load(json_data)
json_data.close()
i=0
"""HEY IM STILL WORKING ON THIS...DONT RUN PLZ FUTUTRE ME"""
"""todo: add dists"""
while i < len(data):
	i=i+1
	acode=data[i]['fields']['code']
	#take care of lab courses	
	acredit=data[i]['fields']['credit_hours']
	if acredit == '0':
		acode+='L'
	#if course exists, add section
	print 'reading ' + acode
	if Course.objects.filter(code=acode).exists():
		print acode + ' already exists'
		sprofs=data[i]['fields']['prof']
		if ',' in sprofs:
			sprofs=sprofs.split(',')
		else:
			temp_sprofs=[]
			temp_sprofs.append(sprofs)
			sprofs=temp_sprofs
		print sprofs
		print '\nadding ' + str(len(sprofs)) + ' sections:'
		for p in sprofs:
			#add section
			print p
			sc=Course.objects.get(code=acode)
			ssem=Semester.objects.get(session='Archive')
			sid=Course.objects.get(code=acode).section_set.filter(semester__session='Archive').count()
			sid+=1 #increment
			print 'adding section ' + str(sid)
			scrn=data[i]['fields']['crn']
			sseats=data[i]['fields']['seats_available']
			smax=data[i]['fields']['max_enrollment']
			sprof=Professor.objects.filter(name=p)[0]
			stad=TimeAndDate.objects.filter(starttime=data[i]['fields']['starttime']).filter(endtime=data[i]['fields']['endtime']).get(dates=data[i]['fields']['date'])
			print 'crn: ' + scrn + ', sseats: ' + sseats + ', smax: ' + smax 
			sec=Section.objects.create(sec_id=sid,crn=scrn,seats_available=sseats,max_enrollment=smax,prof=sprof,timeanddate=stad,semester=ssem,course=sc)
			sec.save()
			print 'saved' 
	else: #if course does not exist, add course and section
		#create course
		print acode + ' does not exist'
		print 'adding course'
		cdept=data[i]['fields']['dept']
		ccode=acode
		ctitle=data[i]['fields']['title']
		chours=acredit
		cdes=data[i]['fields']['description']
		caddit=data[i]['fields']['addit_info']
		cbyperm=data[i]['fields']['by_permission']
		cprereq=data[i]['fields']['prereq']
		cnotes=data[i]['fields']['notes']
		cxlist=data[i]['fields']['xlisted']
		print 'dept ' + cdept + ' code ' + ccode + ' title ' + ctitle
		print 'hours ' + chours + ' descrp ' + cdes + ' addit ' + caddit
		print 'by perm ' + cbyperm + ' prereq ' + cprereq + ' notes ' + cnotes + ' xlist ' + cxlist
		# cdist
		c=Course.objects.create(dept=cdept,code=ccode,title=ctitle,credit_hours=chours,description=cdes,addit_info=caddit,by_permission=cbyperm,prereq=cprereq,notes=cnotes,xlisted=cxlist)
		c.save()
		#create section
		print 'course saved' 
		print '\nadding section'
		sprofs=data[i]['fields']['prof']
		if ',' in sprofs:
			sprofs=sprofs.split(',')
		else:
			temp_sprofs=[]
			temp_sprofs.append(sprofs)
			sprofs=temp_sprofs
		print sprofs
		for p in sprofs:
			#add section
			sc=Course.objects.get(code=acode)
			ssem=Semester.objects.get(session='Archive')
			sid=Course.objects.get(code=acode).section_set.filter(semester__session='Archive').count()
			sid+=1 #increment
			scrn=data[i]['fields']['crn']
			sseats=data[i]['fields']['seats_available']
			smax=data[i]['fields']['max_enrollment']
			sprof=Professor.objects.filter(name=p)[0]
			stad=TimeAndDate.objects.filter(starttime=data[i]['fields']['starttime']).filter(endtime=data[i]['fields']['endtime']).get(dates=data[i]['fields']['date'])
			print 'crn: ' + scrn + ', sseats: ' + sseats + ', smax: ' + smax 
			sec=Section.objects.create(sec_id=sid,crn=scrn,seats_available=sseats,max_enrollment=smax,prof=sprof,timeanddate=stad,semester=ssem,course=sc)
			sec.save()
			print 'saved'

	# else:
	# 	print 'DNE: ' + acode
	print '\n\n'
	print '-------------'
	print '\n'



