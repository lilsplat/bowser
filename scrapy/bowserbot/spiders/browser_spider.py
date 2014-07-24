#browser_spider.py

import scrapy
from scrapy.selector import Selector 
from scrapy.http import HtmlResponse
from bowserbot.items import *
from courses.models import *


class BrowserSpider(scrapy.Spider):
    name = "browser_spider"
    allowed_domains = ["https://courses.wellesley.edu"]

    start_urls = [
    #change from /tutorial to /bowserbot
        "https://courses.wellesley.edu/display_single_course_cb.php?crn=13275&semester=201409&pe_term=&skip_graphics=1&no_navs=1"
        # "file:///Users/lilian/Documents/2014/GitHub/bowser/scrapy/bowserbot/course_browser_htmls/201409.txt", 
        # "file:///Users/lilian/Documents/2014/GitHub/bowser/scrapy/bowserbot/course_browser_htmls/201407", 
        # "file:///Users/lilian/Documents/2014/GitHub/bowser/scrapy/bowserbot/course_browser_htmls/201406.txt", 
        # "file:///Users/lilian/Documents/2014/GitHub/bowser/scrapy/bowserbot/course_browser_htmls/201402.txt", 
        # "file:///Users/lilian/Documents/2014/GitHub/bowser/scrapy/bowserbot/course_browser_htmls/201401.txt", 
        # "file:///Users/lilian/Documents/2014/GitHub/bowser/scrapy/bowserbot/course_browser_htmls/201309.txt", 
        # "file:///Users/lilian/Documents/2014/GitHub/bowser/scrapy/bowserbot/course_browser_htmls/201307.txt", 
        # "file:///Users/lilian/Documents/2014/GitHub/bowser/scrapy/bowserbot/course_browser_htmls/201306.txt", 
        # "file:///Users/lilian/Documents/2014/GitHub/bowser/scrapy/bowserbot/course_browser_htmls/201302.txt", 
        # "file:///Users/lilian/Documents/2014/GitHub/bowser/scrapy/bowserbot/course_browser_htmls/201301.txt", 
        # "file:///Users/lilian/Documents/2014/GitHub/bowser/scrapy/bowserbot/course_browser_htmls/201209.txt", 
        # "file:///Users/lilian/Documents/2014/GitHub/bowser/scrapy/bowserbot/course_browser_htmls/201207.txt", 
        # "file:///Users/lilian/Documents/2014/GitHub/bowser/scrapy/bowserbot/course_browser_htmls/201206.txt", 
        # "file:///Users/lilian/Documents/2014/GitHub/bowser/scrapy/bowserbot/course_browser_htmls/201202.txt", 
        # "file:///Users/lilian/Documents/2014/GitHub/bowser/scrapy/bowserbot/course_browser_htmls/201201.txt", 
        # "file:///Users/lilian/Documents/2014/GitHub/bowser/scrapy/bowserbot/course_browser_htmls/201109.txt", 
        # "file:///Users/lilian/Documents/2014/GitHub/bowser/scrapy/bowserbot/course_browser_htmls/201107.txt", 
        # "file:///Users/lilian/Documents/2014/GitHub/bowser/scrapy/bowserbot/course_browser_htmls/201106.txt", 
        # "file:///Users/lilian/Documents/2014/GitHub/bowser/scrapy/bowserbot/course_browser_htmls/201102.txt", 
        # "file:///Users/lilian/Documents/2014/GitHub/bowser/scrapy/bowserbot/course_browser_htmls/201101.txt", 
        # "file:///Users/lilian/Documents/2014/GitHub/bowser/scrapy/bowserbot/course_browser_htmls/201009.txt", 
        # "file:///Users/lilian/Documents/2014/GitHub/bowser/scrapy/bowserbot/course_browser_htmls/201007.txt", 
        # "file:///Users/lilian/Documents/2014/GitHub/bowser/scrapy/bowserbot/course_browser_htmls/201006.txt", 
        # "file:///Users/lilian/Documents/2014/GitHub/bowser/scrapy/bowserbot/course_browser_htmls/201002.txt", 
        # "file:///Users/lilian/Documents/2014/GitHub/bowser/scrapy/bowserbot/course_browser_htmls/201001.txt", 
        # "file:///Users/lilian/Documents/2014/GitHub/bowser/scrapy/bowserbot/course_browser_htmls/200909.txt", 
        # "file:///Users/lilian/Documents/2014/GitHub/bowser/scrapy/bowserbot/course_browser_htmls/200907.txt", 
        # "file:///Users/lilian/Documents/2014/GitHub/bowser/scrapy/bowserbot/course_browser_htmls/200906.txt", 
        # "file:///Users/lilian/Documents/2014/GitHub/bowser/scrapy/bowserbot/course_browser_htmls/200902.txt", 
        # "file:///Users/lilian/Documents/2014/GitHub/bowser/scrapy/bowserbot/course_browser_htmls/200901.txt", 
        # "file:///Users/lilian/Documents/2014/GitHub/bowser/scrapy/bowserbot/course_browser_htmls/200809.txt", 
        # "file:///Users/lilian/Documents/2014/GitHub/bowser/scrapy/bowserbot/course_browser_htmls/200807.txt", 
        # "file:///Users/lilian/Documents/2014/GitHub/bowser/scrapy/bowserbot/course_browser_htmls/200806.txt", 
        # "file:///Users/lilian/Documents/2014/GitHub/bowser/scrapy/bowserbot/course_browser_htmls/200802.txt", 
        # "file:///Users/lilian/Documents/2014/GitHub/bowser/scrapy/bowserbot/course_browser_htmls/200801.txt", 
        # "file:///Users/lilian/Documents/2014/GitHub/bowser/scrapy/bowserbot/course_browser_htmls/200709.txt", 
        # "file:///Users/lilian/Documents/2014/GitHub/bowser/scrapy/bowserbot/course_browser_htmls/200707.txt", 
        # "file:///Users/lilian/Documents/2014/GitHub/bowser/scrapy/bowserbot/course_browser_htmls/200706.txt", 
        # "file:///Users/lilian/Documents/2014/GitHub/bowser/scrapy/bowserbot/course_browser_htmls/200702.txt", 
        # "file:///Users/lilian/Documents/2014/GitHub/bowser/scrapy/bowserbot/course_browser_htmls/200701.txt", 
        # "file:///Users/lilian/Documents/2014/GitHub/bowser/scrapy/bowserbot/course_browser_htmls/200609.txt", 
        # "file:///Users/lilian/Documents/2014/GitHub/bowser/scrapy/bowserbot/course_browser_htmls/200607.txt", 
        # "file:///Users/lilian/Documents/2014/GitHub/bowser/scrapy/bowserbot/course_browser_htmls/200606.txt", 
        # "file:///Users/lilian/Documents/2014/GitHub/bowser/scrapy/bowserbot/course_browser_htmls/200602.txt", 
        # "file:///Users/lilian/Documents/2014/GitHub/bowser/scrapy/bowserbot/course_browser_htmls/200601.txt", 
        # "file:///Users/lilian/Documents/2014/GitHub/bowser/scrapy/bowserbot/course_browser_htmls/200509.txt", 
        # "file:///Users/lilian/Documents/2014/GitHub/bowser/scrapy/bowserbot/course_browser_htmls/200507.txt", 
        # "file:///Users/lilian/Documents/2014/GitHub/bowser/scrapy/bowserbot/course_browser_htmls/200506.txt", 
        # "file:///Users/lilian/Documents/2014/GitHub/bowser/scrapy/bowserbot/course_browser_htmls/200502.txt", 
        # "file:///Users/lilian/Documents/2014/GitHub/bowser/scrapy/bowserbot/course_browser_htmls/200501.txt", 
        # "file:///Users/lilian/Documents/2014/GitHub/bowser/scrapy/bowserbot/course_browser_htmls/200409.txt", 
        # "file:///Users/lilian/Documents/2014/GitHub/bowser/scrapy/bowserbot/course_browser_htmls/200407.txt", 
        # "file:///Users/lilian/Documents/2014/GitHub/bowser/scrapy/bowserbot/course_browser_htmls/200406.txt", 
        # "file:///Users/lilian/Documents/2014/GitHub/bowser/scrapy/bowserbot/course_browser_htmls/200402.txt", 
        # "file:///Users/lilian/Documents/2014/GitHub/bowser/scrapy/bowserbot/course_browser_htmls/200401.txt", 
        # "file:///Users/lilian/Documents/2014/GitHub/bowser/scrapy/bowserbot/course_browser_htmls/200309.txt", 
        # "file:///Users/lilian/Documents/2014/GitHub/bowser/scrapy/bowserbot/course_browser_htmls/200307.txt", 
        # "file:///Users/lilian/Documents/2014/GitHub/bowser/scrapy/bowserbot/course_browser_htmls/200306.txt", 
        # "file:///Users/lilian/Documents/2014/GitHub/bowser/scrapy/bowserbot/course_browser_htmls/200302.txt", 
        # "file:///Users/lilian/Documents/2014/GitHub/bowser/scrapy/bowserbot/course_browser_htmls/200301.txt", 
        # "file:///Users/lilian/Documents/2014/GitHub/bowser/scrapy/bowserbot/course_browser_htmls/200209.txt", 
        # "file:///Users/lilian/Documents/2014/GitHub/bowser/scrapy/bowserbot/course_browser_htmls/200207.txt", 
        # "file:///Users/lilian/Documents/2014/GitHub/bowser/scrapy/bowserbot/course_browser_htmls/200206.txt", 
        # "file:///Users/lilian/Documents/2014/GitHub/bowser/scrapy/bowserbot/course_browser_htmls/200202.txt", 
        # "file:///Users/lilian/Documents/2014/GitHub/bowser/scrapy/bowserbot/course_browser_htmls/200201.txt", 
        # "file:///Users/lilian/Documents/2014/GitHub/bowser/scrapy/bowserbot/course_browser_htmls/200109.txt", 
        # "file:///Users/lilian/Documents/2014/GitHub/bowser/scrapy/bowserbot/course_browser_htmls/200107.txt", 
        # "file:///Users/lilian/Documents/2014/GitHub/bowser/scrapy/bowserbot/course_browser_htmls/200106.txt", 
        # "file:///Users/lilian/Documents/2014/GitHub/bowser/scrapy/bowserbot/course_browser_htmls/200102.txt", 
        # "file:///Users/lilian/Documents/2014/GitHub/bowser/scrapy/bowserbot/course_browser_htmls/200101.txt", 
        # "file:///Users/lilian/Documents/2014/GitHub/bowser/scrapy/bowserbot/course_browser_htmls/200009.txt", 
        # "file:///Users/lilian/Documents/2014/GitHub/bowser/scrapy/bowserbot/course_browser_htmls/200007"]

        ]


    def parse(self, response):
        self.log('A response from %s just arrived!' % response.url)
        for sel in response.xpath('//tbody'):
            course=sel.xpath('tr[1]/th[2]/text()').extract()
            crn=sel.xpath('tr[2]/th[2]/text()').extract()
            title=sel.xpath('tr[3]/th[2]/text()').extract()
            credit_hours=sel.xpath('tr[4]/th[2]/text()').extract()
            description=sel.xpath('tr[5]/th[2]/text()').extract()
            seats_available=sel.xpath('tr[6]/th[2]/text()').extract()
            max_enrollment=sel.xpath('tr[7]/th[2]/text()').extract()
            by_permission=sel.xpath('tr[8]/th[2]/text()').extract()
            prereq=sel.xpath('tr[9]/th[2]/text()').extract()
            dist=sel.xpath('tr[10]/th[2]/text()').extract()
            notes=sel.xpath('tr[11]/th[2]/text()').extract()
            prof=sel.xpath('tr[12]/th[2]/text()').extract()
            time_and_date=sel.xpath('tr[13]/th[2]/text()').extract()
            
            print course
            print crn
            print title
            print credit_hours
            print description
            print seats_available
            print max_enrollment
            print by_permission
            print prereq
            print dist
            print notes
            print time_and_date
            print 'end'


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

    # def test_and_pop(self, extracted_list):
    #     if len(extracted_list) == 0:
    #         return 'None assigned'
    #     elif len(extracted_list) == 1:
    #         return extracted_list.pop()
    #     else:
    #         string = extracted_list.pop().strip()
    #         for element in extracted_list:
    #             string = element.strip() + ',' + string
    #         # print string
    #         return string
        




    	
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







