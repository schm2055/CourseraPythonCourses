#read a file and create a dictionary based on particular words to make a key:value pair
filename = raw_input('Enter your file name:\n')
filehandle = open(filename, 'r')
word_dict = dict()
for line in filehandle:
	stripline = line.strip()
	splitline = stripline.split()
	for word in splitline:
		word_dict[word] = 1
print word_dict

