from bs4 import BeautifulSoup

soup=BeautifulSoup(open('course_browser_htmls copy/201406.txt'))
# print (soup.prettify())
# print soup.find_all('tr')#[2] #starts courses here

# print soup.get_text()
print soup.tbody.tr.th.contents #first CRN
num_courses=len(soup.tbody.contents)
print num_courses

all_course_strings=[]
for s in soup.tbody.find_all('tr'):
	l=1
	alltags=[]
	for x in s.stripped_strings:
		alltags.append(x)
	# crn=alltags[0]
	# print crn
	# code=alltags[1]
	# print code
	# title=alltags[2]
	# print title
	print alltags
	print '\n'



# for s in soup.tbody.tr.stripped_strings:
# 	print s
# 	print '\n'


# for string in soup.tbody.stripped_strings:
# 	all_course_strings.append(repr(string))
# 	print string
# 	print '\n\n'

# for a in all_course_strings:
# 	print a

# print '\n\n'
# i=0
# all_courses=[]
# while i < (len(all_course_strings)-13):
# 	crn=all_course_strings[i]
# 	# print crn
# 	code=all_course_strings[i+1]
# 	print code
# 	title=all_course_strings[i+2]
# 	time=all_course_strings[i+6]
# 	date=all_course_strings[i+8]
# 	prof=all_course_strings[i+9]
# 	dist=all_course_strings[i+10]
# 	all_courses.append(crn)
# 	i=i+13

#have to manually delete <hr> tags......