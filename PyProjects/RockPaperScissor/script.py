import random
import os
arr = ["Rock", "Paper", "Scissors"]


def gameLogic(userInput):
    #   Opponent choice
    opponentChoice = arr[random.randint(0, 2)]
    print(f"Opponent: {opponentChoice}!")

    #   Actual Game Logic
    #   If tie
    if userInput == opponentChoice:
        print("<< it's a tie! >>")

    #   If player wins with Rock 
    elif userInput == "Rock" and opponentChoice == "Scissors":
        print("<< You win! >>")
    
    #   If player wins with Scissors 
    elif userInput == "Scissors" and opponentChoice == "Rock":
        print("<< You win! >>")
    
    #   If player wins with Paper 
    elif userInput == "Paper" and opponentChoice == "Rock":
        print("<< You win! >>")

    #   Else the player has lost
    else:
        print("<< You lost... >>")



#   Clears console
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

#   UI
errorMessage = "<< Error Invalid Command! >>"


while True:
    #   MainMenu
    print("<< Do you wish to play? [y / n]")
    userInput = input()
    
    #   If input is y / yes
    if userInput.lower() == "y" or userInput.lower == "yes":
        while True:
            clearConsole()
            print("<< Please input choice index... >>")
            print("----------------------------------")

            displayNum = int(0)
            for x in arr:
                displayNum = displayNum + 1
                print(f"{displayNum} {x}")

            userChoice = input()

            #   Rock
            if userChoice == "1":
                gameLogic(arr[0])
                break

            #   Paper
            elif userChoice == "2":
                gameLogic(arr[1])
                break;

            #   Scissors
            elif userChoice == "3":
                gameLogic(arr[2])
                break;
            
            else:
                print(errorMessage)
    
    elif userInput.lower() == "n" or userInput.lower == "no":
        quit()
    
    else:
        print(errorMessage)
        print("----------------------------")