#W4A3 - prompt users for hours and rate per hour to calculate gross pay

hours = raw_input('Enter the number of hours:\n')
rate = raw_input('Enter your rate:\n')
pay = float(hours) * float(rate)
print pay
