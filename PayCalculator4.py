#Pay calculator based on base and overtime hours

#Ask for hours
hours = raw_input ('Enter your hours:\n')
#Convert to a float
float_hours = float(hours)
#Ask for pay rate
rate = raw_input('Enter your hourly rate:\n')
#convert to a float
float_rate = float(rate)
#conditional to provide pay based on number of hours worked (40+ is 1.5 time)
if float_hours <= 40:
    pay = float_hours * float_rate
    print pay
else:
    extra_hours = float_hours - 40
    pay = (extra_hours * (float_rate *1.5)) + ((float_hours - extra_hours) * float_rate)
    print pay
