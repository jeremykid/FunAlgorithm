def getAllCombination(inputList, returnList, newItem):
        if len(inputList) == 0:
                returnList.append(newItem)
                return returnList
        else:
                for i in inputList:
                        newItem = newItem+i
                        inputList.remove(i)
                        returnList = getAllCombination(inputList,returnList,newItem)
        return returnList
