# This program gives the grade to a score as
# entered by the user. "0.9 = A, 0.8 = B, 0.7
# = C, 0.6 = D, < 0.6 = F. If the user enters
# a wrong value a report is generated to the
# screen. we use "try" and "except".

input1 = raw_input("Enter the score: \n")

try:
    input1 = float(input1)
    if input1 >= 0.9:
        print "A"
    elif input1 >= 0.8:
        print "B"
    elif input1 >= 0.7:
        print "C"
    elif input1 >= 0.6:
        print "D"
    elif input1 < 0.6:
        print "F"
except:
    print "Enter a float!!"

