#String practice
file = raw_input('Enter your file name\n')
fhand = open(file, 'r')
for line in fhand:
    line = line.rstrip()
    print line.upper()
	