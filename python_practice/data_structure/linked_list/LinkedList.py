from node import Node

class linked_list(Object):
	def __init__(self):
		self.head = None

	def set_head(self, head_node):
		self.head = head_node

	def __len__(self):
		count = 0
        current = self.head
        while current:
            count += 1
            current = current.get_next()
        return count

    def __str__(self):
    	current = self.head
        output = ""
        while current:
            output += str(current) + " -> "
            current = current.get_next()
        return output

	def empty(self):
		count = 0
		if (self.head):
			return False
		else:
			return True

    # Pops an item from the front of the list
    def pop_front(self):
        if self.head:
            self.head = self.head.get_next()
        else:
            raise IndexError("Unable to pop from empty list")

    # params: node value
    # return: int, index of the node value in the linked list
    def value_at(self,node_value):
    	current = 0
    	current = self.head
    	while (current != node_value):
    		current += 1
    		current = current.get_next()
    	return current
    # params: node value 
    # return: bool true: exist that value in the linked list false: does not exist
    def exist(self, node_value):
    	result = false
    	current = self.head
    	while (result == false and current):
    		if current.get_data == node_value:
    			result = true
    		current = current.get_next()
    	return result

    # params: node value
    # return:
    def push_front(self, node_value):
    	new_node = Node(node_value)
    	new_node.set_next(self.head)
    	self.head = new_node

    def push_back(self, node_value):
    	new_node = Node(node_value)
    	current = self.head
    	while current.get_next():
    		current = current.get_next()
    	current.get_next().set_next(new_node)

    # delete the last 
    def pop_back(self):
    	current = self.head
    	while current.get_next().get_next():
    		current = current.get_next()

    	current.set_next(None)
    	return 
    # return: the front node
    def front(self):
    	return self.head
    # return: the end node
    def back(self):
    	while current.get_next():
    		current = current.get_next()
    	return current
    # params: index of the item which need to be erase
    #
    def erase(self, index):
    	count = 0
    	current = self.head
    	while (count < index and current):
    		current = current.get_next()
    	if (count == index):

