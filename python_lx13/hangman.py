#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Falade Olumuyiwa Lx13  Written 12/08/2014
import random, sys

def openfiles():
    svenskordlista = []
    count = 0
    try:
        fil = open('svenskaord.txt')
        for lines in fil:
            lines = lines.rstrip()
            svenskordlista.append(lines)
            count +=1

        print count
        secretnum = random.randrange(0, count)
        secretword = svenskordlista[secretnum]
        print secretword
        return svenskordlista, secretword, secretnum
    except:
        print "ERROR: Cannot open the text document"
        sys.exit(1)

"""
def get_info():
    try:
        userguess = raw_input('Guess a letter in the secret word: ')
        return userguess
    except:
        print "WARNING: Alphabets shoulb be used, not intergers"
"""

def main():
    global svenskordlista
    wlist, sword, snum = openfiles()
    global wlist, sword, snum
    print sword,snum
    try:
        userguess = raw_input('Guess a letter in the secret word: ')
        print userguess
    except:
        print "WARNING: Alphabets shoulb be used, not intergers"

    l = []
    wrdlen = len(sword) + 2
    itr = 0
    if wrdlen > 1:
        for i in range(len(sword)):
            l.append('_')
        for stre in l:
            print stre,
            print "You have {} guesses! ".format(wrdlen)
        #a = get_info()
        if a in sword:
            b=sword.find(a)
            pass



#    get_info()

main()

