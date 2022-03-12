class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dictionary = {}
        for num_index in range(len(nums)):
            num = nums[num_index]
            if num in dictionary and num_index - dictionary[num] <= k:
                return True
            # else:
            dictionary[num] = num_index
            # print (dictionary)
        return False