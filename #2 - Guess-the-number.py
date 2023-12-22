# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

# initialize global variables used in your code
num_range = 100
secret_number = 0
num_guesses = 0

# helper function to start and restart the game
def new_game():
    global secret_number
    global num_guesses
    
    # print a blank line to seperate consecutive games
    print
    
    print "New game. Range is from 0 to", num_range
    
    # calculate guesses allowed
    num_guesses = int(math.ceil(math.log(num_range,2)))
    
    print "Number of remaining guesses is", num_guesses
    
    secret_number = random.randrange(0, num_range)
    #print "secret", secret_number
    
# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global num_range
    num_range = 100
    new_game()
   
    

def range1000():
    # button that changes range to range [0,1000) and restarts
    global num_range
    num_range = 1000
    new_game()
   
    
    
def input_guess(guess):
    # main game logic goes here	
    global secret_number
    global num_guesses
    
    print
    print "Guess was", guess
    num_guesses = num_guesses - 1
    print "Number of remaining guesses is", num_guesses
  
    if num_guesses > 0:
        guess = float(guess)
        if guess == secret_number:
            print "Correct!"
            new_game()
        elif guess > secret_number:
            print "Lower!"
        elif guess < secret_number:
            print "Higher!"
    
    elif num_guesses == 0:
        print "You ran out of guesses. The number was", secret_number
        new_game()
    
        
    
# create frame
f = simplegui.create_frame("Guess the number", 200, 200)


# register event handlers for control elements
f.add_button("Range is [0,100)", range100, 200)
f.add_button("Range is [0,1000)", range1000, 200)
f.add_input("Enter a guess", input_guess, 200)


# call new_game and start frame
new_game()


# always remember to check your completed program against the grading rubric
