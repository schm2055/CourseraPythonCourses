#Grading calculator that determines a grade based on a score
stringgrade = raw_input ('Enter your score 0.0-1.0:')

try:
    grade = float(stringgrade)
    if grade < 0 or grade > 1:
        print 'Grade outside of range'
    elif grade >= 0.9:
        print 'A'
    elif grade >= 0.8 and grade < 0.9:
        print 'B'
    elif grade >= 0.7 and grade < 0.8:
        print 'C'
    elif grade >= 0.6 and grade < 0.7:
        print 'D'
    else:
        print 'F'
except:
    print 'Bad Entry. Enter in numerical grade.'