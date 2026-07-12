class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for each in s:
            if each in d:
                d[each] += 1
            else:
                d[each] = 1
        i = 0
        while i < len(s):
            if d[s[i]] == 1:
                return i
            i += 1
        return -1


"""
from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)  # O(n) counting in optimized C code
        for i, ch in enumerate(s):  # O(n) scan
            if count[ch] == 1:
                return i
        return -1
"""
