# This code calculates
#
def addme (a,b):
    add = a+b
    return add

def minusme (a,b):
    minus = a-b
    return minus

firstnum = raw_input("Enter the first number:\n")
firstnum= float(firstnum)
operat = raw_input("Enter your Operator:")
secondnum = raw_input("Enter your second number:\n")
secondnum = float(secondnum)

if operat == '+':
    ans = addme(firstnum,secondnum)
    print ans
elif operat == '-':
    ans = minusme(firstnum,secondnum)
    print ans
else:
    print "I can add or subtract"

