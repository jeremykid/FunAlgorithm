import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap_tree = nums #build max heap

    def add(self, val: int) -> int:
        # insert element in the heap
        heappush(self.heap_tree, val)
        # return the K largest
        print (self.heap_tree)
        return (nlargest(self.k, self.heap_tree))
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)