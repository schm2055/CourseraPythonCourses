#loop through a file with email records, determine the person that sends the most emails and print who the person is and how many emails they sent
name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
mail = dict()
clist = list()
eperson = 0
fperson = None
for line in handle:
    if not line.startswith('From'): continue
    elif line.startswith('From:'): continue
    else:
    	sline = line.strip()
        tline = sline.split()
	fline = tline[1]
	clist.append(fline)
for person in clist:
	mail[person] = mail.get(person,0) + 1
for person in mail:
	if mail[person] > eperson:
		eperson = mail[person]
		fperson = person
print fperson,eperson
	