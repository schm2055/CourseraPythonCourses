#Determine determine the most frequent sender in a document using a dictionary
filename = raw_input('Enter your file name:\n')
filehandle = open(filename,'r')
namedict = dict()
count = 0
highestperson = None
for line in filehandle:
	if line.startswith('From '):
		stripline = line.strip()
		splitline = line.split()
		namedict[splitline[1]] = namedict.get(splitline[1], 0) + 1
		for name in namedict:
			if namedict[name] > count:
				count = namedict[name]
				highestperson = name	
print highestperson, count