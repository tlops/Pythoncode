#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This script reads through any specified file and checks for the
# 100 most occurred words in the file.
# Falade O.T
import time
def openfil():
    try:
        fname = raw_input("Enter file name: ") # get file name
        if len(fname) < 1:          # if no name is entered
            fname = "aohf.txt"      # use default file
            fhandler = open(fname, 'r') # open the file for reading

        counting = dict()                      # empty Dictionary
        count = 0
        for lines in fhandler:      # read every line in the file
            lines = lines.rstrip()  # remove \n
            words = lines.split()   # separate every word on the line
            for word in words:      # reading through all word
                if word == []:      # avoid empty lines
                    continue # avoid empty lines
                word = word.lower() # conver words to lowercase
                word = specialtxt(word) # remove special characters
                counting[word] = counting.get(word, 0) + 1  # populate the dictionary
            count +=1
        fhandler.close() # close the file

    except: # IOError:
        print "WARNING: The file does not exist: "+fname

    # create a new list with the key. value of the dict
    lista =[]
    for key, value in counting.items():
        lista.append((value,key))

    #sort the list to arrange the 100 most common words
    lista.sort(reverse=True) # descending order
    asd = 1
    for elements in lista:
        if asd <= 100:
            print ("%d  %10s  %5d" % (asd,elements[1],elements[0]))
            asd +=1
    print ("\nThere are " + str(count)+ " lines in this Document.")



def specialtxt(txt):
    # this function help to remove special xters from words.
    specialist = ["'","!",",",";","?",";",".",":","_","-",'"',")","(","#","="]
    for i in specialist:
        if i in txt: # checks if word contains any special Xter
            txt = txt.replace(i,"") # then replaces the xter with no space
    # checks if there is a second special Xter
    for j in specialist: # checks if word contains any special Xter
        if j in txt:
            return txt.replace(j,"") # then replaces the xter with no space
        else:
            return txt

def main ():
    openfil()

if __name__=='__main__':
    main()

