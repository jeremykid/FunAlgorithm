def main():
	#init an array named a
	a = list() 
	a = []
	b = [1,'1',[1,2]]

	#Get the size of a list
	a_size = len(a)

	#how to check if a list is empty
	if (a):
		print ("not empty")
	else:
		print ("empty")


	index = 0
	a = ['a','b','c']
	print (a[index])

	a.append('d')
	a.extend(['e'])
	print ('After append a, extend [e]')
	print (a)

	a.insert(2,'bb')
	print ('After insert bb at 2')
	print (a)

	a.insert(0, 'a0')
	print ('After insert a0 at 0')
	print (a)

	#Find the index of a item in an array
	answer_1 = a.index('a')
	answer_0 = a.index('a0')	
	print ('use a.index(item) to find the index only for the first item')

	#list.pop() return last item in the list and remove the last item
	print 'Before a.pop(), a = ', a
	print 'a.pop() = ', a.pop()
	print 'After a.pop(), a = ', a 

	#Remove an item
	
main()