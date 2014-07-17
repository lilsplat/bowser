"""TODO:
still needs to fill out the Distribution object, probably todo after distribution is filled into the table
fix bug: manually need to add ] and delete , at end of .json
for future semesters: need to modify x as to not overwrite other entries in table
need to add semester field to models???
"""


import re

f = open('initial_course_load.json','w')
f.write('[\n')
x = 1

with open('all_courses_fall2014.txt','r') as r:
	read_data = r.read()

read_data = read_data.split("#")
courses = []
x = 1


def parsedept(d):
    deptlist = ['AFR,Africana Studies',
    'AMST,American Studies',
    'ANTH,Anthropology',
    'ART,Art',
    'ASTR,Astronomy',
    'BIOC,Biological Chemistry',
    'BISC,Biological Sciences',
    'CAMS,Cinema and Media Studies',
    'CHEM,Chemistry',
    'CLSC,Cognitive and Linguistic Sciences',
    'CLST,Classical Studies',
    'CPLT,Comparative Literature',
    'CS,Computer Science',
    'EALC,East Asian Languages and Cultures',
    'ECON,Economics',
    'EDUC,Education',
    'ENG,English',
    'ES,Environmental Studies',
    'FREN,French',
    'GEOS,Geosciences',
    'GER,German',
    'HIST,History',
    'ITST,Italian Studies',
    'JWST,Jewish Studies',
    'MATH,Mathematics',
    'MER,Medieval Renaissance Studies',
    'MES,Middle Eastern Studies',
    'MUS,Music',
    'NEUR,Neuroscience',
    'PE,Physical Education',
    'PEAC,Peace and Justice Studies',
    'PHIL,Philosophy',
    'PHYS,Physics',
    'POLS,Political Science',
    'PSYC,Psychology',
    'QR,Quantitative Reasoning',
    'REL,Religion',
    'RUSS,Russian',
    'SAS,South Asia Studies',
    'SOC,Sociology',
    'SPAN,Spanish',
    'THST,Theatre Studies',
    'WGST,Women and Gender Studies',
    'WRIT,Writing',
    'OTHER,Other',
    'UND,Undecided',
    'ARAB,Middle Eastern Studies',
    'ARTH,Art History',
    'ARTS,Studio Art',
    #isn't there another one too....
    'CHIN,East Asian Languages and Cultures',
    'CLCV,Classical Studies',
    'GRK,Classical Studies',
    'HEBR,Jewish Studies',
    'HNUR,South Asian Studies',
    'ITAS,Italian Studies',
    'JPN,East Asian Languages and Cultures',
    'KOR,East Asian Languages and Cultures',
    'LAT,Classical Studies',
    'LING,Cognitive and Linguistic Sciences',
    'ME,Medieval Renaissance Studies',
    'POL,Political Science',
    'PORT,Spanish',
    'SWA,Africana Studies'
    ]

    for dept in deptlist:
        dept = dept.split(',')
        if d == dept[0]:
            print dept[1]
            return dept[1]
    
    return d


for chunk in read_data:
    chunk = chunk.rstrip().split('\n')
    if x != 1:
        chunk.pop(0)
    if len(chunk) > 0:
      f.write("  {\n")
      f.write("    \"model\": \"courses.course\",\n")
      f.write("    \"pk\": " + str(x) + ",\n")
      f.write("    \"fields\": {\n")
      code = chunk.pop(0)
      dept = code
      dept = re.match('[aA-zZ]+', dept)
      dept = dept.group()
      dept = parsedept(dept)
      # print dept
      f.write("      \"code\": \"" + code + "\",\n")
      f.write("      \"dept\": \"" + dept + "\",\n")
      f.write("      \"name\": \"" + chunk.pop(0) + "\",\n")
      f.write("      \"time\": \"" + chunk.pop(0) + "\",\n")
      f.write("      \"date\": \"" + chunk.pop(0) + "\",\n")
      f.write("      \"prof\": \"" + chunk.pop(0) + "\",\n")
      f.write("      \"prof_site\": \"" + chunk.pop(0) + "\"\n")
      f.write("    }\n")
      f.write("  },\n")
      x += 1

      
f.close()







