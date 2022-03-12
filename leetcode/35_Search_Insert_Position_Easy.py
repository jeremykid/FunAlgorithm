class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        index = 0
        numsLength = len(nums)
        while index < len(nums):
            if (target <= nums[index]):
                break
            index += 1
        return index