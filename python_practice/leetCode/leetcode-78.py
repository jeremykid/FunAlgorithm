class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if nums == []:
            return [[]]
        
        sub = self.subsets(nums[1:])
        newSub = []
        for i in sub:
            newI = i + [nums[0]]
            newSub.append(newI)
        sub.extend(newSub)
        return sub
