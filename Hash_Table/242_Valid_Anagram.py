class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d1 = {}
        for x in s:
            if x not in d1:
                d1[x] = 1
            else:
                d1[x] += 1
        
        d2 = {}
        for x in t:
            if x not in d2:
                d2[x] = 1
            else:
                d2[x] += 1
        for each in d1:
            if each not in d2:
                return False
            elif d1[each] != d2[each]:
                return False
        return True

        
"""
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(t) == Counter(s)
"""
