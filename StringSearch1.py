#Search for a string within a file
file = raw_input('Enter the file name\n')
string = raw_input('Enter the string you are looking for\n')
fhand = open(file, 'r')
count = 0
total = 0
for line in fhand:
	if line.startswith(string):
		startchar = line.find(':')
		rawnum = line[startchar+1:]
		floatnum = float(rawnum)
		total = total + floatnum
		count = count + 1
average = total / count
print 'Average Spam Confidence: ',average