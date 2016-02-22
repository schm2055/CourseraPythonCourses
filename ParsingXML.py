#Parsing XML with ElementTree
import urllib
import xml.etree.ElementTree as ET

url = raw_input('Enter the URL\n')
html = urllib.urlopen(url).read()
tree = ET.fromstring(html)
counts = tree.findall('.//comment')
countlist = list()
for count in counts:
	countlist.append(int(count.find('count').text))
print sum(countlist)
