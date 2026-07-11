class Solution:
    def countKeyChanges(self, s: str) -> int:
        count = 0
        i = 1
        while i < len(s):
            if s[i].lower() != s[i-1].lower():
                count += 1
            i += 1
        return count    
        
