def lessThan4(aList):
    '''
    aList: a list of strings
    '''
    # Your code here
    returnList = []
    for i in aList:
        if len(i) < 4:
            returnList.append(i)
    return returnList