class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if len(s)<2:
            return s
        if s == s[::-1]:
            return s
        x = ""
        for i in range(1,len(s)):
            x = x + s[-i]
            y = x + s
            if y == y[::-1]:
                return y
        
        
