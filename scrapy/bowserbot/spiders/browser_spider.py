#browser_spider.py

import scrapy
from scrapy.selector import Selector 
from scrapy.http import HtmlResponse
from bowserbot.items import *
# from courses.models import *
import re

filewriter=open('browser_spider_test.txt','w+')
class BrowserSpider(scrapy.Spider):
    name = "browser_spider"
    allowed_domains = ["https://courses.wellesley.edu"]

    start_urls=[]
    filereader=open('course_urls.txt','r')
    for line in filereader.readlines():
        start_urls.append(line)
            

    # start_urls = [
    #     # "https://courses.wellesley.edu/display_single_course_cb.php?crn=13275&semester=201409&pe_term=&skip_graphics=1&no_navs=1"
    #     "https://courses.wellesley.edu/display_single_course_cb.php?crn=10219&semester=201409&pe_term=&skip_graphics=1&no_navs=1%0A",
    #     "https://courses.wellesley.edu/display_single_course_cb.php?crn=13275&semester=201409&pe_term=&skip_graphics=1&no_navs=1"
    #     ]

    def parse(self, response):
        # self.log('A response from %s just arrived!' % response.url)
        for sel in response.xpath('//tbody'):
            i=1

            course=sel.xpath('tr['+str(i)+']/th[2]/text()').extract()
            course=self.test_and_pop(course, 'course')
            course=course.split(' ')
            course=course[0]+course[1]
            i+=1

            crn=sel.xpath('tr['+str(i)+']/th[2]/text()').extract()
            crn=self.test_and_pop(crn, 'crn')
            i+=1

            title=sel.xpath('tr['+str(i)+']/th[2]/text()').extract()
            title=self.test_and_pop(title, 'title')
            i+=1

            credit_hours=sel.xpath('tr['+str(i)+']/th[2]/text()').extract()
            credit_hours=self.test_and_pop(credit_hours, 'credit hours')
            i+=1

            #problem with /p/ -- some are, some aren't WHYHYHYYYY
            description=sel.xpath('tr['+str(i)+']/th[2]/p/text()').extract()
            description=self.test_and_pop(description, 'description')
            i+=1

            seats_available=sel.xpath('tr['+str(i)+']/th[2]/text()').extract()
            seats_available=self.test_and_pop(seats_available, 'seats_available')
            i+=1

            max_enrollment=sel.xpath('tr['+str(i)+']/th[2]/text()').extract()
            max_enrollment=self.test_and_pop(max_enrollment, 'max_enrollment')
            i+=1

            x=sel.xpath('tr['+str(i)+']/th[1]/b/text()').extract()
            x=self.test_and_pop(x,'x')
            if x == 'Permission of Instructor':
                by_permission=sel.xpath('tr['+str(i)+']/th[2]/b/text()').extract()
                by_permission=self.test_and_pop(by_permission,'by_permission')
                i+=1
            else:
                by_permission='permission of instructor: None assigned'

            prereq=sel.xpath('tr['+str(i)+']/th[2]/text()').extract()
            prereq=self.test_and_pop(prereq, 'prereq')
            i+=1

            dist=sel.xpath('tr['+str(i)+']/th[2]/text()').extract()
            dist=self.test_and_pop(dist, 'dist')
            i+=1

            x=sel.xpath('tr['+str(i)+']/th[1]/b/text()').extract()
            x=self.test_and_pop(x,'x')
            if x == 'Notes':
                notes=sel.xpath('tr['+str(i)+']/th[2]/b/text()').extract()
                notes=self.test_and_pop(notes,'notes')
                i+=1
            else:
                notes='Notes: none assigned'

            prof=sel.xpath('tr['+str(i)+']/th[2]/text()').extract()
            prof=self.test_and_pop(prof, 'prof')
            i+=1

            time_and_date=sel.xpath('tr['+str(i)+']/th[2]/text()').extract()
            time_and_date=self.test_and_pop(time_and_date, 'time_and_date')
            
            # print 'course:' + str(course)
            # print 'crn:' + str(crn)
            # print 'title:' + str(title)
            # print 'credit hours:' + str(credit_hours)
            # print 'description:' + str(description)
            # print 'seats_available:' + str(seats_available)
            # print 'max_enrollment:' + str(max_enrollment)
            # print 'by_permission:' + str(by_permission)
            # print 'prereq:' + str(prereq)
            # print 'dist:' + str(dist)
            # print 'notes:' + str(notes)
            # print 'time_and_date:' + str(time_and_date)
            # print 'end'
            filewriter.write(course.encode("UTF-8") + '\n')
            filewriter.write(crn.encode("UTF-8") + '\n')
            filewriter.write(title.encode("UTF-8") + '\n')
            filewriter.write(credit_hours.encode("UTF-8") + '\n')
            filewriter.write(description.encode("UTF-8") + '\n')
            filewriter.write(seats_available.encode("UTF-8") + '\n')
            filewriter.write(max_enrollment.encode("UTF-8") + '\n')
            filewriter.write(by_permission.encode("UTF-8") + '\n')
            filewriter.write(prereq.encode("UTF-8") + '\n')
            filewriter.write(dist.encode("UTF-8") + '\n')
            filewriter.write(notes.encode("UTF-8") + '\n')
            filewriter.write(prof.encode("UTF-8") + '\n')
            filewriter.write('time and date:')
            filewriter.write(time_and_date.encode("UTF-8") + '\n')
            filewriter.write("\n")

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
        


"""COMMENTED OFF STUFF FROM COURSE_SPIDER BELOW"""

    #     self.log('A response from %s just arrived!' % response.url)

    #     #parsing file:///.... into the semester code
    #     path = response.url
    #     code = path.split("/").pop(12)
    #     code = code.split(".").pop(0)

    #     filewriter = open('course_browser_database/' + code + '_new.txt', 'w')


    #     for sel in response.xpath('//tbody/tr'): #each <tr> is a class table

    #         course = sel.xpath('th[2]/a/text()').extract()
    #         course = self.test_and_pop(course)
    #         course = course.replace(" ","")

    #         title = sel.xpath('th[3]/text()').extract()
    #         title = self.test_and_pop(title)

    #         time = sel.xpath('th[7]/text()').extract() #has empty and multiple object lists
    #         time = self.test_and_pop(time)

    #         date = sel.xpath('th[8]/text()').extract() #has empty and multiple object lists
    #         date = self.test_and_pop(date)
    #         date = date.strip() #idk why but new line?

    #         prof = sel.xpath('th[9]/a/text()').extract() #has empty lists
    #         prof = self.test_and_pop(prof)

    #         prof_site = sel.xpath('th[9]/a/@href').extract() #has empty lists
    #         prof_site = self.test_and_pop(prof_site)
    #         prof_site = 'https://courses.wellesley.edu/' + prof_site

    #         distribution = sel.xpath('th[11]/text()').extract() #has multiple object lists
    #         distribution = self.test_and_pop(distribution)


    #         # """ Do we need to encode UTF-8? """

    #         # c = DjangoCourseItem()

    #         # c['code'] = course.encode("UTF-8")
    #         # c['name'] = title.encode("UTF-8")
    #         # c['time'] = time.encode("UTF-8")
    #         # c['date'] = date.encode("UTF-8")
    #         # c['prof'] = prof.encode("UTF-8")
    #         # c['prof_site'] = prof_site.encode("UTF-8")
    #         # return c
            
    #         # dist = []
    #         # if len(distribution) == 0:
    #         #     d = DjangoDistItem()
    #         #     d['name'] = 'None assigned'
    #         #     dist.append(d)
    #         # elif len(distribution) == 1:
    #         #     d = DjangoDistItem()
    #         #     d['name'] = distribution.pop().strip().encode("UTF-8")
    #         #     dist.append(d) 
    #         # else:
    #         #     for element in distribution:
    #         #         d = DjangoDistItem()
    #         #         d['name'] = element.strip().encode("UTF-8")
    #         #         dist.append(d)


    #         # """ TO DO: fix this!! django does not recognize DjangoDistItem as an acceptable input to the dists field """

    #         # test = dist[0]
    #         # c['dists'] = test

            



    #         # print 'beginning writing\n'
    #         # print 'writing crn %s' % str(crn)
    #         # filewriter.write(crn.encode("UTF-8") + '\n')
    #         # print 'writing title %s' % title
    #         # filewriter.write(title.encode("UTF-8") + '\n') #why?????
    #         # print 'writing time %s' % str(time)
    #         # filewriter.write(time.encode("UTF-8") + '\n')
    #         # print 'writing date %s' % str(date)
    #         # filewriter.write(date.encode("UTF-8") + '\n')
    #         # print 'writing prof %s' % str(prof)
    #         # filewriter.write(prof.encode("UTF-8") + '\n')
    #         # print 'writing prof site %s' % str(prof_site)
    #         # filewriter.write(prof_site.encode("UTF-8") + '\n')
    #         # print 'writing distribution %s' % str(distribution)
    #         # filewriter.write(distribution.encode("UTF-8") + '\n')
    #         # print 'writing delimiter'
    #         # filewriter.write("..")

    #         filewriter.write(#crn.encode("UTF-8") + "\n" + 
    #             course.encode("UTF-8") + "\n" + 
    #             title.encode("UTF-8") + "\n" + 
    #             # str(isCourseFull) + "\n" + 
    #             time.encode("UTF-8") + "\n" + 
    #             date.encode("UTF-8") + "\n" + 
    #             prof.encode("UTF-8") + "\n" + 
    #             prof_site.encode("UTF-8") + "\n" + 
    #             distribution.encode("UTF-8") + 
    #             "\n#\n") #delimiter

    #     filewriter.close()





    	
    # 	   # page_title = response.selector.xpath('head/title/text()').extract()
    # 	   # filename = "tutorial/txt_docs/" + str(page_title.pop()) + ".txt" #saved in txt docs directory
    # 	   # f = open (filename, 'w') #new file writer with name of the title

    #     #    #creates selector to loop through all <p> tags for hyperlinks
    #     #    for sel in response.xpath('//p'):
    #     #     title = sel.xpath('a[contains(@href,"/wiki/")]/@title').extract() 

    #     #    #problem is this only works with /a; it doesn't work on disambiguation pages because those use /link
    #     #    #find wikipedia links and extract their titles
	   #     #  #??????? what's the proper syntax here
	   #     #  while not not title: #len(title) != 0:
	   #     #  	f.write(str(title.pop()) + "\n") #write titles line by line onto file

	   #     #  #NB: it will scrape ALL //p tags even if they are empty. seems like a waste



    


    # # def parse(self, response):
    # #     filename = response.url.split("/")[-2]
    # #     with open(filename, 'wb') as f:
    # #         f.write(response.body)

    # # def make_requests_from_url(url):
    # #     return scrapy.http.Request(url)
    # #     # return [scrapy.FormRequest("http://www.example.com/login",
    # #     #     formdata={'user': 'john', 'pass': 'secret'},
    # #     #     callback=self.logged_in)]







