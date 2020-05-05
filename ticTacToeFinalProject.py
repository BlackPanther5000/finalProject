'''
Created on Mar 7, 2020

@author: ITAUser
'''

#import random function
import random

#Sets player to either "X" or "O"
smbls = ["X","O"]
playerSymbol = random.choice(smbls)
if playerSymbol=="X":
    compSymbol="O"
else:
    compSymbol="X"

#Spaces that have not been used
openSpaces=[1,2,3,4,5,6,7,8,9]

#squares
squ1="     |"
squ2="    |"
squ3="      "
squ4="     |"
squ5="    |"
squ6="      "
squ7="     |"
squ8="    |"
squ9="      "
squares=[squ1,squ2,squ3,squ4,squ5,squ6,squ7,squ8,squ9]

#neither player has won yet
player = 0
computer = 0

#Introduce player to game
print("   Tic-Tac-Toe")
print(" Your goal is to")
print("get three in a row.")
print("   You are: ", playerSymbol)
#print("  Pick a square:")

#prints empty board (numbers are listed the first time, so the player knows which square is which)
print("     |     |     ")
print("  1  |  2  |  3  ")
print("-----|-----|-----")
print("  4  |  5  |  6  ")
print("-----|-----|-----")
print("  7  |  8  |  9  ")
print("     |     |     ")

#Creates the board with the player square they chose
def add_player_choice (square):
    #if square.isdigit(): #check if user input is a number
    try: #see if "square" is an integer
        square=int(square)
    except ValueError: #if the input is not a number
        print("That is not a number.")
        return False
    square=int(square) #user input is now an integer
    if square>0 and square<10: #tests if the user input is an integer from 1 to 9 (if the number is one of the board spaces)
        if square in openSpaces: #tests if the board square is full or not
            openSpaces.remove(square)
            if square>0 and square<4: #if the square the player chose is one of the first three
                if square==1:
                    global squ1
                    squ1="".join(["  ",playerSymbol,"  |"])
                elif square==2:
                    global squ2
                    squ2="".join([" ",playerSymbol,"  |"])
                elif square==3:
                    global squ3
                    squ3="".join([" ",playerSymbol,"  "])
            elif square>3 and square<7: #if the square the player chose is one of the second three
                if square==4:
                    global squ4
                    squ4="".join(["  ",playerSymbol,"  |"])
                elif square==5:
                    global squ5
                    squ5="".join([" ",playerSymbol,"  |"])
                elif square==6:
                    global squ6
                    squ6="".join([" ",playerSymbol,"   "])
            elif square>6 and square<10: #if the square the player chose is one of the third three
                if square==7:
                    global squ7
                    squ7="".join(["  ",playerSymbol,"  |"])
                elif square==8:
                    global squ8
                    squ8="".join([" ",playerSymbol,"  |"])
                elif square==9:
                    global squ9
                    squ9="".join([" ",playerSymbol,"   "])
        else: #if the square is full
            print("That square has already been chosen.")
            return False
    else: #if the number given is not one of the board squares
        print("That is not a valid square.")
        return False

#Creates the board with a random computer square
def add_computer_choice():
    global compChoice
    compChoice = 0
    while not compChoice in openSpaces:
        compChoice=random.randint(1,9)
    openSpaces.remove(compChoice)
    if compChoice>0 and compChoice<4: #if the square the computer chose is one of the first three
        if compChoice==1:
            global squ1
            squ1="".join(["  ",compSymbol,"  |"])
        elif compChoice==2:
            global squ2
            squ2="".join([" ",compSymbol,"  |"])
        elif compChoice==3:
            global squ3
            squ3="".join([" ",compSymbol,"   "])
    elif compChoice>3 and compChoice<7: #if the square the computer chose is one of the second three
        if compChoice==4:
            global squ4
            squ4="".join(["  ",compSymbol,"  |"])
        elif compChoice==5:
            global squ5
            squ5="".join([" ",compSymbol,"  |"])
        elif compChoice==6:
            global squ6
            squ6="".join([" ",compSymbol,"   "])
    elif compChoice>6 and compChoice<10: #if the square the computer chose is one of the third three
        if compChoice==7:
            global squ7
            squ7="".join(["  ",compSymbol,"  |"])
        elif compChoice==8:
            global squ8
            squ8="".join([" ",compSymbol,"  |"])
        elif compChoice==9:
            global squ9
            squ9="".join([" ",compSymbol,"   "])

def test_for_win():
    global player
    global computer

    #Tests if the player X won in any of several ways
    #first three: horizontal; second three: vertical; last two: diagonal
    if "X" in squ1 and "X" in squ2 and "X" in squ3\
    or "X" in squ4 and "X" in squ5 and "X" in squ6\
    or "X" in squ7 and "X" in squ8 and "X" in squ9\
    or "X" in squ1 and "X" in squ4 and "X" in squ7\
    or "X" in squ2 and "X" in squ5 and "X" in squ8\
    or "X" in squ3 and "X" in squ6 and "X" in squ9\
    or "X" in squ1 and "X" in squ5 and "X" in squ9\
    or "X" in squ3 and "X" in squ5 and "X" in squ7:
        if playerSymbol=="X":
            print_board()
            print("You win!")
            player=1
            return True
        else:
            print_board()
            print("You lose!")
            computer=1
            return True
            
    #Tests if the player O won in any of several ways
    #first three: horizontal; second three: vertical; last two: diagonal
    elif "O" in squ1 and "O" in squ2 and "O" in squ3\
    or "O" in squ4 and "O" in squ5 and "O" in squ6\
    or "O" in squ7 and "O" in squ8 and "O" in squ9\
    or "O" in squ1 and "O" in squ4 and "O" in squ7\
    or "O" in squ2 and "O" in squ5 and "O" in squ8\
    or "O" in squ3 and "O" in squ6 and "O" in squ9\
    or "O" in squ1 and "X" in squ5 and "O" in squ9\
    or "O" in squ3 and "O" in squ5 and "O" in squ7:
        if playerSymbol=="O":
            print_board()
            print("You win!")
            player=1
            return True
        else:
            print_board()
            print("You lose!")
            computer=1
            return True

    #If all nine board spaces are full
    elif len(openSpaces)==0:
        print_board()
        print("Cat's Game! No one wins!")
        return True
        
def print_board():
    print("     |     |     ")
    print(squ1,squ2,squ3)
    print("-----|-----|-----")
    print(squ4,squ5,squ6)
    print("-----|-----|-----")
    print(squ7,squ8,squ9)
    print("     |     |     ")

#GAME STARTS HERE

#This is if the computer starts as X, so the board gets printed correctly
if compSymbol=="X":
    add_computer_choice()
    print ("The computer chose: ", compChoice)
    print_board()
    square = input("Pick a square (1 through 9): ")
    while add_player_choice(square)==False: #repeats until the player gives a correct response
        square = input("Pick a square (1 through 9): ")

#The main While loop that asks the player for their choice, draws it, draws the
#computer's choice, and checks to see if anyone has won yet
while computer<1 or player<1:
    if playerSymbol=="X":
        square = input("Pick a square (1 through 9): ")
        while add_player_choice(square)==False:
            square = input("Pick a square (1 through 9): ")
        if test_for_win()==True:
            break
        add_computer_choice()
        print ("The computer chose: ", compChoice)
        if test_for_win()==True:
            break
        print_board()

    else:
        add_computer_choice()
        print ("The computer chose: ", compChoice)
        if test_for_win()==True:
            break
        print_board()
        square = input("Pick a square (1 through 9): ")
        while add_player_choice(square)==False:
            square = input("Pick a square (1 through 9): ")
        if test_for_win()==True:
            break

#Thanks the user for playing after the game ends
print("Thanks for playing!")