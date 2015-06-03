#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Olumuyiwa Falade
# LX13

# This is a Translation game.

import sys

global wordlist
wordlist = []
try:
		
	fname = open('glosor.txt','r')
	for lines in fname:
		lines = lines.rstrip()
		words = lines.split()
		wordlist.append(words)
		#print words
		#for word in words:
		#	print word
	fname.close()

except:
	print "The file does not exist"


#print wordlist

def sve_eng():
	score = 0 # the score
	lost = 0  # the misse
	global wordlist # list of words and transation
	missedlist = [] # list of words that was missed
	for elements in wordlist: # Loop thru wordlist
		sve = elements[0].lower() # makes the first element in each list lowercase
		try:
			response = raw_input("Convert this word: '{}' to English: ".format(sve)) # take user input
			response = response.lower() # makes user input lowercase
			if response == elements[1]: # Checks if the Translation matches 
				score +=1 # increase score
			else: # if not
				missedlist.append((elements[0], elements[1])) # adds the misse ones to  new list
				lost +=1 # count missed score 
		except:
			print "Enter Character only!\n"

	print "Your Total score is: ", score # prints outs score
	if len(missedlist) == 0: # checks if none was missed
		print "Congratultions You Got all right!"
	else: # if you missed some
		print "You missed: {}".format(lost)		
		print "These are the ones you Missed\n"
		for missed in missedlist: # loop though the miss list.
			print "Swedish: {} To English: {}".format(missed[0], missed[1])
		

def eng_sve():
	score = 0 # the score
	lost = 0  # the misse
	global wordlist # list of words and transation
	missedlist = [] # list of words that was missed
	for elements in wordlist: # Loop thru wordlist
		eng = elements[1].lower() # makes the second element in each list lowercase
		try:
			response = raw_input("Översätt ordet: '{}' till Svenska: ".format(eng))
			response = response.lower() # makes user input lowercase
			if response == elements[0]: # Checks if the Translation matches
				score +=1 # increase score
			else: # if not
				missedlist.append((elements[0], elements[1])) # adds the misse ones to  new list
				lost +=1 # count missed score
		except:
			print "Enter Character only!\n"

	print "Your Total score is: ", score # prints outs score
	if len(missedlist) == 0: # checks if none was missed
		print "Grattis! Du fick alla rätt! :)"
	else:
		print "Du Missat: {}".format(lost)		
		print "Orden som du Översätte fel var:"
		for missed in missedlist: # loop though the miss list.
			print "Engelska: {} Svenska: {}".format(missed[1], missed[0])


def main():
	print "1. Svenska till Engelska"
	print "2. Engelska till Svenska"
	print "3. To Quit"
	choice = raw_input("Vad vill du göra? ") # makea choice
	choice = int(choice) # convert to int
	
	if choice == 1:
		sve_eng()
	elif choice == 2:
		eng_sve()
	else:
		print "No choice taken! exiting... "
		sys.exit() # exits the system

if __name__ =='__main__':
	main()
