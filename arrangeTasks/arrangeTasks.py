def minmumInArray(newArray,originalArray):
    sumArray = [0]*len(newArray)
    for index in range(len(newArray)):
        sumArray[index] = newArray[index] + originalArray[index]

    minimumValue = min(sumArray)
    minimumIndex = sumArray.index(minimumValue)
    newArray[minimumIndex] = minimumValue

    minimumValue = newArray[minimumIndex]
    i = minimumIndex+1
    while (i<len(newArray) and newArray[i]<minimumValue):
        newArray[i],newArray[i-1] = newArray[i-1],newArray[i]
        originalArray[i],originalArray[i-1] = originalArray[i-1],originalArray[i]
        i += 1
    return newArray,originalArray


def main():
    m = int(input("")) # the number of tasks
    n = input("") # the number of machine
    nArray = input("") # the list of Machine take the time
    nArray = nArray.split(' ')
    nArray = list(map(int, nArray))
    nArray.sort()
    newArray = [0]*len(nArray)
    while (m>0):
        newArray,nArray = minmumInArray(newArray,nArray)
        # 6,0
        # 6,8
        # 12,8
        m -= 1

    result = newArray[-1]
    print (newArray)
main()