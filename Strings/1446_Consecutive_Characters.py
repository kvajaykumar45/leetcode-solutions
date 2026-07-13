class Solution:
    def maxPower(self, s: str) -> int:
        maxcount = count = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
                
            else:
                maxcount = max(maxcount, count)
                count = 1
        
        return count if count>maxcount else maxcount





        
