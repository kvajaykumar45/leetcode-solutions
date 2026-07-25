class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        maxdepth = 0
        for each in s:
            if each == '(':
                depth += 1
                maxdepth = max(depth, maxdepth)
            elif each == ')':
                depth -= 1
        return maxdepth
