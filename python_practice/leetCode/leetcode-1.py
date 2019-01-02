class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dir = {}

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in dir:
                return [dir[difference], i]

            dir[nums[i]] = i
        
