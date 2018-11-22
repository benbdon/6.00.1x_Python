def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''
    uniqueVals = []
    for key in aDict.keys():
        subaDict = aDict.copy()
        del subaDict[key]
        
        uniqueValue=True
        
        for compKey in subaDict.keys():
            if aDict[key] == subaDict[compKey]:
                uniqueValue = False
        if uniqueValue:
            uniqueVals.append(key)
            uniqueVals.sort()
    return uniqueVals