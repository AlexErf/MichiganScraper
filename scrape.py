#!/usr/bin/python

import urllib2
from bs4 import BeautifulSoup

schedule_page = 'http://www.espn.com/college-football/team/schedule/_/id/130'
page = urllib2.urlopen(schedule_page)

soup = BeautifulSoup(page, 'html.parser')

time = soup.find(id='showschedule').find(class_='tablehead').contents[2].contents[0].get_text()
print(soup.find(id='showschedule').find(class_='tablehead').contents[2].prettify())

