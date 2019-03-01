class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = self.subsets(sorted(nums))
        result = [list(t) for t in set(tuple(element) for element in result)]
        return result
    
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if nums == []:
            return [[]]
        
        sub = self.subsets(nums[1:])
        newSub = []
        for i in sub:
            newI = [nums[0]] + i 
            newSub.append(newI)
        sub.extend(newSub)
        return sub
