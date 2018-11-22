def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    #Base case: If aStr is emply, we did not find the char.
    if  aStr == '':
        return False
    
    #Base case: If aStr is of length 1, just see if the chars are equal
    if len(aStr) == 1:
        return aStr == char 
    
    #Base case: See if the character in the middle of aStr equals the
    #test character
    middle = len(aStr) / 2
    guess = aStr[middle]
    if char == guess:
        #We found the character!
        return True
    
    #bisect aStr and enter recursion
    elif char < guess:
        return isIn(char, aStr[:middle])
    else:
        return isIn(char, aStr[middle+1:])