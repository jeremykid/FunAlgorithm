# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        self.swapPairsRecursion(head)

        return head

    def swapPairsRecursion(self, head):
        if (head == None or head.next == None):
            return
        else:
            swap = head.val
            head.val = head.next.val
            head.next.val = swap
        
        self.swapPairsRecursion(head.next.next)