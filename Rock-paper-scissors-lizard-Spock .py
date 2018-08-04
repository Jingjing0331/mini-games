# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random

# helper functions

def number_to_name(number):
    # fill in your code below
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        return "is not in the correct range"
    # convert number to a name using if/elif/else
    # don't forget to return the result!

    
def name_to_number(name):
    # fill in your code below
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        return -1
    # convert name to number using if/elif/else
    # don't forget to return the result!

# the main function

def rpsls(name): 
    # fill in your code below

    # convert name to player_number using name_to_number
    player_guess = name_to_number(name)

    # compute random guess for comp_number using random.randrange()
    computer_guess = random.randrange(0,5)

    # compute difference of player_number and comp_number modulo five
    if 0 <= player_guess <= 4 and 0 <= computer_guess <= 4:
        distance = (player_guess - computer_guess) % 5

    # use if/elif/else to determine winner
        if distance == 0:
            winner = "Player and Computer tie!"
        elif distance <= 2:
            winner = "Player wins!"
        elif 2 < distance <= 4:
            winner = "Computer wins!"
        else:
            winner = "Distance Error!"

    # convert comp_number to name using number_to_name
        player_guess = number_to_name(player_guess)
        computer_guess = number_to_name(computer_guess)
        
    
    # print results
        print "Player chooses ", player_guess
        print "Computer chooses ", computer_guess
        print winner
        print ""
    else:
        print "Input Error!"
        print "Player_guess", number_to_name(player_guess)
        print "Computer_guess", number_to_name(computer_guess)
        print ""
        
    

    
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


