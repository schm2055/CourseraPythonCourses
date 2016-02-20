#Determine the max and min from a list of user input numbers
maximum_num = None
minimum_num = None
while True:
    input = raw_input("Enter a number:\n")
    if input == 'done' or input == 'Done':
        break
    try:
        number = int(input)
    except:
        print 'Invalid input'
        continue
    if number > maximum_num:
        maximum_num = number
    if minimum_num is None or number < minimum_num:
        minimum_num = number
print 'Maximum is',maximum_num
print 'Minimum is',minimum_num