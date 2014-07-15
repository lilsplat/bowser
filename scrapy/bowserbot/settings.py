# -*- coding: utf-8 -*-

# Scrapy settings for tutorial project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

import sys
#set up django project path
sys.path.insert(0, '/Users/lilian/Documents/2014/GitHub/bowser')

import os
#set up django settings module name
os.environ['DJANGO_SETTINGS_MODULE'] = 'bowser.settings'

BOT_NAME = 'bowserbot'

SPIDER_MODULES = ['bowserbot.spiders']
NEWSPIDER_MODULE = 'bowserbot.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tutorial (+http://www.yourdomain.com)'
