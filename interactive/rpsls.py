# Rock-paper-scissors-lizard-Spock template

import random
import math

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# User input
print "\nrock, paper, scissors, lizard, Spock"

global players_choice
# helper functions

def name_to_number(name):
    # This function converts the player_choice to number
    if name == 'rock' or 'Rock':
        number = 0
        return number
    elif name == 'paper' or 'Paper':
        number = 1
        return number
    elif name == 'scissors' or 'Scissors':
        number = 2
        return number
    elif name == 'lizard' or 'Lizard':
        number = 3
        return number
    elif name == 'Spock' or 'spock':
        number = 4
        return number
  #  elif name == 'Exit' or 'exit':
#     quit()
    else:
        print "Error: Rock, Spock, Lizard, Scissors, Paper"



# convert name to number using if/elif/else
#don't forget to return the result!
def number_to_name(number):
# This function converts the comp_number to name
    if number == 0:
        name = "rock"
        return name
    elif number == 1:
        name = "paper"
        return name
    elif number == 2:
        name = "scissors"
        return name
    elif number == 3:
        name = "lizard"
        return name
    elif number == 4:
        name = "Spock"
        return name
    else:
        print "Error!"
                                                                                                                                               # convert number to a name using if/elif/else
# don't forget to return the result!
def rpsls(player_choice):
    print ""
    # print out the message for the player's choice
    global record
    print "Player chooses ", player_choice

    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)

    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 5)
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    # print out the message for computer's choice
    print "Computer chooses ", comp_choice
    # compute difference of comp_number and player_number modulo five
    final = (comp_number - player_number) % 5
    # use if/elif/else to determine winner, print winner message
    if final == 1 or final == 2:
        #print "Computer wins!"
        record = "Computer wins!"
    elif final == 3 or 4:
        #print "Player wins!"
        record = "Player wins!"
    elif final == 0:
        #print "Player and computer tie!"
        record = "Player and computer tie!"
    return record


def statistics(each_win):
# This function count how many times the player or the
# computer wins to determine the overall winner!
    global record
    board = dict()

count = 20
i = 0
lista = ["rock","Rock", "Paper", "paper", "Scissors", "scissors", "Lizard", "lizard", "Spock", "spock"]

#for i in 1,2,3,4,5:
while i<=count:
    players_choice = raw_input("\nEnter your Choice! ")

    if players_choice in lista:
        print rpsls(players_choice)

    elif players_choice == 'Exit' or players_choice == 'exit':
        print "Bye!"
        break
    elif players_choice not in lista:
        print "rock, paper, scissors, lizard, Spock"
i+=1




# THESE CALLS MUST BE PRESENT IN YOUR SU)
# always remember to check your completed program against the grading rubric
#rpsls(players_choice)
#rpsls("rock")
#rpsls("Spock")
#rpsls("scissors")
#rpsls("lizard")
#rpsls("paper")
