""" This is a Guess what game
    The computer generates a random number
    while you try to guess the number. you
    get clues as what your choice is higer
    or lower than the secret number. 
"""

import random
num_guess = 7
counter = 0
total = 10
def new_game():
   print "\nNew Game: Range is 1-100: "
   global secret_number
   secret_number = random.randrange(0,100)
   input_guess()


def input_guess():
   global guess, secret_number, num_guess, counter
   #guess = raw_input("Enter your Guess: ")
   #guess = int(guess)
   while counter <= total:
      try:
         guess = raw_input("Enter your Guess: ")
         #if guess == 'Exit' or 'exit':
         #   print "Bye!"
         #   quit()
         #else:
         guess = int(guess)
         if guess < secret_number:
            response = " is Lower!"
         elif guess > secret_number:
            response = " is Higher!"
         else:
            response = "Right!"
         print guess, response
         num_guess -=1
         print "You have ", num_guess, "guesses left!\n"
         if num_guess == 0:
            print "You Lost!"
            print "The secret Number is: ", secret_number
            control()
         elif response == "Right!":
            print "Congratulations, You Won!"
            control()
         counter=counter+1

      except:
         print "Enter an integer number!"

def control():
   global num_guess, counter, total
   try:
      answer = raw_input("\nDo you want to continue with\nthe game? Type 'Yes!' or No!")
      if answer == "Yes" or "yes":
         num_guess = 7
         counter = 0
         total = 10
         new_game()
      elif answer == "No" or answer == "no":
         print "\nBye!"
         quit()

   except:
      print "Enter Yes or No..."



new_game()
