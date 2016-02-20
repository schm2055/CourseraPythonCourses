#Practice creating a function
str_score = raw_input('Enter your score (0.0 - 1.0):\n')
def computegrade (score):
    if score < 0 or score > 1:
        print 'grade outside of range. Enter a valid score.'
    elif score >= .9:
        print 'A'
    elif score >= .8:
        print 'B'
    elif score >= .7:
        print 'C'
    elif score >= .6:
        print 'D'
    elif score < .6:
        print 'F'

try: 
    score = float (str_score)
    computegrade (score)
except:
    print 'Enter a valid number for your grade'