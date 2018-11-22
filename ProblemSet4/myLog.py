def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2
    x = b ^ a
    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    a = 0
    while b**a <= x:
        a += 1
    return a - 1