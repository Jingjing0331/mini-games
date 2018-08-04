# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random

# initialize global variables used in your code
count = 0
secret_num = 0
dis_range = True


# helper function to start and restart the game
def new_game(): 
    global count, secret_num
    # range discrimination
    if dis_range:
        secret_num = random.randrange(0,100)
        count = 7
        print "New game. Range is from 0 to 100"
        print "Number of remaining guesses is", count
        print ""
    else:
        secret_num = random.randrange(0,1000)
        count = 10
        print "New game. Range is from 0 to 1000"
        print "Number of remaining guesses is", count
        print ""
        


# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global dis_range
    dis_range = True
    new_game()    
    

def range1000():
    # button that changes range to range [0,1000) and restarts
    global dis_range
    dis_range = False
    new_game()
   
    
def input_guess(guess):
    # main game logic goes here	
    global count, secret_num
    guess = int(guess)
    count = count - 1
    print "Guess was", guess
    print "Number of remaining guesses is", count
    if count > 0:
        if guess > secret_num:
            print "Lower!"
            print ""
        elif guess < secret_num:
            print "Higher!"
            print ""
        else:
            print "Correct!"
            print ""
            new_game()
    else:
        if guess == secret_num:
            print "Correct!"
            print ""
            new_game()
        else:
            print "You ran out of guesses. The Number was", secret_num
            print ""
            new_game()
    

    
# create frame
frame = simplegui.create_frame("Guess the Number", 200, 200)


# register event handlers for control elements
frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)
frame.add_input("Enter a guess", input_guess, 200)


# call new_game and start frame
new_game()
frame.start()


# always remember to check your completed program against the grading rubric
