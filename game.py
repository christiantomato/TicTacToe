import random

#help

#create the GAMEBOARD
grids = [" - ", " - "," - ", " - "," - ", " - "," - ", " - "," - "]

#game logic
def gamestart():

    while True:

        #game instructions
        print("welcome to tictactoe! Move commands are as follows:")
        print("top left = 0, top middle = 1, top right = 2")
        print("middle left = 3, middle = 4, middle right = 5")
        print("bottom left = 6, bottom middle = 7, bottom middle = 8")

        printgrid()
        print("AI will go first")
        #type whatever lol
        input("ready?\n")
        aiupdategrid()
        printgrid()

        move = input("Where would you like to move? \n")
        updategrid(int(move))
        printgrid()
        print("ai moves")
        aiupdategrid()
        printgrid()

        move = input("Where would you like to move? \n")
        updategrid(int(move))
        printgrid()
        print("ai moves")
        aiupdategrid()
        printgrid()
        if checkwin():
            print("AI WINS!")
            break

        move = input("Where would you like to move? \n")
        updategrid(int(move))
        printgrid()
        if checkwin():
            print("YOU WIN!")
            break
        print("ai moves")
        aiupdategrid()
        printgrid()
        if checkwin():
            print("AI WINS!")
            break

        move = input("Where would you like to move? \n")
        updategrid(int(move))
        printgrid()
        if checkwin():
            print("YOU WIN!")
            break
        print("ai moves")
        aiupdategrid()
        printgrid()
        if checkwin():
            print("AI WINS!")
            break
        else:
            #nobody won
            print("tie game!")
            break
        #MAX TURNS

def updategrid(location):
    #place an X
    grids[location] = " X "

def aiupdategrid():
    #ai movement
    #generate random move from 0-8
    move = random.randint(0,8)
    if " X " in grids[move] or " O " in grids[move]:
        aiupdategrid()
    else:
        grids[move] = " O "

def printgrid():
    x = 0
    while x < len(grids):
        print(grids[x] + grids[x + 1] + grids[x + 2])
        x += 3

def checkwin():
    #check row wins
    x = 0
    while x < 7:
        if grids[x] == grids[x + 1] == grids[x + 2] and " - " not in grids[x]:
            #win
            print("win")
            return True
        else:
            x+=3
    #check column wins
    y = 0
    while y < 3:
        if grids[y] == grids[y + 3] == grids[y + 6] and " - " not in grids[y]:
            #win
            print("win")
            return True
        else:
            y+=1
    #check diagonal wins (getting lazy)
    if grids[0] == grids[4] == grids[8] and " - " not in grids[0]:
        # win
        print("win")
        return True
    elif grids[2] == grids[4] == grids[6] and " - " not in grids[2]:
        # win
        print("win")
        return True

def restartgame():
    global grids
    grids = [" - ", " - ", " - ", " - ", " - ", " - ", " - ", " - ", " - "]


#intro
name = input("What is your name? \n")
print(f"Nice to meet you {name},")
challengeAccept = input("Are you ready to play?\n(type YES or NO)\n")

#check answer
if "YES" in challengeAccept:
    #start game
    gamestart()

else:
    print("come back again soon!")
    #exit

while True:

    #play again?
    again = input("Play Again?\n(YES or NO)\n")

    if "YES" in again:
        #restartgame
        restartgame()
        gamestart()

    else:
        print("come back again soon!")
        break

