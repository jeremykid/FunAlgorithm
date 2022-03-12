class Solution:
    def permute(self, nums: 'List[int]') -> 'List[List[int]]':
        if len(nums) == 1:
            return [nums]
        else:
            result = []
            for index in range(len(nums)):
                subResults = self.permute(nums[:index] + nums[index+1:])
                for i in subResults:
                    result.append([nums[index]] + i)
            return result