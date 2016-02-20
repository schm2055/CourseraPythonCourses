#Script to search through JSON, find a comment represented in an integer, and determine the sum of all comments in the JSON document
import urllib
import json
url = raw_input('Enter URL:\n')
html = urllib.urlopen(url).read()
info = json.loads(html)
numlist = list()
for entry in info['comments']:
    numlist.append(entry['count'])
print sum(numlist)
