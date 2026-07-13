class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        s=word
        return s == s.upper() or s == s.lower() or s == s.capitalize()
        
