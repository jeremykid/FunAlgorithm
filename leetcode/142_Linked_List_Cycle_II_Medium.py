# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # method 1
        exist = []
        if head == None:
            return (None)
        
        while head.next != None and head not in exist:
            # print (head.val)
            exist.append(head)
            head = head.next
        
        if head.next != None:
            return (head)
        else:
            return (None)
        
        # method 2
        
        slow = head
        fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return slow
        return None
        
