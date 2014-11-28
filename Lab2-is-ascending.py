#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" checks if the numbers are in ascending order """

def is_ascending(numbers):
     """Returns whether the given list of numbers is in ascending order."""
     for i in range(len(numbers)-1):
         if numbers[i+1] < numbers[i]: # checks if the next number is lesser than the current number
             return False 				# returns false if the above is true
     return True						# returns true if the condition is false

# declared two Lists to test the function
list1= [1,2,3,4,56,7,89,9]
list2= [2,4,5,6,7,8,9]

# calling the function
print is_ascending(list1)
print is_ascending(list2)

 #########################################################

def checkString(string):
    a= string
    count={} 	# empty dictionary

    for i in a: # for every character in a
        count[i]=count.get(i,0)+1		# if the Xter is present then increase it by 1
    for key, value in count.items():
       print key,value


checkString('ciccinnati')

######################################################
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
