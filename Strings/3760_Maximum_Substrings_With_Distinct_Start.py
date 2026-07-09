class Solution:
    def maxDistinct(self, s: str) -> int:
        h = set()
        for each in s:
            if each not in h:
                h.add(each)
        return len(h)
        