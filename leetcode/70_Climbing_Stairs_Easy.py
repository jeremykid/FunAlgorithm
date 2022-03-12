class Solution:
    def climbStairs(self, n: int) -> int:
        # n = 3
        # n=2 + n=1 : n=3
        
        if n <= 3:
            return n
        results = [0, 1, 2, 3]
        
        first, second = 2, 3
        
        for i in range(4, n+1):
            # results.append(results[i-1] + results[i-2])
            temp = first + second
            first, second = second, temp
            
        # return results[-1]
        return second