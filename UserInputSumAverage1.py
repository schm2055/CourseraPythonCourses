#creating a sum and average of user input numbers
count = 0
n_sum = 0
while True:
    string_number = raw_input('Enter a number:\n')
    if string_number == 'Done' or string_number == 'done':
        break 
    try:
        number = float(string_number)
    except:
        print 'Invalid input'
        continue
    count = count + 1
    n_sum = n_sum + number
    average = n_sum / count
print n_sum,count,average
    

