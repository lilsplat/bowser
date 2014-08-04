#run with ./manage.py shell < django_shell_script.py

from courses.models import Professor, Course, TimeAndDate

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
x=1
tdlist=[]
for c in Course.objects.all():
	if TimeAndDate.objects.filter(dates=c.date,starttime=c.starttime,endtime=c.endtime).exists():
		#id | course_id | timeanddate_id
		tdlist.append((x,c.id,TimeAndDate.objects.filter(dates=c.date,starttime=c.starttime,endtime=c.endtime)[0].id))
	else:
		#td object does not exist; create it
		TimeAndDate.objects.create(dates=c.date,starttime=c.starttime,endtime=c.endtime)
		tdlist.append((x,c.id,TimeAndDate.objects.filter(dates=c.date,starttime=c.starttime,endtime=c.endtime)[0].id))
	x+=1

# with open('all_courses_fall2014_profs.txt','w+') as txt:
# print proflist
txt=open('all_courses_fall2014_tds.txt','w+')
for t in tdlist:
	txt.write(str(t).replace(' ','')+'\n')

txt.close()


"""SEMESTER M2M POPULATION"""

