#Working with regular expressions
import re
filename = raw_input('Enter your file name\n')
if len(filename) < 1:
	filename = 'regex_sum_212672.txt'
filehandle = open(filename, 'r')
numlist = list()
for line in filehandle:
	stripline = line.strip()
	desiredvalue = re.findall('[0-9]+', stripline)
	if len(desiredvalue) > 0:
		for value in desiredvalue:
			numlist.append(int(value))
print sum(numlist)
print len(numlist)