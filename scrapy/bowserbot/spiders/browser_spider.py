#browser_spider.py

import scrapy
from scrapy.selector import Selector 
from scrapy.http import HtmlResponse
from bowserbot.items import *
# from courses.models import *
import re

# filewriter=open('browser_spider_test.txt','w+')
f=open('browser_spider_test.json','w+')

class BrowserSpider(scrapy.Spider):
    pk=1
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
                code=code[0]+code[1]
                i+=1
            else:
                code='None assigned'

            category=sel.xpath('tr['+str(i)+']/th[1]/b/text()').extract()
            category=self.test_and_pop(category,'categoryname')
            if category == 'CRN':
                crn=sel.xpath('tr['+str(i)+']/th[2]/text()').extract()
                crn=self.test_and_pop(crn, 'crn')
                i+=1
            else:
                crn='None assigned'

            category=sel.xpath('tr['+str(i)+']/th[1]/b/text()').extract()
            category=self.test_and_pop(category,'categoryname')
            if category == 'Title':
                title=sel.xpath('tr['+str(i)+']/th[2]/text()').extract()
                title=self.test_and_pop(title, 'title')
                i+=1
            else:
                title='None assigned'

            category=sel.xpath('tr['+str(i)+']/th[1]/b/text()').extract()
            category=self.test_and_pop(category,'categoryname')
            if category == 'Credit Hours':
                credit_hours=sel.xpath('tr['+str(i)+']/th[2]/text()').extract()
                credit_hours=self.test_and_pop(credit_hours, 'credit hours')
                i+=1
            else:
                credit_hours='None assigned'

            category=sel.xpath('tr['+str(i)+']/th[1]/b/text()').extract()
            category=self.test_and_pop(category,'categoryname')
            if category == 'Description':
                description=sel.xpath('tr['+str(i)+']/th[2]/text()').extract()
                if len(description) == 0: #if not in this tag
                    description=sel.xpath('tr['+str(i)+']/th[2]/p/text()').extract()
                description=self.test_and_pop(description, 'description')
                i+=1
            else:
                description='None assigned'

            category=sel.xpath('tr['+str(i)+']/th[1]/b/text()').extract()
            category=self.test_and_pop(category,'categoryname')
            if category == 'Additional Information':
                addit_info=sel.xpath('tr['+str(i)+']/th[2]/text()').extract()
                addit_info=self.test_and_pop(addit_info, 'seats_available')
                i+=1
            else:
                addit_info='None assigned'

            category=sel.xpath('tr['+str(i)+']/th[1]/b/text()').extract()
            category=self.test_and_pop(category,'categoryname')
            if category == 'Seats Available':
                seats_available=sel.xpath('tr['+str(i)+']/th[2]/text()').extract()
                seats_available=self.test_and_pop(seats_available, 'seats_available')
                i+=1
            else:
                seats_available='None assigned'

            category=sel.xpath('tr['+str(i)+']/th[1]/b/text()').extract()
            category=self.test_and_pop(category,'categoryname')
            if category == 'Max. Enrollment':
                max_enrollment=sel.xpath('tr['+str(i)+']/th[2]/text()').extract()
                max_enrollment=self.test_and_pop(max_enrollment, 'max_enrollment')
                i+=1
            else:
                max_enrollment='None assigned'

            #SOMETHING WENT WRONG HERE SEE CRN 13427
            category=sel.xpath('tr['+str(i)+']/th[1]/b/text()').extract()
            category=self.test_and_pop(category,'categoryname')
            if category == 'Permission of Instructor':
                by_permission=sel.xpath('tr['+str(i)+']/th[2]/b/text()').extract()
                by_permission=self.test_and_pop(by_permission,'by_permission')
                i+=1
            else:
                by_permission='None assigned'

            category=sel.xpath('tr['+str(i)+']/th[1]/b/text()').extract()
            category=self.test_and_pop(category,'categoryname')
            if category == 'Prerequisite(s)':
                prereq=sel.xpath('tr['+str(i)+']/th[2]/text()').extract()
                prereq=self.test_and_pop(prereq, 'prereq')
                i+=1
            else:
                prereq='None assigned'

            category=sel.xpath('tr['+str(i)+']/th[1]/b/text()').extract()
            category=self.test_and_pop(category,'categoryname')
            if category == 'Distributions':
                dist=sel.xpath('tr['+str(i)+']/th[2]/text()').extract()
                dist=self.test_and_pop(dist, 'dist')
                i+=1
            else:
                dist='None assigned'

            category=sel.xpath('tr['+str(i)+']/th[1]/b/text()').extract()
            category=self.test_and_pop(category, 'categoryname')
            if category == 'Notes':
                notes=sel.xpath('tr['+str(i)+']/th[2]/b/text()').extract()
                notes=self.test_and_pop(notes,'notes')
                i+=1
            else:
                notes='None assigned'

            category=sel.xpath('tr['+str(i)+']/th[1]/b/text()').extract()
            category=self.test_and_pop(category,'categoryname')
            if category == 'Crosslisted Courses:':
                xlisted=sel.xpath('tr['+str(i)+']/th[2]/text()').extract()
                xlisted=self.test_and_pop(xlisted, 'dist')
                i+=1
            else:
                xlisted='None assigned'

            category=sel.xpath('tr['+str(i)+']/th[1]/b/text()').extract()
            category=self.test_and_pop(category, 'categoryname')
            if category == 'Instructor(s)':
                prof=sel.xpath('tr['+str(i)+']/th[2]/text()').extract()
                prof=self.test_and_pop(prof, 'prof')
                i+=1
            else:
                prof='None assigned'

            category=sel.xpath('tr['+str(i)+']/th[1]/b/text()').extract()
            category=self.test_and_pop(category, 'categoryname')
            if category == 'Meeting Time(s)':
                time_and_date=sel.xpath('tr['+str(i)+']/th[2]/text()').extract()
                time_and_date=self.test_and_pop(time_and_date, 'time_and_date')
            else:
                time_and_date='None assigned'
            
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

            dept=code
            dept=re.search('[A-Z]+', dept).group()
            dept=self.parsedept(code)

            f.write("  {\n")
            f.write("    \"model\": \"courses.course\",\n")
            f.write("    \"pk\": " + str(BrowserSpider.pk) + ",\n")
            f.write("    \"fields\": {\n")
            f.write("      \"dept\": \"" + dept + "\",\n")
            f.write("      \"code\": \"" + code.encode("UTF-8") + "\",\n")
            f.write("      \"crn\": \"" + crn.encode("UTF-8") + "\",\n")
            f.write("      \"title\": \"" + title.encode("UTF-8").strip('\"') + "\",\n")
            f.write("      \"credit_hours\": \"" + credit_hours.encode("UTF-8") + "\",\n")
            f.write("      \"description\": \"" + description.encode("UTF-8").strip('\"') + "\",\n")
            f.write("      \"addit_info\": \"" + addit_info.encode("UTF-8").strip('\"') + "\",\n")
            f.write("      \"seats_available\": \"" + seats_available.encode("UTF-8") + "\",\n")
            f.write("      \"max_enrollment\": \"" + max_enrollment.encode("UTF-8") + "\",\n")
            f.write("      \"by_permission\": \"" + by_permission.encode("UTF-8") + "\",\n")
            f.write("      \"prereq\": \"" + prereq.encode("UTF-8").strip('\"') + "\",\n")
            # f.write("      \"dist\": \"" + dist.encode("UTF-8") + "\",\n")
            f.write("      \"notes\": \"" + notes.encode("UTF-8").strip('\"') + "\",\n")
            f.write("      \"xlisted\": \"" + xlisted.encode("UTF-8").strip('\"') + "\",\n")
            f.write("      \"prof\": \"" + prof.encode("UTF-8") + "\",\n")
            f.write("      \"time_and_date\": \"" + time_and_date.encode("UTF-8")[:-6] + "\",\n")
            f.write("      \"offered_in_fall\": true,\n")
            f.write("      \"offered_in_spring\": false\n")
            f.write("    }\n")
            f.write("  },\n")
            BrowserSpider.pk += 1

            #problems: sometimes there's a bug if there's a "" in Description
            #still need to better parse description for random tokens like , or ;
    

    def test_and_pop(self, extracted_list, listname):
        if len(extracted_list) == 0:
            return listname + ': None assigned'
        elif len(extracted_list) == 1:
            return extracted_list.pop()
        else:
            string = extracted_list.pop().strip()
            for element in extracted_list:
                string = element.strip() + ',' + string
            return string

    # def remove_quotes(s):


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
            else:
                return d
                print str(d) +' has no dept'
        # return d


        