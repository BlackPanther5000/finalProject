'''
Created on Mar 7, 2020

@author: ITAUser
'''
#Ideas:
    #20 questions
    #turtle picture
    #Tic-Tac-Toe

#Board:
'''
Empty board:
     |     |     
     |     |     
-----|-----|-----
     |     |     
-----|-----|-----
     |     | 
     |     | 
Labeled board:
     |     |     
  1  |  2  |  3  
-----|-----|-----
  4  |  5  |  6  
-----|-----|-----
  7  |  8  |  9
     |     |    
By square:
     |
     |

     |
     |

-----|
-----|
-----
     |
     |

-----|
-----|
-----
     |
     |

     |
     |

Extra things I might not use:
print("     |     |     ")
print("  1  |  2  |  3  ")
print("-----|-----|-----")
print("  4  |  5  |  6  ")
print("-----|-----|-----")
print("  7  |  8  |  9  ")
print("     |     |     ")

The board, split into nine sections
board=[
    "     |","     |","      ",
    "     |","     |","      ", #1[4],2[5],3[6]
    "-----|","-----|","----- ",
    "     |","     |","      ", #4[10],5[11],6[12]
    "-----|","-----|","----- ",
    "     |","     |","      ", #7[16],8[17],9[18]
    "     |","     |","      "]
'''

'''
def add_player_choice (square):
    #squ=int(square) #user input is now an integer
    squ=square #shortened
    if squ.isdigit(): #check if user input is a number
        if squ>0 and squ<10: #tests if the user input is an integer from 1 to 9 (if the number is one of the board spaces)
            if squ in openSpaces: #tests if the board square is full or not
                f = open("board.txt","w") #writes the board into the board.txt file
                f.write("     |     |     ")
                f.close()
                f = open("board.txt","a")
                if squ>0 and squ<4: #if the square the player chose is one of the first three
                    if squ==1:
                        line1="  1  |     |     "
                        #line1=["  ",squ,"  |","     |","      "]
                        #f.write("  " + "\n" + squ + "\n" + "  |" + "\n" + "     |" + "\n" + "      ")
                    elif squ==2:
                        line1="     |  2  |     "
                        #line1=["     |","  ",squ,"  |","      "]
                    elif squ==3:
                        line1="     |     |  3  "
                        #line1=["     |","     |","  ",squ,"   "]
                    f.write(line1)
                    f.write("-----|-----|-----")
                    f.write("     |     |     ")
                    f.write("-----|-----|-----")
                    f.write("     |     |     ")
                    f.write("     |     |     ")
                elif squ>3 and squ<7: #if the square the player chose is one of the second three
                    f.write("     |     |     ")
                    f.write("-----|-----|-----")
                    if squ==4:
                        f.write("  ",squ,"  |","     |","      ")
                    elif squ==5:
                        f.write("     |","  ",squ,"  |","      ")
                    elif squ==6:
                        f.write("     |","     |","  ",squ,"   ")
                    f.write("-----|-----|-----")
                    f.write("     |     |     ")
                    f.write("     |     |     ")
                elif squ>6 and squ<10: #if the square the player chose is one of the third three
                    f.write("     |     |     ")
                    f.write("-----|-----|-----")
                    f.write("     |     |     ")
                    f.write("-----|-----|-----")
                    if squ==7:
                        f.write("  ",squ,"  |","     |","      ")
                    elif squ==8:
                        f.write("     |","  ",squ,"  |","      ")
                    elif squ==9:
                        f.write("     |","     |","  ",squ,"   ")
                    f.write("     |     |     ")
            else: #if the square is full
                print("That square has already been chosen.")
        else: #if the number given is not one of the board squares
            print("That is not a valid square.")
    else: #if the input is not a number
        print("That is not a number.")
        f.close()
    #f.open("board.txt", "r") #reads the new board and prints it
    #finalBoard=f.read()
    #f.close()
    #return finalBoard
    #print(finalBoard)
    
while computer<1 or player<1:
    square = input("Pick a square (1 through 9): ")
    #print(add_player_choice(square))
    add_player_choice
    f = open("board.txt","r")
    print(f.read())
    #finalBoard = f.read()
    #print(finalBoard)
    f.close()    
'''
#Tests
text=input("sumthin ")
#number=int(text)
'''
if text.isdigit():
    print(text)
else:
    print("nope")
'''
text=int(text)
if isinstance(text,int):
    print(text)
else:
    print("Nuh uh mister")