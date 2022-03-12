class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        result = [0]*len(nums)
        for num in range(len(nums)):
            result[num] = nums[nums[num]]
        return result