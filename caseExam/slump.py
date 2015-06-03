#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Olumuyiwa Falade
# LX13

# generates a random number between the range
# entered as argument to the script.

import random
import sys

def slumptal(a,b):
	minNum = a
	maxNum = b
	#minNum = int(minNum)
	#maxNum = int(maxNum)

	if minNum < maxNum: # tests if the first arg is less than the second arg
		newNum = random.randrange(minNum, maxNum) # generates a random number
		return newNum 	# return the random number
		
	else:	# if arg2 is lesser than arg1 prints the below and exit
		print ('Usage: {} minNumber maxNumber'.format(sys.argv[0]))
		return None
	


