#Obtain senders of emails from a document and input them into a dictionary
filename = raw_input('Enter your file name:\n')
filehandle = open(filename,'r')
namedict = dict()
for line in filehandle:
	if line.startswith('From '):
		stripline = line.strip()
		splitline = line.split()
		isolatesender = splitline[1]
		slicesender = isolatesender[isolatesender.find('@') + 1:]
		namedict[slicesender] = namedict.get(slicesender, 0) + 1
print namedict