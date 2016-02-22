#Navigating through multiple web pages and selecting a specific link from a page then repeating the process
import urllib
import re
#ask for user inputs
url = raw_input('Enter url:\n ')
usercount = raw_input('Enter the count number\n')
position = raw_input('Enter the position you are interested in\n')
#read html link from user input and pull out all nested links in web page
count = int(usercount)
loopcount = 0
newlink = None
newlinks = list()

while True:
	if loopcount < 1:
		print 'Retrieving', url
		loopcount = loopcount + 1
	elif loopcount == 1:
		html = urllib.urlopen(url).read()
		newlinks = re.findall('href="(https://.*?)"', html)
		newlink = newlinks[int(position) - 1]
		print 'Retrieving', newlink
		loopcount = loopcount + 1
	elif loopcount > 1 and loopcount < count:
		html = urllib.urlopen(newlink).read()
		newlinks = re.findall('href="(https://.*?)"', html)
		try:
			newlink = newlinks[int(position) - 1]
			print 'Retrieving',newlink
			loopcount = loopcount + 1
		except:
			newlink = newlinks[1]
			print 'Retrieving4',newlink
			loopcount = loopcount + 1
	elif loopcount == count:
		html = urllib.urlopen(newlink).read()
		newlinks = re.findall('href="(https://.*?)"', html)
		try:
			newlink = newlinks[int(position) - 1]
			loopcount = loopcount + 1
			break
		except:
			newlink = newlinks[1]
			loopcount = loopcount + 1
			break
print 'Last URL',newlinks[int(position) - 1]
