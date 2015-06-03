#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Olumuyiwa Falade
# LX13
# Skriv ut ett heltal



def test():
	while True:	# a while loop to ensure continuity
		try:	# to enable only numerical input value
        		thenum = input("Enter an integer: ") # Take in a value from keyboard
        		if isinstance(thenum, int):     # check if the value is an integer
                		print thenum            # prints out the number
				break
				
        		else:                           # if it is not an integer
        	        	print "WARNING: not a valid input!"
		except:                                 # catches the error due to non- numerical input
        		print "Try Again: Enter an integer Value!"

test()


