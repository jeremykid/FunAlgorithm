from LinkedList import linked_list 
from node import Node

def testLinkedList():
	test1 = linked_list()
	node0 = Node('a')
	node1 = Node('b')
	node2 = Node('c')
	node0.set_next(node1)
	node1.set_next(node2)
	test1.set_head(node0)
	print (test1)
	return 0

def main():
	testLinkedList()
main()