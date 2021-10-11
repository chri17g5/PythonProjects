def updatecensor(input, wordlist):
    word = ''.join(wordlist)
    start_at = -1
    locs = []
    while True:
        try:
            loc = word.index(input, start_at+1)
        except ValueError:
            break
        else:
            locs.append(loc)
            start_at = loc
    return locs