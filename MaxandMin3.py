#finding the max and min from a list
input_list = []
while True:
	user_input = raw_input('Enter a number:\n')
	if user_input == 'done': break
	else:
		try:
			float_input = float(user_input)
		except:
			print 'enter a valid number'
		input_list.append(float_input)
	
try:
	maxnum = max(input_list)
	minnum = min(input_list)
	print 'The maximum number is',maxnum
	print 'The minimum number is',minnum
except:
	print 'no numbers were entered in this series'