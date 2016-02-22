#read a file and count specific words to make a key:value pair to determine what words are most frequently used
filename = raw_input('Enter your file name:\n')
filehandle = open(filename,'r')
namedict = dict()
for line in filehandle:
	if line.startswith('From '):
		stripline = line.strip()
		splitline = line.split()
		namedict[splitline[1]] = namedict.get(splitline[1], 0) + 1
print namedict