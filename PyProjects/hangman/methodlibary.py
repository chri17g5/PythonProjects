#   Gets inputLetter and crossrefrence it with word (word value from wordlist)
#   Then gets inputLetters index from word and returns it.
def updatecensor(inputletter, wordlist):
    word = ''.join(wordlist)
    startAt = -1
    locs = []
    while True:
        try:
            loc = word.index(inputletter, startAt+1)
        except ValueError:
            break
        else:
            locs.append(loc)
            startAt = loc
    return locs