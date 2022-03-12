class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #0, 1, 2, 3
        #0, 1, 3, 2
        #0, 2, 1, 3
        #0, 2, 3, 1
        #0, 3, 1, 2
        #0, 3, 2, 1
        # sorted_nums = sorted(nums)
        
        max_index = 0
        # find where is there are revert index
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                max_index = i
                break
        
        # if revert index at the bottom, which we need get the first permutation
        if max_index == 0:
            nums[:] = sorted(nums)
            # print (nums)
        else:
            # if the revert index, then sort the array after revert index
            next_value = nums[i-1]
            new_next_value = min([i for i in nums[i-1:] if i > next_value])
            left = nums[i-1:]
            left.remove(new_next_value)
            nums[i-1] = new_next_value
            nums[i:] = sorted(left)
            

        # print (nums)
        