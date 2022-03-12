import math

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # divided conquer is O(nlogn)
        
        # O(n)
        max_result = -math.inf        
        end_index = 0
        sum_nums = 0
        for end_index in range(0, len(nums)):
            sum_nums += nums[end_index]
            max_result = max(sum_nums, max_result)
            if sum_nums < 0:
                sum_nums = 0
        return max_result
