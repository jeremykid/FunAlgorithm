class Solution:
    def groupAnagrams(self, strs: 'List[str]') -> 'List[List[str]]':
        dic = {}
        for anagram in strs:
            key = ''.join(sorted(anagram))
            if key in dic.keys():
                dic[key].append(anagram)
            else:
                dic[key] = [anagram]
        result = []
        for key in dic.keys():
            result.append(dic[key])
        
        return result
