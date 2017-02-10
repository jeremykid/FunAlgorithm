def getAllStringCombination(inputList, returnList, newItem):
    if len(inputList) == 0:
        returnList.append(newItem)
        return returnList
    else:
        for i in inputList:
            tempList = list(inputList)
            tempList.remove(i)
            returnList = getAllStringCombination(tempList,returnList,newItem+i)

    return returnList

def getAllListCombination(inputList, returnList, newItem):
    if len(inputList) == 0:
        returnList.append(newItem)
        return returnList
    else:
        for i in inputList:
            tempList = list(inputList)
            tempList.remove(i)
            tempItem = list(newItem)
            newItem.append(i)
            returnList = getAllListCombination(tempList,returnList,newItem)
            newItem = list(tempItem)
    return returnList

def main():
    inputList = ["1","2","3"]
    returnList = getAllStringCombination(inputList,[],"")
    print returnList
    returnList = getAllListCombination(inputList, [],[])
    print returnList
main()