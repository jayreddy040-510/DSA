from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
#         length = len(s)
#         if length == 0 or k == 0: return 0
        
#         right, left = 0,0
#         max_length = 1
#         hashmap = OrderedDict()
        
#         while right < length:
#             char = s[right]
#             if char in hashmap:
#                 del hashmap[char]
#             hashmap[char] = right
#             right += 1
#             if len(hashmap) == k + 1:
#                 _, del_idx = hashmap.popitem(last=False)
#                 left = del_idx + 1
#             max_length = max(max_length, right - left)
            
#         return max_length

        ret = 0
        dict = defaultdict(int)
        start = 0
        for i in range(len(s)):
            dict[s[i]] += 1
            while len(dict) > k:
                dict[s[start]] -= 1
                if dict[s[start]] == 0:
                    del dict[s[start]]
                start += 1
            ret = max(ret, i - start + 1 )
        
        return ret

#         window_start = 0
#         max_length = 0
#         char_frequency = {}

#         # in the following loop we'll try to extend the range [window_start, window_end]
#         for window_end in range(len(str1)):
#             right_char = str1[window_end]
#             if right_char not in char_frequency:
#                 char_frequency[right_char] = 0
#             char_frequency[right_char] += 1

#             # shrink the sliding window, until we are left with 'k' distinct characters in
#             # the char_frequency
#             while len(char_frequency) > k:
#                 left_char = str1[window_start]
#                 char_frequency[left_char] -= 1
#                 if char_frequency[left_char] == 0:
#                     del char_frequency[left_char]
#                 window_start += 1  # shrink the window
#             # remember the maximum length so far
#             max_length = max(max_length, window_end-window_start + 1)
#         return max_length