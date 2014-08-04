#profreader.py

p=open('professors.txt','r')
f=open('init_prof_fixture.json','w+')
f.write('[\n')
x=1

proflist=[]
for l in p.readlines():
	t=l.split('\t')
	proflist.append((t[0].strip(),t[1].strip()))

p.close()

print len(proflist)
proflist=list(set(proflist))
print len(proflist)

for p in proflist:
	f.write("  {\n")
	f.write("    \"model\": \"courses.professor\",\n")
	f.write("    \"pk\": " + str(x) + ",\n")
	f.write("    \"fields\": {\n")
	f.write("      \"name\": \"" + p[0] + "\",\n")
	f.write("      \"site\": \"" + p[1] + "\"\n")
	f.write("    }\n")
	f.write("  },\n")
	x+=1