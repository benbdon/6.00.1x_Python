def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    retTup = ()
    for i in range(len(aTup)):
        if i%2 == 0:
            retTup += (aTup[i],)
    return retTup