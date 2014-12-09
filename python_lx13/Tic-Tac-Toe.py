#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 This is a version of the popular Tic-Tac-Toe game!
 Players use Nos 1-9 to represent the location to play
 on screen.
 function draw_board draws the current board status wh-
 ich is represented by a list (a). each element from the
 list represent a position on the board. 
 function 'check_win' checks the state of the board against
 the 'win_condition' to find  a match.
 function 'get_input' gets the right input from the players 
"""
import random
import sys
import os
a = range(10)

def draw_board():
     # This functn draws the board using a list that has each
     # element represent a box on the board.
     print ("A   B   C ")
     print a[1], '|', a[2], '|', a[3]
     print ("----------")
     print a[4], '|', a[5], '|', a[6]
     print ("----------")
     print a[7], '|', a[8], '|', a[9]

def instruction():
    # This function gives instruction on how to play the game.
    print ("1 | 2 | 3")
    print ("----------")
    print ("4 | 5 | 6")
    print ("----------")
    print ("7 | 8 | 9")
    print "Use the numbers to choose your location"
    print "Enter Nos <1-9> to choose the position to play"
    print ""
    print ""


def check_win ():
    # This function checks for wins
    win_condition = ((1,2,3), (4,5,6), (7,8,9), (1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)) # a list of possible winning combination
    #check if X wins
    for each in range(len(win_condition)): # iteration over the main list
        row = 0
        for element in win_condition[each]: # iteration over the elements in each element in the main list (1,2,3)
            if a[element] == 'X': # checks if the element have the same character: X
                row +=1		  # increase the counter
                if row ==3:	  # if 3 are the same
                    print "X wins!"  # print winner
                    sys.exit()

    # Checks if O wins
    for each in range(len(win_condition)): # iteration over the main list
        row = 0				    # set counter
        for element in win_condition[each]: # iteration over the elements in each element in the main list (1,2,3)
            if a[element] == 'O': 	    # checks if the element have the same character: O
                row +=1  		    # increase the counter
                if row == 3:		    # if 3 are the same
                    print "O wins!"	    # print winner
                    sys.exit()		    # exit

def get_input(player):
    global user		# user input made global
    checkMark = True
    while checkMark == True:
        try:		# handle error in a good way
            user = input(player)	# take in user's choice
            if user >= 1 and user <=9:	# it must be between 1 and 9
                if  isinstance(a[user], int): # check if the space is free
                    break
                else:
                    print "That Position is Occupied!" # if occupied it returns this message
            else:
                print "Use numbers <1-9> to choose your Position!"
        except Exception as e:
            print "This is not a Valid Move!"

			
def main():
    instruction()
    nr = 1	# we set the state to 1
    count = 0	# set counter to 0
    while count <= 8: # when counter is less than or equal to 8
        if nr == 1: 
            draw_board()		# calls the draw function
            get_input('X plays: ')	# call the get_input funtn with X
            a[user] = 'X'		# places X in the position chosen by player
            nr +=1			# increase the state to 2, to pass play to player O
            os.system('clear')		# clears the screen
            check_win()			# check if there is a winner
            count +=1			# increment counter
        else:
            draw_board()		# calls the draw function
            get_input('O plays: ')	# call the get_input funtn with O
            a[user] = 'O'		# places O in the position chosen by player
            nr -=1			# decrease the state to , to pass back play to player X
            os.system('clear')		# clears the screen
            check_win()			# check if there is a winner
            count +=1			# increment counter
    print "No winner!"			# if the check_win function does not halt the game, it means no winner!

if __name__=='__main__':
    main()
