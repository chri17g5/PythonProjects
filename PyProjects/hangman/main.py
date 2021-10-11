#   TFT Hang Man!
from numpy import random
from methodlibary import *

#   Words array and then print a word from array into currentWord
wordsArr = ["pengu", "dango", "sprite", "abyssia", "bellswayer", "choncc", "craggle", "dowsie", 
            "fenroar", "flutterbug", "furyhorn", "fuwa", "hauntling", "hushtail", "lightcharger", 
            "melisma", "Molediver", "nimblefoot", "nixie", "neexie", "ossia", "paddlemar", "protector",
            "qiqi", "runespirit"]
currentWord = wordsArr[random.randint(len(wordsArr))]

#   Seperate string intro list
currentWordSplit = []
for i, x in enumerate(currentWord):
    currentWordSplit.append(currentWord[i])
    
#   Censored string
censoredWord = []
for x in range(len(currentWordSplit)):
    censoredWord.append("X")

print(censoredWord)

health = int(5)

while True:
    userinput = input()
    userinput.lower
    
    #   Quits application **APP COMMAND**
    if userinput == "quit":
        quit()

    #   If user input is 1 charackter **CORRECT AMOUNT**
    elif len(userinput) == 1:
        if userinput in currentWordSplit:
            index = updatecensor(userinput, currentWordSplit)

            for x in index:
                censoredWord[x] = userinput

            print(censoredWord)

        else:
            health = int(health - 1)
            print(f"*Wrong -1 try, you have {health} remaining")


    #   If userinput is empty **WRONG AMOUNT**
    elif len(userinput) == 0:
        print("*No Letters Was Typed*")

    #   If user input has more than acceptable charackters
    else:
        print("*Too many Letters*")

    #   Checks if your dead **WRONG AMOUNT**
    if health <= 0:
        print("*GAME OVER!*")
        break;
    elif currentWordSplit == censoredWord:
        print("*You won the game!*")
        break;

