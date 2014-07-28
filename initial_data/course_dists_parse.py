#NOT USED as of 6/28
#see browser_spider in scrapy instead
#course_dists_parse.py
import re

string=''
with open ("all_courses_fall2014.txt", "r") as myfile:
    string=myfile.read().replace('\n', ';')

#new delim is ;#;

string=string[2:] #remove first #
all_courses = str.split(string,";#;")

course_id=0
i=1
f = open("all_courses_fall2014_dists.txt","w'")
for chunk in all_courses:
	d=[]
	course = str.split(chunk,";")
	# print course[6]
	# if "Foreign Language"
	if "QRB" in course[6]:
		d.append(3)
	if "QRF" in course[6]:
		d.append(4)
	if "Lab" in course[6]:
		d.append(5)
	#ALSO AHVE TO CHECK POL13...
	if 3==int(float(re.search('[0-9,-]',course[0]).group())):
		if not "POL31" in course[0] and not "POL32" in course[0]:
			d.append(6)
	if "W" in course[6]:
		d.append(7)
	if "Language" in course[6]:
		d.append(8)
		d.append(10)
	if "Arts" in course[6]:
		d.append(9)
		d.append(10)
	if "Social" in course[6]:
		d.append(11)
	if "Epistemology" in course[6]:
		d.append(12)
	if "Historical" in course[6]:
		d.append(13)
	if "Religion" in course[6]:
		d.append(13)
	if "Mathematical" in course[6]:
		d.append(14)
		d.append(16)
	if "Natural" in course[6]:
		d.append(15)
		d.append(16)

	course_id+=1
	for distribution_id in d:
		f.write("("+str(i)+","+str(course_id)+","+str(distribution_id)+")")
		f.write("\n")
		i+=1

s = "WRIT301-92"
# print re.search('[0-9,-]',s).group()

