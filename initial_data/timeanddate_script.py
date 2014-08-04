#profreader.py

p=open('timeanddate.txt','r')
f=open('init_timeanddate_fixture.json','w+')
f.write('[\n')
x=1

tdlist=[]
for l in p.readlines():
	part=l.split('\t\t')
	time=part[0]
	time=time.split(',')
	for t in time:
		if t != 'None assigned' and t != 'TBA':
			a=t.split('-')
			print a
			starttime=a[0]
			endtime=a[1]
			date=part[1].strip()
			tdlist.append((starttime.strip(),endtime.strip(),part[1].strip()))
		else:
			starttime='None assigned'
			endtime='None assigned'
			date=part[1]
			tdlist.append((starttime.strip(),endtime.strip(),part[1].strip()))

p.close()

print len(tdlist)
tdlist=list(set(tdlist))
print len(tdlist)
print tdlist

for p in tdlist:
	f.write("  {\n")
	f.write("    \"model\": \"courses.timeanddate\",\n")
	f.write("    \"pk\": " + str(x) + ",\n")
	f.write("    \"fields\": {\n")
	f.write("      \"dates\": \"" + p[2] + "\",\n")
	f.write("      \"starttime\": \"" + p[0] + "\",\n")
	f.write("      \"endtime\": \"" + p[1] + "\"\n")
	f.write("    }\n")
	f.write("  },\n")
	x+=1