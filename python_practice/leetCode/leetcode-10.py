
class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        sIndex = 0
        pIndex = 0
        sLength = len(s)
        pLength = len(p)
        res = true
        startTrigger = 0
        while res and sIndex < sLength and pIndex < pLength:
            if p[pIndex+1] == '*':
                startTrigger = 1
                if p[pIndex] == '.':
                    p[pIndex] = s[sIndex]
                elif p[pIndex] == s[sIndex]:
                    sIndex += 1
                else:
                    pIndex += 2
                    sIndex += 1 
            elif p[pIndex] == '.':
                sIndex += 1
                pIndex += 1
            elif s[sIndex] == p[pIndex]:
                sIndex += 1
                pIndex += 1
            else:
                res = false

        return res
