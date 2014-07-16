# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.contrib.djangoitem import DjangoItem
from scrapy.item import Field
from courses.models import *

# class TutorialItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass

class DjangoCourseItem(DjangoItem):
	django_model = Course

class DjangoDistItem(DjangoItem):
	django_model = Distribution
	# Distribution.objects.all()
