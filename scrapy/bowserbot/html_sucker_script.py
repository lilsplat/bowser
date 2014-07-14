"""
This script runs through all semesters available from the online course browser and 
'suck' the html to course_browser_htmls/[semester code]. 

"""


import mechanize
import sys
from mechanize import ParseResponse, urlopen, urljoin

browser = mechanize.Browser()
browser.set_handle_robots(False)
browser.set_handle_refresh(False)

response = browser.open('https://courses.wellesley.edu/')
forms = ParseResponse(response, backwards_compat=False)
form = forms[1]
# print form 

all_semesters = ["201409", "201407", "201406", "201402", "201401", "201309", "201307", 
"201306", "201302", "201301", "201209", "201207", "201206", "201202", "201201", "201109", "201107", 
"201106", "201102", "201101", "201009", "201007", "201006", "201002", "201001", "200909", "200907", "200906", 
"200902", "200901", "200809", "200807", "200806", "200802", "200801", "200709", "200707", "200706", 
"200702", "200701", "200609", "200607", "200606", "200602", "200601", "200509", "200507", "200506", 
"200502", "200501", "200409", "200407", "200406", "200402", "200401", "200309", "200307", "200306", 
"200302", "200301", "200209", "200207", "200206", "200202", "200201", "200109", "200107", "200106", "200102", "200101", "200009", "200007"]

for s in all_semesters:
	form["semester"] = [s]
	fileWriter = open('course_browser_htmls/' + s + '.txt', 'w')
	fileWriter.write(urlopen(form.click()).read())

fileWriter.close()

""""""

# for form in browser.forms():
# 	print "Form name: ", form.name

# browser.select_form("classes")
# for control in browser.form.controls:
# 	print "type=%s, name=%s, value=%s" % (control.type, control.name, browser[control.name])

# control = browser.form.find_control("semester")

# if control.type == "select":
# 	for item in control.items:
# 		print "name = %s, values = %s" % (item.name, str([label.text for label in item.get_labels()]))

