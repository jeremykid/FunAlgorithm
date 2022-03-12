class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # method with sort alogrithm
        '''
        nums.sort()
        start = 0
        end = len(nums) - 1
        while start < end:
            if (nums[start] + nums[end] == target):
                return [start, end]
            elif (nums[start] + nums[end] > target):
                end -= 1
            else: #(nums[start] + nums[end] < target):
                start += 1
        '''
        # method O(n)
        dir = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in dir:
                return [dir[difference], i]

            dir[nums[i]] = i