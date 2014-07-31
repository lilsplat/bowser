f=open('all_courses_fall2014_semesters.txt','w+')

#id | course_id | semester_id

i=1 #id
course_id=1 #course_id
semester_id=1

for x in xrange(1,784):
	f.write('('+str(x)+','+str(x)+','+'1)')
	f.write('\n')

f.close()