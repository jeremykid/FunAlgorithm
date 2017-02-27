from node import Node

class linked_list():
    def __init__(self):
        self.head = None

    def set_head(self, head_node):
        self.head = head_node

    def size(self):
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
        output += " End "
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
    def value_at(self,index):
        count = 0
        current = self.head
        while (count < index and current):
            count += 1
            current = current.get_next()
        if current:
            return current
        else:
            return "Out of Index"
    # params: node value 
    # return: bool true: exist that value in the linked list false: does not exist
    def exist(self, node_value):
        result = False
        current = self.head
        while (result == False and current):
            if current.get_data() == node_value:
                result = True
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

    # delete the last and return the end node value
    def pop_back(self):
        current = self.head
        while current.get_next().get_next():
            current = current.get_next()
        result = current.get_next()
        current.set_next(None)
        return result
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
        if (index == 0):
            self.head = self.head.get_next()
        else:
            while (count < index-1 and current):
                current = current.get_next()
            if (count == index-1):
                current.set_next(current.get_next().get_next())
            else:
                print "Index out of range"

    def insert(self, index, node_value):
        if (index == 0):
            temp = self.head
            self.head = node(node_value)
            self.head.set_next(temp)
        else:
            count = 0
            current = self.head
            while (count == index-1 and current):
                count += 1
                current = current.get_next()

            if (count == index-1):
                temp_next = current.get_next()
                temp = node(node_value)
                current.set_next(temp)
                temp.set_next(temp_next)
            else:
                print "index out of range"

    # a->b->c->end
    def reverse(self):
        current = self.head#a
        temp_next = current.get_next()#b
        if temp_next == None:
            return self
        current.set_next(None)#a->end
        while temp_next.get_next():
            temp_node = temp_next.get_next()
            temp_next.set_next(current)
            current = temp_next
            temp_next = temp_node
            
        temp_next.set_next(current)
        self.head = temp_next
        return self

    def remove_value(self, value):
        current =self.head
        if current == value:
            self.head = current.get_next()
            return 1
        while (current.get_next() != value and current.get_next()):
            current = current.get_next()

        if (current.get_next() == value):
            temp_next = current.get_next().get_next()
            current.set_next(temp_next)
            return 1
        else:
            return -1

    def value_n_from_end(self, n):
        linked_list_length = self.size()
        return self.value_at(linked_list_length - n)