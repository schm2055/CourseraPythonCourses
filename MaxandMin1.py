#Finding the max and min numbers of a list of user input numbers
maximum_num = None
minimum_num = None
while True:
    input = raw_input("Enter a number:\n")
    if input == 'done' or input == 'Done':
        break
    try:
        number = float(input)
    except:
        print 'Invalid input'
        continue
    if number > maximum_num:
        maximum_num = number
    elif minimum_num is None or number < minimum_num:
        minimum_num = number
    else:
        continue
print 'Maximum:',maximum_num,'Minimum:',minimum_num