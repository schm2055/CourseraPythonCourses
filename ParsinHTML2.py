#Parsing HTML with BeautifulSoup
import re
import urllib
from bs4 import BeautifulSoup

url = raw_input('Enter url:\n ')
usercount = raw_input('Enter the count number\n')
userposition = raw_input('Enter the position you are interested in\n')
position = int(userposition)
count = int(usercount)
loopcount = 0

while True:
	if loopcount == 0:
		print "Retrieving:",url
		loopcount = loopcount + 1
	elif loopcount < count:
		html = urllib.urlopen(url).read()
		soup = BeautifulSoup(html, 'html.parser')
		tags = soup('a')
		linklist = list()
	
		for tag in tags:
			apptag = tag.get('href' , None)
			linklist.append(apptag)
		
		url = linklist[position - 1]
		print 'Retrieving:',url
		loopcount = loopcount + 1
	elif loopcount == count:
		html = urllib.urlopen(url).read()
		soup = BeautifulSoup(html, 'html.parser')
		tags = soup('a')
		linklist = list()
		for tag in tags:
			apptag = tag.get('href' , None)
			linklist.append(apptag)
		
		url = linklist[position - 1]
		break
print 'Final URL:',url
	