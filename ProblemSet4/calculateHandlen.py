def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    len = 0
    for letter in hand.keys():
        for j in range(hand[letter]):
            len += 1        
    return len