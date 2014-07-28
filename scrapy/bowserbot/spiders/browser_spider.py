#browser_spider.py

import scrapy
from scrapy.selector import Selector 
from scrapy.http import HtmlResponse
from bowserbot.items import *
# from courses.models import *
import re

#can't close these ruh roh...bad practice
f=open('browser_spider_test.json','w+')
distf=open('all_courses_fall2014_dists.txt','w+')

class BrowserSpider(scrapy.Spider):
    pk=1
    dist_pk=1
    name = "browser_spider"
    allowed_domains = ["https://courses.wellesley.edu"]

    start_urls=[]
    filereader=open('course_urls.txt','r')
    for line in filereader.readlines():
        start_urls.append(line)

    def parse(self, response):
        # self.log('A response from %s just arrived!' % response.url)
        for sel in response.xpath('//tbody'):
            i=1

            category=sel.xpath('tr['+str(i)+']/th[1]/b/text()').extract()
            category=self.test_and_pop(category,'categoryname')
            if category == 'Course':
                code=sel.xpath('tr['+str(i)+']/th[2]/text()').extract()
                code=self.test_and_pop(code, 'code')
                code=code.split(' ')
                if len(code) >= 4:
                    code_ext=code[3]
                else:
                    code_ext=''
                code=code[0]+code[1]
                code=code.encode("UTF-8")
                code_ext=code_ext.encode("UTF-8")
                i+=1
            else:
                code='None assigned'

            category=sel.xpath('tr['+str(i)+']/th[1]/b/text()').extract()
            category=self.test_and_pop(category,'categoryname')
            if category == 'CRN':
                crn=sel.xpath('tr['+str(i)+']/th[2]/text()').extract()
                crn=self.test_and_pop(crn, 'crn')
                crn=crn.encode("UTF-8")
                i+=1
            else:
                crn='None assigned'

            category=sel.xpath('tr['+str(i)+']/th[1]/b/text()').extract()
            category=self.test_and_pop(category,'categoryname')
            if category == 'Title':
                title=sel.xpath('tr['+str(i)+']/th[2]/text()').extract()
                title=self.test_and_pop(title, 'title')
                title=title.encode("UTF-8")
                title=title.split('\"')
                title=''.join(title)
                i+=1
            else:
                title='None assigned'

            category=sel.xpath('tr['+str(i)+']/th[1]/b/text()').extract()
            category=self.test_and_pop(category,'categoryname')
            if category == 'Credit Hours':
                credit_hours=sel.xpath('tr['+str(i)+']/th[2]/text()').extract()
                credit_hours=self.test_and_pop(credit_hours, 'credit hours')
                credit_hours=credit_hours.encode("UTF-8")
                i+=1
            else:
                credit_hours='None assigned'

            category=sel.xpath('tr['+str(i)+']/th[1]/b/text()').extract()
            category=self.test_and_pop(category,'categoryname')
            if category == 'Description':
                description=sel.xpath('tr['+str(i)+']/th[2]/text()').extract()
                if len(description) == 0: #if not in this tag, in p tag
                    description=sel.xpath('tr['+str(i)+']/th[2]/p[1]/text()').extract()
                if len(description) == 0: #for courses with added div
                    description=sel.xpath('tr['+str(i)+']/th[2]/div/text()').extract()

                if len(description) == 0: #for courses with Topics
                    description=sel.xpath('tr['+str(i)+']/th[2]/div/p[2]/text()').extract()
                if len(description) == 0: #more Topics
                    description=sel.xpath('tr['+str(i)+']/th[2]/p[2]/text()').extract()
                if len(description) == 0: #more Topics
                    description=sel.xpath('tr['+str(i)+']/th[2]/p[3]/text()').extract()

                description=self.test_and_pop(description, 'description')
                description=description.encode("UTF-8")
                description=description.split('\"')
                description=''.join(description)
                description=description.split('\n')
                description=' '.join(description)
                i+=1
            else:
                description='None assigned'

            if len(description) < 3:
                description='None assigned'

            category=sel.xpath('tr['+str(i)+']/th[1]/b/text()').extract()
            category=self.test_and_pop(category,'categoryname')
            if category == 'Additional Information':
                addit_info=sel.xpath('tr['+str(i)+']/th[2]/text()').extract()
                addit_info=self.test_and_pop(addit_info, 'seats_available')
                addit_info=addit_info.encode("UTF-8")
                addit_info=addit_info.split('\"')
                addit_info=''.join(addit_info)
                i+=1
            else:
                addit_info='None assigned'

            category=sel.xpath('tr['+str(i)+']/th[1]/b/text()').extract()
            category=self.test_and_pop(category,'categoryname')
            if category == 'Seats Available':
                seats_available=sel.xpath('tr['+str(i)+']/th[2]/text()').extract()
                seats_available=self.test_and_pop(seats_available, 'seats_available')
                seats_available=seats_available.encode("UTF-8")
                i+=1
            else:
                seats_available='None assigned'

            category=sel.xpath('tr['+str(i)+']/th[1]/b/text()').extract()
            category=self.test_and_pop(category,'categoryname')
            if category == 'Max. Enrollment':
                max_enrollment=sel.xpath('tr['+str(i)+']/th[2]/text()').extract()
                max_enrollment=self.test_and_pop(max_enrollment, 'max_enrollment')
                max_enrollment=max_enrollment.encode("UTF-8")
                i+=1
            else:
                max_enrollment='None assigned'

            #SOMETHING WENT WRONG HERE SEE CRN 13427
            category=sel.xpath('tr['+str(i)+']/th[1]/b/text()').extract()
            category=self.test_and_pop(category,'categoryname')
            if category == 'Permission of Instructor':
                by_permission=sel.xpath('tr['+str(i)+']/th[2]/b/text()').extract()
                by_permission=self.test_and_pop(by_permission,'by_permission')
                by_permission=by_permission.encode("UTF-8")
                by_permission=by_permission.split('\"')
                by_permission=''.join(by_permission)
                i+=1
            else:
                by_permission='None assigned'

            category=sel.xpath('tr['+str(i)+']/th[1]/b/text()').extract()
            category=self.test_and_pop(category,'categoryname')
            if category == 'Prerequisite(s)':
                prereq=sel.xpath('tr['+str(i)+']/th[2]/text()').extract()
                prereq=self.test_and_pop(prereq, 'prereq')
                prereq=prereq.encode("UTF-8")
                prereq=prereq.split('\"')
                prereq=''.join(prereq)
                i+=1
            else:
                prereq='None assigned'

            category=sel.xpath('tr['+str(i)+']/th[1]/b/text()').extract()
            category=self.test_and_pop(category,'categoryname')
            if category == 'Distributions':
                dist=sel.xpath('tr['+str(i)+']/th[2]/text()').extract()
                dist=self.test_and_pop(dist, 'dist')
                dist=dist.encode("UTF-8")
                i+=1
            else:
                dist='None assigned'

            category=sel.xpath('tr['+str(i)+']/th[1]/b/text()').extract()
            category=self.test_and_pop(category, 'categoryname')
            if category == 'Notes':
                notes=sel.xpath('tr['+str(i)+']/th[2]/text()').extract()
                notes=self.test_and_pop(notes,'notes')
                notes=notes.encode("UTF-8")
                notes=notes.split('\"')
                notes=''.join(notes)
                notes=notes.split('\n')
                notes=' '.join(notes)
                i+=1
            else:
                notes='None assigned'

            category=sel.xpath('tr['+str(i)+']/th[1]/b/text()').extract()
            category=self.test_and_pop(category,'categoryname')
            if category == 'Crosslisted Courses:':
                xlisted=sel.xpath('tr['+str(i)+']/th[2]/text()').extract()
                xlisted=self.test_and_pop(xlisted, 'dist')
                xlisted=xlisted.encode("UTF-8")
                xlisted=xlisted.split('\"')
                xlisted=''.join(xlisted)
                i+=1
            else:
                xlisted='None assigned'

            category=sel.xpath('tr['+str(i)+']/th[1]/b/text()').extract()
            category=self.test_and_pop(category, 'categoryname')
            if category == 'Instructor(s)':
                prof=sel.xpath('tr['+str(i)+']/th[2]/text()').extract()
                prof=self.test_and_pop(prof, 'prof')
                prof=prof.encode("UTF-8")
                i+=1
            else:
                prof='None assigned'

            #still need to fix this
            category=sel.xpath('tr['+str(i)+']/th[1]/b/text()').extract()
            category=self.test_and_pop(category, 'categoryname')
            if category == 'Meeting Time(s)':
                time_and_date=sel.xpath('tr['+str(i)+']/th[2]/text()').extract()
                time_and_date=self.test_and_pop(time_and_date, 'time_and_date')
                time_and_date=time_and_date.encode("UTF-8")
                time_and_date=time_and_date.split(',')
                try:
                    date=''
                    starttime=''
                    endtime=''
                    for part in time_and_date:
                        part=part.split(' - ')
                        date+=part[0]
                        starttime=part[1]
                        starttime=starttime[:5]
                        endtime=part[2]
                        endtime=endtime[:5]
                except IndexError:
                    date='None assigned'
                    starttime='None assigned'
                    endtime='None assigned'
            else:
                # time_and_date='None assigned'
                date='None assigned'
                starttime='None assigned'
                endtime='None assigned'
            
            # print 'course:' + str(course)
            # print 'crn:' + str(crn)
            # print 'title:' + str(title)
            # print 'credit hours:' + str(credit_hours)
            # print 'description:' + str(description)
            # print 'addit info:' + str(addit_info)
            # print 'seats_available:' + str(seats_available)
            # print 'max_enrollment:' + str(max_enrollment)
            # print 'by_permission:' + str(by_permission)
            # print 'prereq:' + str(prereq)
            # print 'dist:' + str(dist)
            # print 'notes:' + str(notes)
            # pritn 'xlisted:' + str(xlisted)
            # print 'time_and_date:' + str(time_and_date)
            # print 'end'

            # filewriter.write(course.encode("UTF-8") + '\n')
            # filewriter.write(crn.encode("UTF-8") + '\n')
            # filewriter.write(title.encode("UTF-8") + '\n')
            # filewriter.write(credit_hours.encode("UTF-8") + '\n')
            # filewriter.write(description.encode("UTF-8") + '\n')
            # filewriter.write(addit_info.encode("UTF-8") + '\n')
            # filewriter.write(seats_available.encode("UTF-8") + '\n')
            # filewriter.write(max_enrollment.encode("UTF-8") + '\n')
            # filewriter.write(by_permission.encode("UTF-8") + '\n')
            # filewriter.write(prereq.encode("UTF-8") + '\n')
            # filewriter.write(dist.encode("UTF-8") + '\n')
            # filewriter.write(notes.encode("UTF-8") + '\n')
            # filewriter.write(xlisted.encode("UTF-8")+'\n')
            # filewriter.write(prof.encode("UTF-8") + '\n')
            # filewriter.write(time_and_date.encode("UTF-8") + '\n')
            # filewriter.write("\n")

            #get rid of quotes for ints

            try:
                dept=code
                dept=re.search('[A-Z]+', dept).group()
                dept=self.parsedept(dept)
            except AttributeError:
                dept='None assigned'

            if (dept != 'Physical Education' and dept != 'None assigned'):
                f.write("  {\n")
                f.write("    \"model\": \"courses.course\",\n")
                f.write("    \"pk\": " + str(BrowserSpider.pk) + ",\n")
                f.write("    \"fields\": {\n")
                f.write("      \"dept\": \"" + dept + "\",\n")
                f.write("      \"code\": \"" + code + "\",\n")
                f.write("      \"crn\": \"" + crn + "\",\n")
                f.write("      \"title\": \"" + title.strip('\"') + "\",\n")
                f.write("      \"credit_hours\": \"" + credit_hours + "\",\n")
                f.write("      \"description\": \"" + description.strip('\"') + "\",\n")
                f.write("      \"addit_info\": \"" + addit_info.strip('\"') + "\",\n")
                f.write("      \"seats_available\": \"" + seats_available + "\",\n")
                f.write("      \"max_enrollment\": \"" + max_enrollment + "\",\n")
                f.write("      \"by_permission\": \"" + by_permission + "\",\n")
                f.write("      \"prereq\": \"" + prereq.strip('\"') + "\",\n")
                # f.write("      \"dist\": \"" + dist + "\",\n")
                f.write("      \"notes\": \"" + notes.strip('\"') + "\",\n")
                f.write("      \"xlisted\": \"" + xlisted.strip('\"') + "\",\n")
                f.write("      \"prof\": \"" + prof + "\",\n")
                f.write("      \"date\": \"" + date + "\",\n")
                f.write("      \"starttime\": \"" + starttime + "\",\n")
                f.write("      \"endtime\": \"" + endtime + "\",\n")
                f.write("      \"offered_in_fall\": true,\n")
                f.write("      \"offered_in_spring\": false\n")
                f.write("    }\n")
                f.write("  },\n")
                # print 'course id:' + str(BrowserSpider.pk)
                self.write_dist(code,dist,credit_hours,code_ext,notes,title)
                BrowserSpider.pk += 1

    def test_and_pop(self, extracted_list, listname):
        if len(extracted_list) == 0:
            return 'None assigned'
        elif len(extracted_list) == 1:
            return extracted_list.pop()
        else:
            string = extracted_list.pop().strip()
            for element in extracted_list:
                string = element.strip() + ',' + string
            return string

    def parsedept(self,d):
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
                # print dept[1]
                return dept[1]

        return d

    def write_dist(self,code,dist,credit_hours,code_ext,notes,title):
        #('L' in code_ext or 'Laboratory' in title)
        if (('L' in code_ext or 'Laboratory' in title)
            and 'Does not fulfill the laboratory requirement.' not in notes
            and 'Does not satisfy the laboratory requirement.' not in notes
            and credit_hours == '0'):
            d=[5] #delete all dists becasue this is lab
        else:
            d=[]
            course=str.split(dist,',')
            for c in course:
                if "QRB" in c:
                    d.append(3)
                if "QRF" in c:
                    d.append(4)
                if "Lab" in c:
                    d.append(5)
                if 3==int(float(re.search('[0-9]',code).group())):
                    if (not 'POL31' in code and not 'POL32' in code):
                        d.append(6)
                    if ('POL13' in code or 'POL23' in code or 'POL43' in code):
                        d.append(6)
                if "W" in c:
                    d.append(7)
                if "Language" in c:
                    d.append(8)
                    d.append(10)
                if "Arts" in c:
                    d.append(9)
                    d.append(10)
                if "Social" in c:
                    d.append(11)
                if "Epistemology" in c:
                    d.append(12)
                if "Historical" in c:
                    d.append(13)
                if "Religion" in c:
                    d.append(13)
                if "Mathematical" in c:
                    d.append(14)
                    d.append(16)
                if "Natural" in c:
                    d.append(15)
                    d.append(16)

        d=list(set(d)) #get rid of duplicates
        # print d
        for distribution_id in d:
            distf.write("("+str(BrowserSpider.dist_pk)+","+str(BrowserSpider.pk)+","+str(distribution_id)+")")
            # print 'wrote: course id:' + str(BrowserSpider.pk) + '   dist id:' + str(distribution_id)
            distf.write("\n")
            BrowserSpider.dist_pk+=1

        