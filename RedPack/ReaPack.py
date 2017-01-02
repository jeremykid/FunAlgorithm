
def main():
	inputArray = raw_input("").split(" ")
	inputArray = [int(i) for i in inputArray]

	for i in range(len(inputArray)):
		inputArray[i] = inputArray[i] + 0.5*inputArray[(i+1)%3] + 0.5*inputArray[(i+2)%3]#0 1 2
		inputArray[(i+1)%3] = 0.5*inputArray[(i+1)%3]
		inputArray[(i+2)%3] = 0.5*inputArray[(i+2)%3]

	print inputArray
main()