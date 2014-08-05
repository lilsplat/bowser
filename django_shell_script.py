#run with ./manage.py shell < django_shell_script.py

from courses.models import Professor, Course, TimeAndDate, CourseTemp, Semester, Section
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
for c in CourseTemp.objects.all():
	print c
	print c.section_set.all()
	print '\n\n'


