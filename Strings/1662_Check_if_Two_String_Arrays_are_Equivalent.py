class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        s1=""
        for each in word1:
            s1+=each
        
        s2=""
        for each in word2:
            s2+=each
        
        return s1 == s2
