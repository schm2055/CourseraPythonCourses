#Sorting a list
file = raw_input('enter your file name\n')
fhand = open(file,'r')
wordlist = []
for line in fhand:
	words = line.split()
	for word in words:
		booword = word in wordlist
		if booword is False:
			wordlist.append(word)
wordlist.sort()
print wordlist

