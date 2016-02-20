#PayCalculator based on base and overtime pay
str_hours = raw_input('enter your hours:\n')
str_rate = raw_input('enter your rate:\n')
hours = float(str_hours)
rate = float(str_rate)
def computepay (hours,rate):
    ehours = hours - 40
    erate = rate * 1.5
    epay = ehours * erate
    return epay
    
if hours > 40:
    initialpay = 40 * rate
    additionalpay = computepay(hours,rate)
    totalpay = initialpay + additionalpay
else:
    totalpay = hours * rate
print totalpay