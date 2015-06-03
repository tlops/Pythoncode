#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Olumuyiwa Falade
# LX13

while True:
    name = raw_input ( "What is your name?" ) # Ask for name

    if name != "": # Check that a name has been entered
        print "Hello ", name # Print out a greeting
        break # Exit the loop
    else: # Check if no name has been entered
        print "You did not enter a name. Please try again"

print "Goodbye!" # Say goodbye before the application exits
