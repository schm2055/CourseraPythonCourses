#Practice creating a function
str_hours = raw_input('Enter your hours worked\n')
str_rate = raw_input('Enter your rate\n')
def computepay(hours, rate):
    if hours <= 40:
        pay = hours * rate
    else:
        ehours = hours - 40
        erate = rate * 1.5
        pay = (rate * 40) + (ehours * erate)
    print pay

try:
    hours = float(str_hours) 
    rate = float(str_rate)
    computepay (hours, rate)
except:
    print 'Enter a valid number for hours and/or rate'