class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        k=sentence.split()
        for i in range(0,len(k)):
            if k[i].startswith(searchWord):
                return i+1
        else:
            return -1
        
