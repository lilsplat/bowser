#run with ./manage.py shell < django_shell_script.py

from courses.models import Professor, Course

x=1
proflist=[]
for c in Course.objects.all():
	p=c.prof
	p=p.split(',')
	for prof in p:
		if Professor.objects.filter(name=prof).exists():
			#pk, prof id, course id
			proflist.append((x,Professor.objects.filter(name=prof)[0].id,c.id))
			x+=1

# with open('all_courses_fall2014_profs.txt','w+') as txt:
print proflist
txt=open('all_courses_fall2014_profs.txt','w+')
for p in proflist:
	txt.write(str(p).replace(' ','')+'\n')

txt.close()

#THIS IS WRONG BTDUBS