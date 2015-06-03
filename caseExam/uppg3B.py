#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Olumuyiwa Falade
# LX13
# this script takes three arguments 
# arg1 = how many numbers to print out
# arg2 = minimum number
# arg3 = maximum number
# it prints out arg1 numbers from a random range arg2 and arg3
# it also uses the module "slump".

import random
import sys
from slump import *

def test():
	lista =[]	# make an empty list to store the numbers
	if len(sys.argv)<4: # checks to make sure that the two arguments are entered
	        print ('{} : Requires THREE argument'.format(sys.argv[0]))
	        print ('Usage: {} amtNumbers minNumber maxNumber'.format(sys.argv[0]))
	        return (1)
	        sys.exit()	# exits the system if the requirement is not fulfilled
	
	try:
		amtNum = sys.argv[1]
		miniNum = sys.argv[2]
		maxiNum = sys.argv[3]
		
		miniNum = int(miniNum)
		maxiNum = int(maxiNum)
		amtNum = int(amtNum)
		while True:
			if miniNum < maxiNum: # tests if the first arg is less than the second arg
				for i in range(amtNum):
					new = slumptal(miniNum, maxiNum) # generates a random number
					lista.append(new)
				lista.sort()
				for i in lista:
					print i
				break # stops the loop

			else:	# if arg2 is lesser than arg1 prints the below and exit
				print ('Usage: {} minNumber maxNumber'.format(sys.argv[0]))
				sys.exit(1)
	except ValueError:	# catches non numerical argument
		print "Warning: Enter interger as argument"

test()


