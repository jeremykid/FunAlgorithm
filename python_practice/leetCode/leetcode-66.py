class Solution:
    def plusOne(self, digits: 'List[int]') -> 'List[int]':
        fl = 1
        for i in range(len(digits)-1,-1,-1):
            if digits[i] == 9 and fl == 1:
                fl = 1
                digits[i] = 0
            else:
                digits[i] += 1
                fl = 0
                break
        if (fl):
            digits.insert(0,1)
        return digits
