
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
	

def main():
	times = int(input(""))
	for i in range(times):
		temp = raw_input("")
		tempArray = temp.split(" ")
		
		a0,a1,b0,b1 = int(tempArray[0]),int(tempArray[1]),int(tempArray[2]),int(tempArray[3])



main()