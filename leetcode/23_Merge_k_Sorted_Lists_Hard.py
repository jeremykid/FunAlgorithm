# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
# from Queue import PriorityQueue

class Solution:
    # method 2
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        result = point = ListNode(0)
        min_heap = []
        for list_index in range(len(lists)):
            list_node = lists[list_index]
            if list_node:
                heappush(min_heap, (list_node.val, list_index))
        while len(min_heap) > 0:
            val, list_index = heappop(min_heap)
            point.next = ListNode(val)
            point = point.next
            list_node = lists[list_index]
            lists[list_index] = list_node = list_node.next
            
            if list_node:
                heappush(min_heap, (list_node.val, list_index))

        return result.next
    
    # method 1
'''
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        # Create a min heap
        min_heap = []        
        for list_node in lists:
            if list_node != None:
                heappush(min_heap, list_node.val)
        
        if len(min_heap) == 0:
            return None
        
        # inital min heap with the first element in each listnode
        min_value = heappop(min_heap)
        for list_index in range(len(lists)):
            list_node = lists[list_index]
          
            if list_node != None and min_value == list_node.val:
                lists[list_index] = list_node.next
                if lists[list_index] != None:
                    heappush(min_heap, lists[list_index].val)
                break
                
        result_listnode = ListNode(min_value)
        
        self.recursive_mergeKLists(lists, min_heap, result_listnode)
        
        return result_listnode
    
    
    def recursive_mergeKLists(self, lists, min_heap, result_listnode):

        if len(min_heap) == 0:
            return
        
        min_value = heappop(min_heap)
        for list_index in range(len(lists)):
            list_node = lists[list_index]   
            if list_node != None and min_value == list_node.val:
                lists[list_index] = list_node.next
                if lists[list_index] != None:
                    heappush(min_heap, lists[list_index].val)            
                break
                
        result_listnode.next = ListNode(min_value)
        result_listnode = result_listnode.next

        return self.recursive_mergeKLists(lists, min_heap, result_listnode)
'''
    
    