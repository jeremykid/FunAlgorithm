class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = set()
        nums.sort()
        countZero = 0
        for i in range(len(nums) - 1):
            a = nums[i]
            if (a == 0):
                countZero += 1
                if (countZero > 3):
                    continue
            start = i + 1
            end = len(nums) - 1 
            while start < end:
                sum = a + nums[start] + nums[end]
                if (sum < 0):
                    start += 1
                elif (sum > 0):
                    end -= 1
                else :
                    res.add((a, nums[start], nums[end]))
                    start += 1
                    end -= 1

        res = [list(t) for t in set(tuple(element) for element in res)]
        return res

## 最后一个test [0,0,...,0] 需要remove 所有的 重复下一个的elememnt, 下次再改了
