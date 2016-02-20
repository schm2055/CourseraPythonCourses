#Finding the amount of lines that start with the word 'from'
file = raw_input('enter file name:\n')
fhand = open(file, 'r')
count = 0
for line in fhand:
	line = line.strip()
	if not line.startswith('From'): continue
	elif line.startswith('From:'): continue
	else:
		sline = line.split()
		print sline[1]
		count = count +1
print 'there were',count,"in the file with the first word of 'from'"