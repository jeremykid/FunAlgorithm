import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'linked_list')))
from LinkedList import linked_list 
from node import Node

class queue_linked_list():
    def __init__(self): 
        self.head = None
        self.tail = None

    def enqueue(self, value):
        tempNode = Node(value)
        if (self.tail):
            self.tail.set_next(tempNode)
            self.tail = tempNode
        else:
            self.head = tempNode
            self.tail = tempNode

    def dequeue(self):
        if (self.empty() == False):
            tempHeadNext = self.head.get_next()
            result = self.head
            if (tempHeadNext == None):
                self.tail = None
            else:
                self.head = tempHeadNext
        else:
            return "The queue is empty"

    def empty(self):
        if (self.head):
            return False
        else:
            return True

    def __str__(self):
        current = self.head
        output = ""
        while current:
            output += str(current) + " -> "
            current = current.get_next()
        output += " End "
        return output