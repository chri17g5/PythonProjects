from numpy import random

#   Words array and then print a word from array into currentWord
wordsArr = ["Food", "Dango", "Fish", "Apple", "Zebra"]
currentWord = wordsArr[random.randint(len(wordsArr))]

#   Seperate string intro list
currentWordSplit = []
for i, x in enumerate(currentWord):
    currentWordSplit.append(currentWord[i])
    
print(currentWordSplit)

censoredWord = []
for x in range(len(currentWordSplit)):
    censoredWord.append("X")

print(censoredWord)