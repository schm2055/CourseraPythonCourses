#Practice with functions
def chop(t):
	del t[0]
	del t[len(t)-1]
	print t
def middle(t):
	f = t[1:len(t)-1]
	print f
	
t = [0,1,2,3,4,5]

#chop(t)
print len(t)
middle(t)
