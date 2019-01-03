class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        strx = str(x)
        reverseStrx = strx[::-1]
        return strx == reverseStrx
