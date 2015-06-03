#
# This program takes in the number of hours and
# rate then calculate the wage based on the given
# rate for hours below 40hrs and  (150%) for hours
# above 40.

def computepay (h,r): # define a function
    if h <= 40:
        wage = r * h
        return wage
    elif h > 40:
        overtime = h - 40
        xtrapay = overtime * (1.5 * r)
        wage = 40 * r + xtrapay
        return wage    # End of function


hrs = raw_input("Enter your number of Hours: \n")
rate = raw_input("Enter the hourly rate: \n")
try:
    hrs = float(hrs) # converts string to float
    rate = float(rate) # converts string to float

    pay = computepay (hrs,rate) # calls the function
    print pay, "USD"
except:
    print "Enter an number!!!"


