class Solution:
    def sortColors(self, nums: 'List[int]') -> 'None':
        """
        Do not return anything, modify nums in-place instead.
        """
        index0 = -1
        index2 = len(nums)
        index = 0
        while index < len(nums):
            if (index >= index2):
                break
            elif nums[index] == 0:
                index0 += 1
                self.swap(nums, index, index0)
                index += 1
            elif nums[index] == 2:
                index2 -= 1
                self.swap(nums, index, index2)
            else:
                index += 1
        

    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
