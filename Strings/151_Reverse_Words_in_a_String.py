class Solution:
    def reverseWords(self, s: str) -> str:
        k = s.split()
        k.reverse()
        return ' '.join(k)
        
