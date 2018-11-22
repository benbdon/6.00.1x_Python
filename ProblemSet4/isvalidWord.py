def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    legalLetter = True
    for i in word:
        if word.count(i) > hand.get(i,0):
            legalLetter = False
    
    legalWord = True
    if word not in wordList:
        legalWord = False
    
    if legalWord == True and legalLetter == True:
        return True
    else: 
        return False