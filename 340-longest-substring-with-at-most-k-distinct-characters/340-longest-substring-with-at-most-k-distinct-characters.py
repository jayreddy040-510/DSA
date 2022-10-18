from collections import OrderedDict
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        length = len(s)
        if length == 0 or k == 0: return 0
        
        right, left = 0,0
        max_length = 1
        hashmap = OrderedDict()
        
        while right < length:
            char = s[right]
            if char in hashmap:
                del hashmap[char]
            hashmap[char] = right
            right += 1
            if len(hashmap) == k + 1:
                _, del_idx = hashmap.popitem(last=False)
                left = del_idx + 1
            max_length = max(max_length, right - left)
            
        return max_length