# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        return self.recursive_add_numbers(l1, l2, 0)
        
        
    def recursive_add_numbers(self, 
                              l1: Optional[ListNode], 
                              l2: Optional[ListNode], 
                             carry: int) -> Optional[ListNode]:
        if l1 == None and l2 == None:
            if carry == 1:
                return ListNode(1)
            else:
                return None
            
        elif l1 == None:
            l2.val += carry
            if l2.val//10 == 1:
                result = ListNode(val = l2.val%10)
                result.next = self.recursive_add_numbers(l1, l2.next, 1)
                return result
            else:
                return l2
        elif l2 == None:
            l1.val += carry
            if l1.val//10 == 1:
                result = ListNode(val = l1.val%10)
                result.next = self.recursive_add_numbers(l1.next, l2, 1)
                return result
            else:
                return l1
        else:
            total = l1.val + l2.val + carry
            carry = total//10
            # print (total, carry)
            result = ListNode(val = total%10)
            result.next = self.recursive_add_numbers(l1.next, l2.next, carry)
            return result