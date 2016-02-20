#find the average x-dspam-confidence level based on email list values
# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    else:
        find = line.find(':')
        snum = line[find + 1:]
        fnum = float(snum)
        count = count + 1
        total = total + fnum
average = total / count
print 'Average spam confidence:', average