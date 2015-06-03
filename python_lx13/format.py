#!/usr/bin/env python
#

a=1.556
print ("%.1f"% a) # 1.6

b = 561
print ("%06i" %b) # 000561


year = 2014
month = 1
day = 19
print ("%d-%d-%d " %(year,month,day)) # 2014-1-19
print "%d-%02d-%d " %(year,month,day) # 2014-01-19

####################################
def min_func (whatever):
    """ This function formats int values to thousandth with space
    (eg 1 223 333) and does the same for float values to the second
    place (eg 1 222 333,34) and returns an empty string for anything
    else. """

    if isinstance(whatever, int): # checks if the value is an integer
        return "{0:,d}".format(int(whatever)).replace(",", " ") # formats the integer and replaces the "," with " "
    elif isinstance(whatever, float):
        whatever = ("%.2f" % whatever) # convert to float with 2 decimal places
        whatever = float(whatever)
        whatever = format(whatever,",").replace(",", " ") # separate the thousands with spaces
        whatever = str(whatever) # convert to string
        whatever = whatever.replace(".", ",") # replace . with ,
        return whatever
    else:
        return "c"

print "#" *12
print min_func(2233123.435) # function calls
print min_func(123435)
print min_func("wenetr")

#############################################



paulena = raw_input("Enter a text: ")
if str(type(paulena)) == "<type 'str'>":
    print "get out!"
else:
    print "Get in!"
