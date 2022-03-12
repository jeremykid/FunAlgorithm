class sort_string_number(str):
    def __lt__(x, y):
        return x+y > y+x

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        str_num = [str(num) for num in nums]
        str_num.sort(key=sort_string_number)
        
        return str(int(''.join(str_num)))
    
