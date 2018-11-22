def sumDigits(N):
    '''
    N: a non-negative integer
    '''
    if N <= 9:
       return N
    else:
        return sumDigits(N/10) + N % 10