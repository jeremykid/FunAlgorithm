from math import sqrt 

def returnPrimeArray(number):
	prime_array = []
	for i in range(2,number):
		is_prime = True
		for j in range(2,int(sqrt(i))+1):
			if (i%j==0):
				is_prime = False
				break
		if (is_prime):
			prime_array.append(i)
	return prime_array

def readFile():
	#todo
	return 1

def printFile():
	#todo
	return 1

def main():
	readFile()

	print returnPrimeArray(15)

	printFile()

main()