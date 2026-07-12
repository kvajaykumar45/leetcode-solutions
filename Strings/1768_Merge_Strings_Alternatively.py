class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m=""
        i=0
        while i < len(word1) and i < len(word2):
            m += word1[i] + word2[i]
            i += 1
        
        if i < len(word1):
            m += word1[i:]
        
        if i < len(word2):
            m += word2[i:]
        
        return m
        
