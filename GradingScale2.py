#Grading scale based on user input score
#ask for numerical score to be graded
grade = raw_input('Enter your numerical score\n')
#provide error checking with Try/Except
#use if, elif statements to capture correct grade per the score range
try:
    float_grade = float(grade)
    if float_grade >= 0.9:
        print 'A'
    elif float_grade >= 0.8:
        print 'B'
    elif float_grade >= 0.7:
        print 'C'
    elif float_grade >= 0.6:
        print 'D'
    elif float_grade < 0.6:
        print 'F'
#except provides suitable error message and ends gracefully
except:
    print 'Enter a numerical score'
    
    