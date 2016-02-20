#Pay calculator to determine pay based on base pay and overtime pay
hours = raw_input('Enter your hours worked:')
rate = raw_input ('Enter your hourly rate:')

try:
    if hours <= 40:
        pay = float(hours) * float(rate)
        print pay
    elif hours > 40:
        ehours = float(hours) - 40
        pay = (ehours) * (1.5 * float(rate)) + ((float(hours) - ehours) * float(rate))
        print pay       

except:
    print 'Enter a number'