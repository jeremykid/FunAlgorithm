class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                line = min(height[i], height[j])
                max_area = max(max_area, line*(j-i))
                
        return max_area