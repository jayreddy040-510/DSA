
from collections import defaultdict
def longest_substring_distinct(s, k):
    """
    >>> longest_substring_distinct("aaaoidaw", 3)
    5
    """
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

print(longest_substring_distinct("aaaoidaw", 3))

