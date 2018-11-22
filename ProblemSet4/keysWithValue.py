def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    keys = aDict.keys()
    resultList = []
    for i in keys:
        if aDict[i] == target:
            resultList.append(i)
    resultList.sort()
    return resultList