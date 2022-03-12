class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        return self.permute(nums)       
        
        
    def permute(self, nums: 'List[int]') -> 'List[List[int]]':
        if len(nums) == 1:
            return [nums]
        else:
            result = []
            for index in range(len(nums)):
                if index > 0 and nums[index] == nums[index - 1]:
                    continue
                subResults = self.permute(nums[:index] + nums[index+1:])
                for i in subResults:
                    result.append([nums[index]] + i)
            return result