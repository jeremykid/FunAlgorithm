class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INTEGERMAX = 2**31 - 1
        INTEGERMIN = - 2**31
        res = 0
        postive = 1
        if (x < 0):
            postive = -1
            x = abs(x)
        res = int(str(x)[::-1])*postive
        if (res >= INTEGERMAX or res <= INTEGERMIN):
            return 0
        return res