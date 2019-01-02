class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        res = 0
        dir = {}
        for i in range(len(s)):
            if s[i] not in dir:
                dir[s[i]] = i
                length += 1
            elif (dir[s[i]]) < i - length:
                #repeat but more than length
                dir[s[i]] = i
                length += 1
            else:
                #repeat
                if (length > res):
                    res = length
                length = i - dir[s[i]]
                dir[s[i]] = i

        if (length > res):
            res = length   
        return res    
