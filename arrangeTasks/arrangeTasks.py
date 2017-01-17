def minmumInArray(newArray,originalArray):
    newArray[0] = newArray[0]+originalArray[0]
    minimumValue = newArray[0]
    i = 1
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
        print (newArray,nArray)
        # 6,0
        # 6,8
        # 12,8
        m -= 1

    result = newArray[-1]
    print (newArray)
main()