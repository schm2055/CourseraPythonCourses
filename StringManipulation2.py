#String manipulation practice
# Use words.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)
for line in fh:
    line = line.rstrip()
    upperline = line.upper()
    print upperline
    