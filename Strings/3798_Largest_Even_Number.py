class Solution:
    def largestEven(self, s: str) -> str:
        while s and s[-1] == '1':
                s = s[0:len(s)-1]
        return s
"""
class Solution:
    def largestEven(self, s: str) -> str:
        while True:
            if s and s[-1] == '1':
                s = s[0:len(s)-1]
            else:
                break
        return s
    
"""
