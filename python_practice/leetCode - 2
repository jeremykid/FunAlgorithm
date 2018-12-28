        

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        return self.addTwoNumbersCal(l1, l2, 0)

    def addTwoNumbersCal(self, l1, l2, fl):
        if (l1 == None and l2 == None):
            if (fl == 1):
                lres = ListNode(1)
                return lres
            else:
                return None;
        elif (l1 == None):
            newValue = l2.val + fl
            fl = 0
            if newValue > 9:
                fl = 1
                newValue -= 10
            lres = ListNode(newValue)
            lres.next = self.addTwoNumbersCal(l1, l2.next, fl)
            return lres
        elif (l2 == None):
            newValue = l1.val + fl
            fl = 0
            if newValue > 9:
                fl = 1
                newValue -= 10
            lres = ListNode(newValue)
            lres.next = self.addTwoNumbersCal(l1.next, l2, fl)
            return lres
        else:
            newValue = l1.val + l2.val + fl
            fl = 0
            if newValue > 9:
                fl = 1
                newValue -= 10
            lres = ListNode(newValue)
            lres.next = self.addTwoNumbersCal(l1.next, l2.next, fl)
            return lres
