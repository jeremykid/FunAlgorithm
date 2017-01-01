
import math

def findFactor(b0):
	temp = b0
	tempSqrt = math.sqrt(temp)
	returnArray = []
	i = 2
	while (i<temp):
		if temp%i == 0:
			temp = temp/i
			returnArray.append(i)
			tempSqrt = math.sqrt(temp)
			i = 2
		else:
			i += 1
	if temp != 1:
		returnArray.append(temp)
	return returnArray

def findDivision(value):
	valueSqrt = math.sqrt(value)
	i = 2
	returnArray = [value,1]
	while i<valueSqrt:
		if value%i == 0:
			returnArray.append(i)
			returnArray.append(value/i)
		i += 1
	return returnArray

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def main():
	times = int(input(""))
	for i in range(times):
		temp = raw_input("")
		tempArray = temp.split(" ")
		
		a0,a1,b0,b1 = int(tempArray[0]),int(tempArray[1]),int(tempArray[2]),int(tempArray[3])
		returnArray = findFactor(b0)
		resultFactor = b1/b0
		newb0 = b0
		gcdB = 1
		for i in findFactor(resultFactor):
			resultPoints = returnArray.count(i)
			gcdB *= i**resultPoints
			newb0= newb0/(i**resultPoints)

		returnDevision = findDivision(newb0)
		returnArray = [i*gcdB*resultFactor for i in returnDevision]
		returnArray = [i for i in returnArray if gcd(i,a0)==a1]
		print len(returnArray)

main()