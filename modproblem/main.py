def main():
	stop = False
	n = 63
	while (stop == False):
		n += 63
		if (n%5 == 4 and n%8 ==1 ):
			stop = True
			print (n)

main()