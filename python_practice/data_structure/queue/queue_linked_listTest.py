from queue_link_list import queue_linked_list

def test1():
	QLL = queue_linked_list()
	QLL.enqueue('A')
	QLL.enqueue('B')
	QLL.enqueue('C')
	print QLL


def main():
	test1()
main()