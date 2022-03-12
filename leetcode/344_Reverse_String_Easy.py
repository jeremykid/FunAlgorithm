class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        #method 1
        total = len(s)-1
        mid = len(s)//2
        for i in range(mid):
            s[i], s[total-i] = s[total-i],s[i]
        
        #method2
        if len(s) > 1:
            s[0], s[-1] = s[-1], s[0]
            print (s)
            return self.reverseString(s[1:-1])
        