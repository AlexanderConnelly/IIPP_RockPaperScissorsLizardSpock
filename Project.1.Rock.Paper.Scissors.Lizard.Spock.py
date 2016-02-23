 # Rock-paper-scissors-lizard-Spock 
import random 
import simplegui
# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors
# global variables:
global player_score 
global computer_score
player_score = 0
computer_score = 0



# helper functions

def name_to_number(name):
    if name =="rock":
        number = 0
    elif name =="Spock":
        number = 1
    elif name =="paper":
        number = 2
    elif name =="lizard":
        number = 3
    elif name =="scissors":
        number = 4
    else:
        print "Error: Input not 'rock', 'Spock', 'paper', 'lizard', or 'scissors'"
        number = 5
    return number    
    
    # convert name to number using if/elif/else
    # don't forget to return the result!


def number_to_name(number):
    if number == 0:
        name="rock"
    elif number == 1:
        name="Spock"
    elif number == 2:
        name="paper"
    elif number == 3:
        name="lizard"
    elif number == 4:
        name="scissors"
    else:
        print "Error: Input not 0,1,2,3, or 4."
    return name
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    

def rpsls(player_choice): 
    global player_score,computer_score
    # print a blank line to separate consecutive games
    print ""
    # print out the message for the player's choice
    print "Player Chooses",player_choice
    # convert the player's choice to player_number using the function name_to_number()
    player_number=name_to_number(player_choice)
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    # print out the message for computer's choice
    print "Computer Chooses",comp_choice
    # compute difference of comp_number and player_number modulo five
    mod=(comp_number-player_number)%5
    # use if/elif/else to determine winner, print winner message
    if mod==0:
        global player_score
        print "Player and computer tie!"
        print "Player Score:",player_score,"Computer Score:",computer_score
    elif mod ==4 or mod== 3:
        print "Player Wins!"
        #global player_score
        player_score+=1
        
        print "Player Score:",str(player_score),"Computer Score:",str(computer_score)
    elif mod ==1 or mod == 2:
        print "Computer Wins!"
        #global computer_score
        computer_score+=1
        print "Player Score:",str(player_score),"Computer Score:",str(computer_score)
    elif player_number == 5:
        print "WRONG INPUT!"
def rock_handler():
    rpsls("rock")
def paper_handler():
    rpsls("paper")
def scissors_handler():
    rpsls("scissors")
def lizard_handler():
    rpsls("lizard")
def spock_handler():
    rpsls("Spock")

    
#def draw_handler(canvas):
    
    


    
frame = simplegui.create_frame("Rock Paper Scissors Lizard Spock", 200, 200)
frame.add_button("Rock", rock_handler)
frame.add_button("Paper", paper_handler)
frame.add_button("Scissors", scissors_handler)
frame.add_button("Lizard", lizard_handler)
frame.add_button("Spock", spock_handler)
frame.add_input("Rock Paper Scissors Lizard Spock", rpsls, 100)
#frame.set_draw_handler(draw_handler)
frame.start()
