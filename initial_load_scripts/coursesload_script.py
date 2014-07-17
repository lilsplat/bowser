f = open('initial_course_load.json','w')
f.write('[\n')
x = 1

with open('all_courses_fall2014.txt','r') as r:
	read_data = r.read()

read_data = read_data.split("#")
courses = []
x = 1
for chunk in read_data:
	chunk = chunk.rstrip().split('\n')
	chunk.pop(0)
	if len(chunk) > 0:
		f.write("  {\n")
    	f.write("    \"model\": \"courses.course\",\n")
    	f.write("    \"pk\": " + str(x) + ",\n")
    	f.write("    \"fields\": {\n")
    	f.write("      \"code\": \"" + chunk.pop(0) + "\",\n")
    	# f.write("      \"dept\": \"" + chunk.pop(0) + "\,"\n")
    	f.write("      \"name\": \"" + chunk.pop(0) + "\",\n")
    	f.write("      \"time\": \"" + chunk.pop(0) + "\",\n")
    	f.write("      \"date\": \"" + chunk.pop(0) + "\",\n")
    	f.write("      \"prof\": \"" + chunk.pop(0) + "\",\n")
    	f.write("      \"prof_site\": \"" + chunk.pop(0) + "\"\n")
    	f.write("    }\n")
    	f.write("  },\n")
    	x += 1

f.close()