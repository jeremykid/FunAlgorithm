class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        end = len(height) -1 
        start = 0
        res = 0
        while start < end:
            if height[start] >= height[end]:
                area = height[end] * (end - start)
                res = max(area, res)
                end -= 1
            else:
                area = height[start] * (end - start)
                res = max(area, res)
                start += 1
        return res
