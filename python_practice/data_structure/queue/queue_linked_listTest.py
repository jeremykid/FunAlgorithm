from queue_link_list import queue_linked_list

def test1():
	QLL = queue_linked_list()
	QLL.enqueue('A')
	QLL.enqueue('B')
	QLL.enqueue('C')
	print "1. QLL = ",QLL
	QLL.enqueue('D')
	print "2. After QLL.enqueue('D') QLL =  ",QLL
	print "3. After QLL.empty() =  ",QLL.empty()
	QLL.dequeue()
	print "4. After QLL.dequeue() QLL =  ",QLL



def main():
	test1()
main()