class Solution:
    def scoreOfString(self, s: str) -> int:
        su = 0
        i = 0
        while i < len(s)-1:
            su += abs(ord(s[i]) - ord(s[i+1]))
            i += 1
        return su
        
