#Parsing HTML using urllib and beautiful soup
import re
import urllib
from bs4 import BeautifulSoup

url = raw_input('Enter the url\n')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
tags = soup('span')

sum = 0
for tag in tags:
	newtype = int(tag.contents[0])
	sum = sum + newtype
print sum
