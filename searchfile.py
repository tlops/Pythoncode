#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 This scripts takes two argument, one a filename
 and the other the word you want to search.

 searchfile filename word
"""
import sys
import os

# sanity check
# The following block of code checks that the right amount
# of argument are entered along with the script.
if len(sys.argv)<3:
    print ('{} : Requires two argument'.format(sys.argv[0]))
    print ('Usage: {} filename word'.format(sys.argv[0]))
#    return (1)
    sys.exit()

# Declaration of argument
filename = sys.argv[1]
text  = ' '+sys.argv[2].lower() + ' ' # creates empty space around argument

main_count = 0  # line number count
text_line = 0   # interesting line count
try:
    fhandler =open(filename, 'r') # open file for reading

    for lines in fhandler: # iterate on each line
        main_count +=1      # increment line count
        lines = lines.rstrip().lower() # remove the extra new line and convert to lowercase
        if text in lines:   # match intresting lines
            text_line +=1   # count intresting lines
            print main_count, lines.index(text), lines # print out the line number,
                                        #position on line and the text on the line
    fhandler.close() # close the file.
    print ("\n\nThere are %d lines in this file and %d lines have: '%s' in them." % (main_count,text_line,text))
except:
    print ('There is no such file/directory: {}'.format(sys.argv[1])) # print error message.



