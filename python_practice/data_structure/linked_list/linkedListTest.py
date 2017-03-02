from LinkedList import linked_list 
from node import Node

def testLinkedList():
	print "test1 is a linked_list"
	test1 = linked_list()
	node0 = Node('a')
	node1 = Node('b')
	node2 = Node('c')
	node0.set_next(node1)
	node1.set_next(node2)
	test1.set_head(node0)
	print "1. Print test1 = ",test1
	print "2. size: test1.size() = ",test1.size()
	print "3. empty: test1.empty() = ",test1.empty()
	print "4.1 value_at: test1.value_at(0) = ",test1.value_at(0)
	print "4.2 value_at: test1.value_at(2) = ",test1.value_at(2)
	print "5.1 exist: test1.exist('a') = ", test1.exist('a')
	print "5.2 exist: test1.exist('d') = ", test1.exist('d')
	print "6 reverse: test1.reverse() = ",test1.reverse()
	test1.remove_value('a')
	print "7 remove_value: test1.remove_value('a')  result =", test1
	print "8.1 value_n_from_end: test1.value_n_from_end(0)  result =", test1.value_n_from_end(0)
	print "8.2 value_n_from_end: test1.value_n_from_end(2)  result =", test1.value_n_from_end(2)

	return 0



def main():
	testLinkedList()
main()