#read a file, and count specific words within the file to represent the number of times each file is read
filename = raw_input('Enter the file name:\n')
filehandle = open(filename, 'r')
daydict = dict()
for line in filehandle:
	if line.startswith('From '):
		stripline = line.strip()
		splitline = stripline.split()
		daydict [splitline[2]] = daydict.get(splitline[2], 0) + 1
print daydict
	