
class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = ""
        while num:
            if num >= 1000:
                res += (num//1000) * 'M'
                num = num%1000
            elif num >= 900:
                res += 'CM'
                num -= 900
            elif num >= 500:
                res += 'D'
                num -= 500
            elif num >= 400:
                res += 'CD'
                num -= 400
            elif num >= 100:
                res += (num//100) * 'C'
                num = num%100
            elif num >= 90:
                res += 'XC'
                num -= 90
            elif num >= 50:
                res += 'L'
                num -= 50
            elif num >= 40:
                res += 'XL'
                num -= 40
            elif num >= 10:
                res += (num//10) * 'X'
                num = num%10
            elif num >= 9:
                res += 'IX'
                num -= 9
            elif num >= 5:
                res += 'V'
                num -= 5
            elif num >= 4:
                res += 'IV'
                num -= 4
            elif num >= 1:
                res += (num//1) * 'I'
                num = 0
        return res
