class Solution:
    def doesAliceWin(self, s: str) -> bool:
        
        for each in 'aeiou':
            if each in s:
                return True
        return False
