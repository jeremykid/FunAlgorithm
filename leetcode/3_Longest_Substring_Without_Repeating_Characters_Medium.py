class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int: 
        # method 1    
        if len(s) == 0:
            return 0
        start = 0
        end = 0
        max_count = 1
        set_s = list(set([element for element in s]))
        frequency_dict = {element:0 for element in set_s}

        frequency_dict[s[start]] = 1
        while start < len(s):
            if end+1 < len(s) and frequency_dict[s[end+1]] == 0:
                frequency_dict[s[end+1]] += 1
                end += 1
                max_count = max(max_count, end - start + 1)
            else:
                frequency_dict[s[start]] -= 1
                start += 1
                max_count = max(max_count, end - start +1)
        return max_count
    
        # method 2
        length = 0
        res = 0
        dir = {}
        for i in range(len(s)):
            # print (dir)
            if s[i] not in dir:
                dir[s[i]] = i
                length += 1
            elif (dir[s[i]]) < i - length:
                #repeat but more than length, which means is not repeat
                print (dir)
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
        return 3