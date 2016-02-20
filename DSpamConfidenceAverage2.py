#Finding the average Dspam confidence level of an email list
file = raw_input('Enter the file name\n')
if file == "na na boo boo":
	print "NA NA BOO BOO TO YOU - You have been Punk'd!"
	quit()
try:
	fhand = open(file, 'r')
except:
	print 'Enter a valid file name'
	quit()
string = raw_input('Enter the string you are looking for\n')
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