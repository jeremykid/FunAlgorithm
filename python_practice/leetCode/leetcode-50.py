class Solution:
    def myPow(self, x: 'float', n: 'int') -> 'float':
        return x**n

    def myPow2(self, x: 'float', n: 'int') -> 'float':
        if n == 0:
            return 1
        if n < 0:
            n = 0-n
            x = 1/x
        
        return x**(n%2)*self.myPow2(x*x, n//2)
