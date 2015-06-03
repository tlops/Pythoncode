#
# This program takes in the number of hours and
# calculate the wage based on the hourly rate of
# $10.50/hr for hours below 40hrs and $15.75/hr
# (150%) for hours above 40.

hrs = raw_input("Enter your number of Hours!! \n")
rate = 10.50
try:
    hrs = float(hrs) # converts string to float
    if hrs <= 40:
        wage = rate * hrs
        print wage, "USD"
    elif hrs > 40:
        overtime = hrs - 40
        xtrapay = overtime * (1.5 * rate)
        wage = 40 * rate + xtrapay
        print wage, "USD"
except:
    print "Enter an number!!!"


