from bs4 import BeautifulSoup

soup=BeautifulSoup(open('course_browser_htmls copy/201407.txt'))
# print (soup.prettify())
# print soup.find_all('tr')#[2] #starts courses here

# print soup.get_text()
print soup.tbody.tr.th.contents #first CRN
num_courses=len(soup.tbody.contents)
print num_courses

all_course_strings=[]
for string in soup.tbody.stripped_strings:
	all_course_strings.append(repr(string))

print all_course_strings
i=0
all_courses=[]
while i < (len(all_course_strings)-12):
	crn=all_course_strings[i]
	code=all_course_strings[i+1]
	title=all_course_strings[i+2]
	time=all_course_strings[i+6]
	date=all_course_strings[i+8]
	prof=all_course_strings[i+9]
	dist=all_course_strings[i+10]
	all_courses.append(crn)
	i=i+12

print all_courses