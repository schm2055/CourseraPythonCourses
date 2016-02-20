#Created a script to determine the most frequent email sender from an email list
name = raw_input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
filehandle = open(name)
sender_list = dict()
mostsent = 0
highestsender = None
for line in filehandle:
    if line.startswith('From '):
        stripline = line.strip()
        splitline = stripline.split()
        sender = splitline[1]
        sender_list[sender] = sender_list.get(sender, 0) + 1
for sender in sender_list:
    if sender_list[sender] > mostsent:
        mostsent = sender_list[sender]
        highestsender = sender
print highestsender, mostsent
