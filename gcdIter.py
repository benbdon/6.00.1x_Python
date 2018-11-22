def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    
    #assign min to guess
    guess = min(a,b) 
    
    #use guess to check if gcd, if not decrement by 1 and try again
    while a % guess != 0 or b % guess != 0:
        guess -= 1
    return guess