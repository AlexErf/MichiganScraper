#!/usr/bin/python

import urllib2
from bs4 import BeautifulSoup

schedule_page = 'http://www.espn.com/college-football/team/schedule/_/id/130'
page = urllib2.urlopen(schedule_page)

soup = BeautifulSoup(page, 'html.parser')

time = soup.find(id='showschedule').find(class_='tablehead').contents[2].contents[0].get_text()
opponent = soup.find(id='showschedule').find(class_='tablehead').contents[2].find(class_='team-name').find('a').get_text()
status = soup.find(id='showschedule').find(class_='tablehead').contents[2].find(class_='game-status').get_text()

print time + ' ' + opponent + ' ' + status

# print(soup.find(id='showschedule').find(class_='tablehead').contents[2].find(class_='game-schedule').prettify())
